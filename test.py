import sqlite3
import pandas as pd

operation_type = "Начисление"
json = ""
login_customer = "TOLOGONOVAB@URALSIB.RU"
value_operation = 100
status_operation = "Исполнен"
on_read = 1


db_path = r'C:\Users\TologonovAB\Desktop\shop_app\Convert\db\shop.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Выполняем запрос для получения данных из таблицы
query = """
SELECT login
FROM users
WHERE strftime('%m-%d', birth_date) = strftime('%m-%d', 'now')
"""
df = pd.read_sql_query(query, conn)


