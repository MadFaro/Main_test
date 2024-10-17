import pymysql

# Параметры подключения
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# Подключение
try:
    connection = pymysql.connect(user=config['user'], password=config['password'],
                                 host=config['host'], database=config['database'])

    with connection.cursor() as cursor:
        # Пример запроса
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print("Вы подключены к базе данных:", result)

except pymysql.MySQLError as error:
    print("Ошибка подключения к MariaDB:", error)

finally:
    connection.close()
    print("Соединение закрыто")

