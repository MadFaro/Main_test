import sqlite3
import pandas as pd
import json

db_path = r'C:\Users\TologonovAB\Desktop\shop_app\Convert\db\shop.db'
conn = sqlite3.connect(db_path)

# Выполняем запрос для получения данных из таблицы
query = """
SELECT id as ID,
       datetime_insert as DATE,
       operation_type as TYPE,
       json as JSON,
       login_customer as LOGIN
  FROM operations
  where operation_type = 'Покупка'
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
    expanded_rows.append(expanded_df)

# Объединяем все отдельные DataFrame в один
final_df = pd.concat(expanded_rows, ignore_index=True)

# Переупорядочиваем столбцы
final_df = final_df[['ID', 'DATE', 'TYPE', 'product_id', 'name', 'count', 'subtotal_price', 'size', 'color']]

# Закрываем соединение с базой данных
conn.close()

# Выводим финальный DataFrame
print(final_df)
