def fetch_data_from_mariadb(last_load_timestamp):
    """Извлекаем данные из MariaDB с учётом метки времени."""
    try:
        mariadb_conn = mysql.connector.connect(**mariadb_config)
        cursor = mariadb_conn.cursor(dictionary=True)
        
        # SQL-запрос для извлечения данных после последней загрузки
        query = """
        SELECT threadid, operatorfullname, operatorid, created, modified, state, offline AS offline_, 
               category, subcategory, threadkind 
        FROM chatthread 
        WHERE created > %s OR modified > %s;
        """
        cursor.execute(query, (last_load_timestamp, last_load_timestamp))
        rows = cursor.fetchall()

        with open(log_file, 'a') as file:
            file.write(f"\n{str(len(rows))} select rows is chatthread.")
        return rows

    except mysql.connector.Error as e:
        with open(log_file, 'a') as file:
            file.write(f"\nerror connect chatthread: {str(e)}")
        return []
    
    finally:
        if mariadb_conn.is_connected():
            cursor.close()
            mariadb_conn.close()

def upsert_data_to_oracle_sl(max_dtm):
    try:
        oracle_conn = cx_Oracle.connect(user='', password='', dsn = '')
        cursor = oracle_conn.cursor()

        #cursor.execute("delete from ANALYTICS.TOLOG_BI_WEBIM_STATS_SERVICE_LEVEL where GOT_INTO_COMMON_QUEUE_TIME >= %s", (max_dtm,))

        # Формируем SQL-запрос для MERGE
        plsql_block = """
            DECLARE
                v_cur_threadid NUMBER;
                v_prev_threadid NUMBER := NULL;
                v_cur_department_id NUMBER;
                v_cur_state VARCHAR2(128); 
                v_cur_time DATE;
                v_start_time DATE := NULL; 
                v_end_time DATE := NULL;
                v_last_updated TIMESTAMP := TO_TIMESTAMP(:max_dtm, 'YYYY-MM-DD HH24:MI:SS');

                CURSOR cur IS
                    SELECT cth.threadid, cth.departmentid, cth.state, cth.dtm 
                    FROM ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY cth
                    JOIN ANALYTICS.TOLOG_BI_WEBIM_CHATTHREAD ct ON ct.threadid = cth.threadid
                    WHERE (ct.created > v_last_updated OR cth.dtm > v_last_updated)
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

            # Выполнение PL/SQL блока с передачей параметра
        cursor.execute(plsql_block, max_dtm=max_dtm)
        oracle_conn.commit()
        
        return True 

    except cx_Oracle.DatabaseError as e:
        with open(log_file, 'a') as file:
            file.write(f"\nerror connect Oracle:{str(e)}") 
        return False

    finally:
        cursor.close()
        oracle_conn.close()
