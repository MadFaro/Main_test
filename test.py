def upsert_data_to_oracle(rows):
    """Добавляем или обновляем данные в Oracle на основании уникальных ключей и поля modified."""
    if not rows:
        print("Нет данных для загрузки.")
        return False

    try:
        oracle_conn = cx_Oracle.connect(**oracle_config)
        cursor = oracle_conn.cursor()

        for row in rows:
            # Проверяем наличие записи в Oracle по `threadid`
            cursor.execute("""
            SELECT modified FROM chatthread_oracle 
            WHERE threadid = :threadid
            """, {'threadid': row['threadid']})
            
            existing_record = cursor.fetchone()
            
            # Если запись не существует, добавляем её
            if existing_record is None:
                cursor.execute("""
                INSERT INTO chatthread_oracle (threadid, operatorfullname, operatorid, created, modified, 
                                               state, offline, category, subcategory, threadkind)
                VALUES (:threadid, :operatorfullname, :operatorid, :created, :modified, 
                        :state, :offline, :category, :subcategory, :threadkind)
                """, {
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
                print(f"Добавлена новая запись: threadid = {row['threadid']}")

            # Если запись существует, но обновлена, перезаписываем её
            elif existing_record[0] < row['modified']:
                cursor.execute("""
                UPDATE chatthread_oracle 
                SET operatorfullname = :operatorfullname, operatorid = :operatorid, created = :created, 
                    modified = :modified, state = :state, offline = :offline, category = :category, 
                    subcategory = :subcategory, threadkind = :threadkind
                WHERE threadid = :threadid
                """, {
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
                print(f"Обновлена запись: threadid = {row['threadid']}")

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
