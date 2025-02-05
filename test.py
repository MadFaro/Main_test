import sqlite3
import psycopg2

# Подключаемся к SQLite
sqlite_conn = sqlite3.connect('my_database.sqlite')
sqlite_cursor = sqlite_conn.cursor()

# Подключаемся к PostgreSQL
pg_conn = psycopg2.connect(dbname="my_database", user="username", password="password", host="localhost")
pg_cursor = pg_conn.cursor()

# Получаем данные из SQLite
sqlite_cursor.execute("SELECT * FROM table_name")
rows = sqlite_cursor.fetchall()

# Получаем список столбцов
columns = [description[0] for description in sqlite_cursor.description]

# Формируем SQL запрос для вставки данных в PostgreSQL
insert_query = f"INSERT INTO table_name ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

# Вставляем данные в PostgreSQL
pg_cursor.executemany(insert_query, rows)

# Коммитим изменения и закрываем соединения
pg_conn.commit()

sqlite_conn.close()
pg_conn.close()
