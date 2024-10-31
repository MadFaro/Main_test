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
    'host': ',
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
        SELECT threadid, operatorfullname, operatorid, created, modified, state, offline as offline_, 
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

def upsert_data_to_oracle(rows):
    if not rows:
        print("Нет данных для загрузки.")
        return False

    try:
        oracle_conn = cx_Oracle.connect(user='', password='', dsn = '')
        cursor = oracle_conn.cursor()

        # Формируем SQL-запрос для MERGE
        merge_query = """
        MERGE INTO ANALYTICS.TOLOG_BI_WEBIM_CHATTHREAD target
        USING (
            SELECT :threadid AS threadid,
                   :operatorfullname AS operatorfullname,
                   :operatorid AS operatorid,
                   :created AS created,
                   :modified AS modified,
                   :state AS state,
                   :offline_ AS offline_,
                   :category AS category,
                   :subcategory AS subcategory,
                   :threadkind AS threadkind
            FROM dual
        ) source
        ON (target.threadid = source.threadid)
        WHEN MATCHED THEN
            UPDATE SET 
                target.operatorfullname = source.operatorfullname,
                target.operatorid = source.operatorid,
                target.created = source.created,
                target.modified = source.modified,
                target.state = source.state,
                target.offline_ = source.offline_,
                target.category = source.category,
                target.subcategory = source.subcategory,
                target.threadkind = source.threadkind
        WHEN NOT MATCHED THEN
            INSERT (threadid, operatorfullname, operatorid, created, modified, state, offline_, category, subcategory, threadkind)
            VALUES (source.threadid, source.operatorfullname, source.operatorid, source.created, source.modified, source.state, source.offline_, source.category, source.subcategory, source.threadkind)
        """

        for row in rows:
            if isinstance(row['threadkind'], set):
                row['threadkind'] = ', '.join(row['threadkind'])

            cursor.execute(merge_query, {
                'threadid': row['threadid'],
                'operatorfullname': row['operatorfullname'],
                'operatorid': row['operatorid'],
                'created': row['created'],
                'modified': row['modified'],
                'state': row['state'],
                'offline_': row['offline_'],
                'category': row['category'],
                'subcategory': row['subcategory'],
                'threadkind': row['threadkind']
            })

        oracle_conn.commit()
        print("Данные успешно загружены в Oracle.")
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

    print(f"Задача завершена: {datetime.now()}")

# Настройка расписания на каждые 5 минут
schedule.every(2).minutes.do(job)

# Основной цикл для выполнения задачи по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
