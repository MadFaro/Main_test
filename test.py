import mysql.connector
import cx_Oracle
import schedule
import time
from datetime import datetime

# Конфигурация подключения к MariaDB
mariadb_config = {
    'user': 'your_mariadb_username',
    'password': 'your_mariadb_password',
    'host': 'mariadb_host',
    'port': 3306,
    'database': 'your_mariadb_database'
}

# Конфигурация подключения к Oracle
oracle_dsn = cx_Oracle.makedsn("oracle_host", "oracle_port", service_name="your_service_name")
oracle_config = {
    'user': 'your_oracle_username',
    'password': 'your_oracle_password',
    'dsn': oracle_dsn
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
        SELECT threadid, operatorfullname, operatorid, created, modified, state, offline, 
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

def insert_data_to_oracle(rows):
    """Загружаем данные в Oracle без дублирования."""
    if not rows:
        print("Нет данных для загрузки.")
        return False

    try:
        oracle_conn = cx_Oracle.connect(**oracle_config)
        cursor = oracle_conn.cursor()

        for row in rows:
            # Проверяем наличие записи в Oracle по `threadid`, `created` и `modified`
            cursor.execute("""
            SELECT 1 FROM chatthread_oracle 
            WHERE threadid = :threadid AND created = :created AND modified = :modified
            """, {'threadid': row['threadid'], 'created': row['created'], 'modified': row['modified']})
            
            # Если запись не существует, вставляем её
            if not cursor.fetchone():
                cursor.execute("""
                INSERT INTO chatthread_oracle (threadid, operatorfullname, operatorid, created, modified, 
                                               state, offline, category, subcategory, threadkind)
                VALUES (:threadid, :operatorfullname, :operatorid, :created, :modified, 
                        :state, :offline, :category, :subcategory, :threadkind)
                """, row)

        # Подтверждаем изменения
        oracle_conn.commit()
        print("Данные успешно загружены в Oracle.")
        return True  # Возвращаем True, если загрузка прошла успешно
        
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
    if insert_data_to_oracle(rows):
        # Обновляем метку времени, если загрузка прошла успешно
        new_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_last_load_timestamp(new_timestamp)
        print("Метка времени обновлена:", new_timestamp)

    print(f"Задача завершена: {datetime.now()}")

# Настройка расписания на каждые 5 минут
schedule.every(5).minutes.do(job)

# Основной цикл для выполнения задачи по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)

