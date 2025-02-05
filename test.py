import sqlite3
import psycopg2

# Подключение к SQLite
sqlite_conn = sqlite3.connect('path_to_your_sqlite.db')
sqlite_cursor = sqlite_conn.cursor()

# Подключение к PostgreSQL
pg_conn = psycopg2.connect(host="localhost", dbname="shop_app", user="postgres", password="yourpassword")
pg_cursor = pg_conn.cursor()

# Получаем все таблицы из SQLite
sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = sqlite_cursor.fetchall()

for table in tables:
    table_name = table[0]

    # Получаем все данные из таблицы SQLite
    sqlite_cursor.execute(f"SELECT * FROM {table_name}")
    rows = sqlite_cursor.fetchall()

    # Получаем описание структуры таблицы
    sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
    columns = sqlite_cursor.fetchall()

    # Формируем запрос для создания таблицы в PostgreSQL
    create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    create_query += ", ".join([f"{column[1]} TEXT" for column in columns])  # Учитываем, что все столбцы будут текстовыми
    create_query += ");"

    # Создаем таблицу в PostgreSQL
    pg_cursor.execute(create_query)

    # Переносим данные из SQLite в PostgreSQL
    insert_query = f"INSERT INTO {table_name} ({', '.join([column[1] for column in columns])}) VALUES %s"
    pg_cursor.executemany(insert_query, rows)

# Подтверждаем изменения и закрываем соединения
pg_conn.commit()
sqlite_conn.close()
pg_conn.close()

print("Данные успешно перенесены из SQLite в PostgreSQL!")

