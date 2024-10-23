import pymysql
import pandas as pd

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

    # Пример запроса через pandas
    query = "select * from chatthread where created >= date(now());"
    
    # Выполнение запроса и сохранение результата в DataFrame
    df = pd.read_sql(query, connection)
    
    print("Результаты запроса:")
    print(df)

except pymysql.MySQLError as error:
    print("Ошибка подключения к MariaDB:", error)

finally:
    connection.close()
    print("Соединение закрыто")
