def get_max_dtm_from_oracle():
    """Получаем максимальную дату DTM из Oracle."""
    try:
        oracle_conn = cx_Oracle.connect(user='', password='', dsn='')
        cursor = oracle_conn.cursor()

        # SQL-запрос для получения максимальной даты DTM
        query = "SELECT NVL(MAX(DTM), NULL) FROM ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY"
        cursor.execute(query)
        max_dtm = cursor.fetchone()[0]

        # Проверяем, если дата пустая, возвращаем начало текущего дня
        if max_dtm is None:
            return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        return max_dtm

    except cx_Oracle.DatabaseError as e:
        print("Ошибка подключения к Oracle:", e)
        # Возвращаем текущую дату и время в случае ошибки
        return datetime.now()

    finally:
        cursor.close()
        oracle_conn.close()
