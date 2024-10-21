import sqlite3
from datetime import datetime, timedelta

# Путь к базе данных
db_path = r'C:\Users\TologonovAB\Desktop\shop_app\Convert\db\shop.db'

# Подключение к базе данных
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Получаем текущее время
current_time = datetime.now()

# Вычисляем время одного часа назад
one_hour_ago = current_time - timedelta(hours=1)

# Удаляем записи, где сессия длится больше одного часа
cursor.execute("""
    DELETE FROM session
    WHERE start_time <= ?
""", (one_hour_ago,))

# Подтверждаем изменения
conn.commit()

# Закрываем соединение
conn.close()

print("Все записи, которые длились больше часа, успешно удалены.")
