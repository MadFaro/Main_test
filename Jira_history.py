# Запрос для получения максимальной даты
query = "SELECT MAX(date_column) FROM your_table"

# Выполнение запроса и получение результата
cursor = connection.cursor()
cursor.execute(query)
max_date = cursor.fetchone()[0]

# Закрытие курсора и соединения
cursor.close()
connection.close()

print(f"Max date from SQL table: {max_date}")
