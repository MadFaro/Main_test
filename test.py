import pymysql

# Параметры подключения
config = {
    'user': '',
    'password': '',
    'host': '',
    'port': '',
    'database': ''
}

# Подключение
try:
    connection = pymysql.connect(user=config['user'], password=config['password'],
                                 host=config['host'], port=config['port'], database=config['database'])

    with connection.cursor() as cursor:
        # Пример запроса
        cursor.execute("select * from chatthread where created >= date(now());")
        result = cursor.fetchone()
        print("Вы подключены к базе данных:", result)

except pymysql.MySQLError as error:
    print("Ошибка подключения к MariaDB:", error)

finally:
    connection.close()
    print("Соединение закрыто")
