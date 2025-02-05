# Вставляем данные из DataFrame в таблицу product_sale
# Преобразуем данные из DataFrame в список кортежей для вставки в базу
records = final_df.to_records(index=False)
insert_query = """
    INSERT INTO product_sale (ID, DATE, TYPE, LOGIN, product_id, name, count, subtotal_price, size, color)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Вставляем все записи за один раз
cursor.executemany(insert_query, records)

# Сохраняем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()
