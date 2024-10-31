import mysql.connector
import cx_Oracle
from sqlalchemy import create_engine, VARCHAR, FLOAT, NUMERIC
import schedule
import time
from datetime import datetime, timedelta

# Конфигурация подключения к MariaDB
mariadb_config = {
    'user': '',
    'password': '',
    'host': '',
    'port': 3306,
    'database': ''
}

# Путь к файлу для хранения метки времени последней загрузки
last_load_timestamp_file = 'last_load_timestamp.txt'

def read_last_load_timestamp():
    """Чтение метки времени последней загрузки из файла."""
    try:
        with open(last_load_timestamp_file, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        # Если файл не найден, возвращаем начало текущего дня
        current_date = datetime.now().strftime('%Y-%m-%d')
        return f"{current_date} 00:00:00"

def update_last_load_timestamp(timestamp):
    """Обновление метки времени последней загрузки в файле."""
    with open(last_load_timestamp_file, 'w') as f:
        f.write(timestamp)

def fetch_data_from_mariadb(last_load_timestamp):
    """Извлекаем данные из MariaDB с учётом метки времени."""
    try:
        mariadb_conn = mysql.connector.connect(**mariadb_config)
        cursor = mariadb_conn.cursor(dictionary=True)
        
        # SQL-запрос для извлечения данных после последней загрузки
        query = """
        SELECT threadid, operatorfullname, operatorid, created, modified, state, offline AS offline_, 
               category, subcategory, threadkind 
        FROM chatthread 
        WHERE created > %s OR modified > %s;
        """
        cursor.execute(query, (last_load_timestamp, last_load_timestamp))
        rows = cursor.fetchall()
        
        print(f"{len(rows)} записей извлечено из MariaDB.")
        return rows

    except mysql.connector.Error as e:
        print("Ошибка подключения к MariaDB:", e)
        return []
    
    finally:
        if mariadb_conn.is_connected():
            cursor.close()
            mariadb_conn.close()

def fetch_history_data_from_mariadb(last_load_timestamp):
    """Извлекаем данные из chatthreadhistory в MariaDB с учётом метки времени."""
    try:
        mariadb_conn = mysql.connector.connect(**mariadb_config)
        cursor = mariadb_conn.cursor(dictionary=True)

        # SQL-запрос для извлечения данных из chatthreadhistory
        query = """
        SELECT THREADHISTORYID, THREADID, NUMBER AS NUMBER_, DTM, STATE, OPERATORID, DEPARTMENTID, EVENT 
        FROM chatthreadhistory 
        WHERE DTM >= %s;
        """
        cursor.execute(query, (last_load_timestamp,))
        rows = cursor.fetchall()
        
        print(f"{len(rows)} записей извлечено из chatthreadhistory.")
        return rows

    except mysql.connector.Error as e:
        print("Ошибка подключения к MariaDB:", e)
        return []
    
    finally:
        if mariadb_conn.is_connected():
            cursor.close()
            mariadb_conn.close()

def get_max_dtm_from_oracle():
    """Получаем максимальную дату DTM из Oracle."""
    try:
        oracle_conn = cx_Oracle.connect(user='', password='', dsn='')
        cursor = oracle_conn.cursor()

        # SQL-запрос для получения максимальной даты DTM
        query = "SELECT NVL(MAX(DTM), TO_DATE('2000-01-01', 'YYYY-MM-DD')) FROM ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY"
        cursor.execute(query)
        max_dtm = cursor.fetchone()[0]

        return max_dtm

    except cx_Oracle.DatabaseError as e:
        print("Ошибка подключения к Oracle:", e)
        return datetime(2000, 1, 1)  # Возвращаем начальную дату в случае ошибки

    finally:
        cursor.close()
        oracle_conn.close()

def upsert_history_data_to_oracle(rows):
    """Добавляем или обновляем историю чатов в Oracle с использованием MERGE и пакетной обработки."""
    if not rows:
        print("Нет данных для загрузки истории.")
        return False

    try:
        oracle_conn = cx_Oracle.connect(user='', password='', dsn='')
        cursor = oracle_conn.cursor()

        # Формируем SQL-запрос для MERGE
        merge_query = """
        MERGE INTO ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY target
        USING (
            SELECT :threadhistoryid AS threadhistoryid,
                   :threadid AS threadid,
                   :number_ AS number_,
                   :dtm AS dtm,
                   :state AS state,
                   :operatorid AS operatorid,
                   :departmentid AS departmentid,
                   :event AS event
            FROM dual
        ) source
        ON (target.threadhistoryid = source.threadhistoryid)
        WHEN MATCHED THEN
            UPDATE SET 
                target.threadid = source.threadid,
                target.number_ = source.number_,
                target.dtm = source.dtm,
                target.state = source.state,
                target.operatorid = source.operatorid,
                target.departmentid = source.departmentid,
                target.event = source.event
        WHEN NOT MATCHED THEN
            INSERT (threadhistoryid, threadid, number_, dtm, state, operatorid, departmentid, event)
            VALUES (source.threadhistoryid, source.threadid, source.number_, source.dtm, source.state, source.operatorid, source.departmentid, source.event)
        """

        for row in rows:
            cursor.execute(merge_query, {
                'threadhistoryid': row['THREADHISTORYID'],
                'threadid': row['THREADID'],
                'number_': row['NUMBER_'],
                'dtm': row['DTM'],
                'state': row['STATE'],
                'operatorid': row['OPERATORID'],
                'departmentid': row['DEPARTMENTID'],
                'event': row['EVENT']
            })

        oracle_conn.commit()
        print("Данные истории успешно загружены в Oracle.")
        return True 

    except cx_Oracle.DatabaseError as e:
        print("Ошибка подключения к Oracle:", e)
        return False

    finally:
        cursor.close()
        oracle_conn.close()

def job():
    """Основная задача для выполнения каждые 5 минут."""
    print(f"Запуск задачи: {datetime.now()}")

    # Читаем метку времени последней загрузки
    last_load_timestamp = read_last_load_timestamp()
    print("Последняя загрузка данных была:", last_load_timestamp)
    
    # Получаем новые или обновленные данные
    rows = fetch_data_from_mariadb(last_load_timestamp)

    # Загружаем данные в Oracle
    if upsert_data_to_oracle(rows):
        # Обновляем метку времени, если загрузка прошла успешно
        new_timestamp = (datetime.now() - timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S')
        update_last_load_timestamp(new_timestamp)
        print("Метка времени обновлена:", new_timestamp)

    # Получаем максимальную дату DTM из Oracle
    max_dtm = get_max_dtm_from_oracle()
    print("Максимальная дата DTM из Oracle:", max_dtm)

    # Читаем метку времени для истории из файла
    last_load_timestamp_history = max_dtm.strftime('%Y-%m-%d %H:%M:%S')
    
    # Получаем новые или обновленные данные для истории
    history_rows = fetch_history_data_from_mariadb(last_load_timestamp_history)

    # Загружаем данные истории в Oracle
    if upsert_history_data_to_oracle(history_rows):
        # Обновляем метку времени для истории
        new_timestamp_history = (datetime.now() - timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S')
        update_last_load_timestamp(new_timestamp_history)
        print("Метка времени для истории обновлена:", new_timestamp_history)

    print(f"Задача завершена: {datetime.now()}")

# Настройка расписания на каждые 5 минут
schedule.every(5).minutes.do(job)

# Основной цикл для выполнения задачи по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)

