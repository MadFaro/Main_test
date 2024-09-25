import sqlite3
import pandas as pd
import json

# Подключаемся к базе данных SQLite
conn = sqlite3.connect('database.db')

# Выполняем запрос для получения данных из таблицы
query = "SELECT ID, DATE, TYPE, JSON FROM your_table"
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
    expanded_rows.append(expanded_df)

# Объединяем все отдельные DataFrame в один
final_df = pd.concat(expanded_rows, ignore_index=True)

# Переупорядочиваем столбцы
final_df = final_df[['ID', 'DATE', 'TYPE', 'product_id', 'name', 'count', 'subtotal_price', 'size', 'color']]

# Закрываем соединение с базой данных
conn.close()

# Выводим финальный DataFrame
print(final_df)
