
    plsql_block = """
    DECLARE
        v_cur_threadid NUMBER;
        v_prev_threadid NUMBER := NULL;
        v_cur_department_id NUMBER;
        v_cur_state VARCHAR2(128); 
        v_cur_time DATE;
        v_start_time DATE := NULL; 
        v_end_time DATE := NULL;
        v_last_updated TIMESTAMP := :max_dtm;

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

    print("PL/SQL блок выполнен успешно.")
except cx_Oracle.DatabaseError as e:
    print("Ошибка выполнения PL/SQL блока:", e)
finally:
    cursor.close()
    oracle_conn.close()
