import sqlite3

db_path = r'C:\Users\TologonovAB\Desktop\shop_app\Convert\db\shop.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('DELETE FROM session')
conn.commit()
conn.close()

print("Все записи из таблицы 'session' успешно удалены.")
