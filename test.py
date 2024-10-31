def upsert_data_to_oracle(rows):
    """Добавляем или обновляем данные в Oracle с использованием MERGE."""
    if not rows:
        print("Нет данных для загрузки.")
        return False

    try:
        oracle_conn = cx_Oracle.connect(**oracle_config)
        cursor = oracle_conn.cursor()

        # Формируем SQL-запрос для MERGE
        merge_query = """
        MERGE INTO chatthread_oracle target
        USING (
            SELECT :threadid AS threadid,
                   :operatorfullname AS operatorfullname,
                   :operatorid AS operatorid,
                   :created AS created,
                   :modified AS modified,
                   :state AS state,
                   :offline AS offline,
                   :category AS category,
                   :subcategory AS subcategory,
                   :threadkind AS threadkind
            FROM dual
        ) source
        ON (target.threadid = source.threadid)
        WHEN MATCHED THEN
            UPDATE SET 
                target.operatorfullname = source.operatorfullname,
                target.operatorid = source.operatorid,
                target.created = source.created,
                target.modified = source.modified,
                target.state = source.state,
                target.offline = source.offline,
                target.category = source.category,
                target.subcategory = source.subcategory,
                target.threadkind = source.threadkind
        WHEN NOT MATCHED THEN
            INSERT (threadid, operatorfullname, operatorid, created, modified, state, offline, category, subcategory, threadkind)
            VALUES (source.threadid, source.operatorfullname, source.operatorid, source.created, source.modified, source.state, source.offline, source.category, source.subcategory, source.threadkind)
        """

        for row in rows:
            # Преобразование threadkind в строку, если это set
            if isinstance(row['threadkind'], set):
                row['threadkind'] = ', '.join(row['threadkind'])  # Преобразуем в строку

            print("Обрабатываем запись:", row)  # Отладочный вывод

            # Выполняем MERGE
            cursor.execute(merge_query, {
                'threadid': row['threadid'],
                'operatorfullname': row['operatorfullname'],
                'operatorid': row['operatorid'],
                'created': row['created'],
                'modified': row['modified'],
                'state': row['state'],
                'offline': row['offline'],
                'category': row['category'],
                'subcategory': row['subcategory'],
                'threadkind': row['threadkind']
            })

        # Подтверждаем изменения
        oracle_conn.commit()
        print("Данные успешно загружены в Oracle.")
        return True  # Возвращаем True, если загрузка прошла успешно

    except cx_Oracle.DatabaseError as e:
        print("Ошибка подключения к Oracle:", e)
        return False

    finally:
        cursor.close()
        oracle_conn.close()
