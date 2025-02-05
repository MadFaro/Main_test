import sqlite3
import psycopg2
from psycopg2 import extras

# Функция для преобразования типов SQLite в PostgreSQL
def map_sqlite_type_to_postgres(sqlite_type):
    sqlite_type = sqlite_type.upper()
    if "INT" in sqlite_type:
        return "INTEGER"
    elif "TEXT" in sqlite_type or "CHAR" in sqlite_type or "CLOB" in sqlite_type:
        return "TEXT"
    elif "REAL" in sqlite_type or "FLOA" in sqlite_type or "DOUB" in sqlite_type:
        return "DOUBLE PRECISION"
    elif "BLOB" in sqlite_type:
        return "BYTEA"
    elif "NUMERIC" in sqlite_type or "DECIMAL" in sqlite_type:
        return "NUMERIC"
    else:
        return "TEXT"  # По умолчанию, если тип неизвестен

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

    # Получаем структуру таблицы
    sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
    columns = sqlite_cursor.fetchall()

    column_definitions = []
    column_names = []

    for column in columns:
        col_name = column[1]
        col_type = map_sqlite_type_to_postgres(column[2])  # Преобразование типа
        not_null = " NOT NULL" if column[3] else ""  # Проверка NOT NULL
        primary_key = " PRIMARY KEY" if column[5] else ""  # Проверка PRIMARY KEY
        column_definitions.append(f"{col_name} {col_type}{not_null}{primary_key}")
        column_names.append(col_name)

    # Создаем таблицу в PostgreSQL
    create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_definitions)});"
    pg_cursor.execute(create_query)

    # Получаем все данные из таблицы SQLite
    sqlite_cursor.execute(f"SELECT * FROM {table_name}")
    rows = sqlite_cursor.fetchall()

    if rows:  # Если таблица не пустая
        insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES %s"
        extras.execute_values(pg_cursor, insert_query, rows)

# Подтверждаем изменения и закрываем соединения
pg_conn.commit()
sqlite_conn.close()
pg_conn.close()

print("Данные успешно перенесены из SQLite в PostgreSQL!")

