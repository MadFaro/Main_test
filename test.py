# Вставляем все записи за один раз
cursor.executemany(insert_query, records)

# Сохраняем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()
