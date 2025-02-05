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
SELECT id as ID,
       datetime_insert as DATE,
       operation_type as TYPE,
       json as JSON,
       login_customer as LOGIN
  FROM operations
  WHERE operation_type = 'Покупка' and status_operation = 'Исполнен'
"""
df = pd.read_sql_query(query, conn)

# Функция для преобразования JSON-строки в DataFrame
def expand_json(json_str):
    products = json.loads(json_str)
    return pd.DataFrame(products)

# Создаем пустой список для сохранения новых строк
expanded_rows = []

# Проходим по каждой строке в исходном датафрейме
for idx, row in df.iterrows():
    json_data = row['JSON']
    expanded_df = expand_json(json_data)
    expanded_df['ID'] = row['ID']
    expanded_df['DATE'] = row['DATE']
    expanded_df['TYPE'] = row['TYPE']
    expanded_df['LOGIN'] = row['LOGIN']  # Добавляем LOGIN в каждую запись
    expanded_rows.append(expanded_df)

# Объединяем все отдельные DataFrame в один
final_df = pd.concat(expanded_rows, ignore_index=True)

# Переупорядочиваем столбцы
final_df = final_df[['ID', 'DATE', 'TYPE', 'LOGIN', 'product_id', 'name', 'count', 'subtotal_price', 'size', 'color']]

# Подключаемся к базе для выполнения SQL-запросов
cursor = conn.cursor()

# Очищаем таблицу product_sale перед вставкой новых данных
cursor.execute("TRUNCATE TABLE product_sale RESTART IDENTITY")

# Преобразуем данные из DataFrame в список кортежей для вставки в базу
records = final_df.to_records(index=False)
insert_query = """
    INSERT INTO product_sale (ID, DATE, TYPE, LOGIN, product_id, name, count, subtotal_price, size, color)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Вставляем все записи за один раз
cursor.executemany(insert_query, records)

# Сохраняем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()
