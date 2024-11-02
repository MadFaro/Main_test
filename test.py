def upsert_data_to_oracle_sl(rows):
    """Вставка данных и выполнение PL/SQL блока с учетом существующих threadid."""
    try:
        oracle_conn = cx_Oracle.connect(user='your_user', password='your_password', dsn='your_dsn')
        cursor = oracle_conn.cursor()

        # Извлекаем уникальные threadid из rows
        thread_ids = list(set(row['threadid'] for row in rows))
        
        # Определяем размер партии (1000 - оптимальное значение для Oracle)
        batch_size = 1000
        thread_id_batches = [thread_ids[i:i + batch_size] for i in range(0, len(thread_ids), batch_size)]

        # Удаление данных из таблицы по каждой партии threadid
        for batch in thread_id_batches:
            thread_ids_str = ', '.join(map(str, batch))
            delete_query = f"DELETE FROM ANALYTICS.TOLOG_BI_WEBIM_STATS_SERVICE_LEVEL WHERE threadid IN ({thread_ids_str})"
            cursor.execute(delete_query)
            oracle_conn.commit()

        # Подготовка PL/SQL блока для обработки данных
        plsql_block = """
            DECLARE
                v_cur_threadid NUMBER;
                v_prev_threadid NUMBER := NULL;
                v_cur_department_id NUMBER;
                v_cur_state VARCHAR2(128); 
                v_cur_time DATE;
                v_start_time DATE := NULL; 
                v_end_time DATE := NULL;

                CURSOR cur IS
                    SELECT cth.threadid, cth.departmentid, cth.state, cth.dtm 
                    FROM ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY cth
                    JOIN ANALYTICS.TOLOG_BI_WEBIM_CHATTHREAD ct ON ct.threadid = cth.threadid
                    WHERE cth.threadid IN ({})
                    ORDER BY cth.threadid, cth.dtm;

            BEGIN
                OPEN cur;
                LOOP
                    FETCH cur INTO v_cur_threadid, v_cur_department_id, v_cur_state, v_cur_time;
                    EXIT WHEN cur%NOTFOUND;

                    IF v_prev_threadid IS NULL OR v_prev_threadid <> v_cur_threadid THEN
                        v_start_time := NULL;
                        v_end_time := NULL;
                    END IF;

                    IF v_cur_state IN ('chatting_with_robot', 'closed_by_operator', 'on_hold') THEN
                        v_start_time := NULL;
                        v_end_time := NULL;
                    END IF;

                    IF v_cur_state = 'queue' AND v_start_time IS NULL THEN
                        v_start_time := v_cur_time;
                    END IF;

                    IF v_cur_state = 'chatting' AND v_start_time IS NOT NULL THEN 
                        SELECT MIN(cm.created)
                        INTO v_end_time
                        FROM ANALYTICS.TOLOG_BI_WEBIM_CHATMESSAGE cm
                        WHERE cm.threadid = v_cur_threadid
                        AND cm.kind IN (2, 10, 13)
                        AND cm.created > v_cur_time;

                        IF v_end_time IS NOT NULL THEN
                            INSERT INTO ANALYTICS.TOLOG_BI_WEBIM_STATS_SERVICE_LEVEL (
                                threadid, department_id, got_into_common_queue_time, start_chatting_time
                            ) VALUES (
                                v_cur_threadid, v_cur_department_id, v_start_time, v_end_time
                            );

                            v_start_time := NULL;
                            v_end_time := NULL;
                        END IF;
                    END IF;

                    v_prev_threadid := v_cur_threadid;
                END LOOP;
                CLOSE cur;
                COMMIT;
            END;
            """

        # Выполнение PL/SQL блока для каждой партии threadid
        for batch in thread_id_batches:
            thread_ids_str = ', '.join(map(str, batch))
            cursor.execute(plsql_block.format(thread_ids_str))
            oracle_conn.commit()

        return True 

    except cx_Oracle.DatabaseError as e:
        with open(log_file, 'a') as file:
            file.write(f"\nОшибка подключения к Oracle: {str(e)}") 
        return False

    finally:
        cursor.close()
        oracle_conn.close()
