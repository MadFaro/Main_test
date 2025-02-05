import psycopg2
import pandas as pd
import json

# Подключаемся к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="your_database_name", 
    user="your_username", 
    password="your_password", 
    host="localhost"
)

# Выполняем запрос для получения данных из таблицы
query = """
SELECT id as id,
       datetime_insert as date,
       operation_type as type,
       json as json,
       login_customer as login
  FROM operations
  WHERE operation_type = 'Покупка' and status_operation = 'Исполнен'
"""
df = pd.read_sql_query(query, conn)

# Проверяем столбцы в датафрейме
print("Columns in the DataFrame:", df.columns)

# Функция для преобразования JSON-строки в DataFrame
def expand_json(json_str):
    products = json.loads(json_str)
    return pd.DataFrame(products)

# Создаем пустой список для сохранения новых строк
expanded_rows = []

# Проходим по каждой строке в исходном датафрейме
for idx, row in df.iterrows():
    json_data = row['json']
    expanded_df = expand_json(json_data)
    expanded_df['id'] = row['id']
    expanded_df['date'] = row['date']
    expanded_df['type'] = row['type']
    expanded_df['login'] = row['login']  # Добавляем login в каждую запись
    expanded_rows.append(expanded_df)

# Объединяем все отдельные DataFrame в один
final_df = pd.concat(expanded_rows, ignore_index=True)

# Переупорядочиваем столбцы
final_df = final_df[['id', 'date', 'type', 'login', 'product_id', 'name', 'count', 'subtotal_price', 'size', 'color']]

# Приводим все столбцы с числовыми значениями к стандартным типам Python
final_df['id'] = final_df['id'].astype(int)
final_df['product_id'] = final_df['product_id'].astype(int)
final_df['count'] = final_df['count'].astype(int)
final_df['subtotal_price'] = final_df['subtotal_price'].astype(float)

# Преобразуем DataFrame в список кортежей, чтобы psycopg2 мог вставить данные
records = [tuple(x) for x in final_df.to_numpy()]

# Подключаемся к базе для выполнения SQL-запросов
cursor = conn.cursor()

# Очищаем таблицу product_sale перед вставкой новых данных
cursor.execute("TRUNCATE TABLE product_sale RESTART IDENTITY")

# SQL-запрос для вставки данных
insert_query = """
    INSERT INTO product_sale (id, date, type, login, product_id, name, count, subtotal_price, size, color)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Вставляем все записи за один раз
cursor.executemany(insert_query, records)

# Сохраняем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()
