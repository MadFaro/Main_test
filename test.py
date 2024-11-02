def upsert_data_to_oracle_sl(rows):
    if not rows:
        print("Нет данных для обработки.")
        return False

    try:
        oracle_conn = cx_Oracle.connect(user='', password='', dsn='')
        cursor = oracle_conn.cursor()

        # Получаем уникальные threadid
        thread_ids = [row['threadid'] for row in rows]
        unique_thread_ids = list(set(thread_ids))

        # Создаем arrayvar для передачи в PL/SQL
        thread_id_array = cursor.arrayvar(cx_Oracle.NUMBER, unique_thread_ids)

        # Удаление данных из витрины по каждому threadid
        for thread_id in unique_thread_ids:
            cursor.execute(
                "DELETE FROM ANALYTICS.TOLOG_BI_WEBIM_STATS_SERVICE_LEVEL WHERE threadid = :thread_id",
                thread_id=thread_id
            )
        oracle_conn.commit()
        print(f"Удалены данные по {len(unique_thread_ids)} уникальным threadid.")

        # PL/SQL блок для обработки данных
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
                WHERE cth.threadid IN (SELECT COLUMN_VALUE FROM TABLE(:thread_ids))
                AND ct.offline_ = 0
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

        # Передача arrayvar в PL/SQL блок
        cursor.execute(plsql_block, thread_ids=thread_id_array)
        oracle_conn.commit()

        print("PL/SQL блок выполнен успешно.")
        return True

    except cx_Oracle.DatabaseError as e:
        with open(log_file, 'a') as file:
            file.write(f"\nОшибка при подключении к Oracle: {str(e)}")
        return False

    finally:
        cursor.close()
        oracle_conn.close()
