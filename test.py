CREATE OR REPLACE PROCEDURE tolog_test AS
    v_cur_threadid NUMBER;
    v_prev_threadid NUMBER := NULL;
    v_cur_department_id NUMBER;
    v_cur_state VARCHAR2(128); 
    v_cur_time DATE;
    v_start_time DATE := NULL; 
    v_end_time DATE := NULL;

    CURSOR cur IS
        SELECT cth.threadid, cth.departmentid, cth.state, cth.dtm 
        FROM ANALYTICS.TOLOG_CHATTHREADHISTORY cth
        JOIN ANALYTICS.TOLOG_CHATTHREAD ct ON ct.threadid = cth.threadid
        WHERE ct.created BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
          AND ct.offline_ = 0
          AND cth.dtm BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
        ORDER BY cth.threadid, cth.dtm;

BEGIN
    OPEN cur;
    LOOP
        FETCH cur INTO v_cur_threadid, v_cur_department_id, v_cur_state, v_cur_time;
        EXIT WHEN cur%NOTFOUND;

        -- Сбрасываем начальные значения, если новый threadid
        IF v_prev_threadid IS NULL OR v_prev_threadid <> v_cur_threadid THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        -- Сбрасываем начальные и конечные времена для определенных состояний
        IF v_cur_state IN ('chatting_with_robot', 'closed_by_operator', 'on_hold') THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        -- Устанавливаем v_start_time при состоянии 'queue'
        IF v_cur_state = 'queue' AND v_start_time IS NULL THEN
            v_start_time := v_cur_time;
        END IF;

        -- Пытаемся найти v_end_time при состоянии 'chatting'
        IF v_cur_state = 'chatting' AND v_start_time IS NOT NULL THEN
            BEGIN
                SELECT created
                INTO v_end_time
                FROM (
                    SELECT created
                    FROM ANALYTICS.TOLOG_CHATMESSAGE
                    WHERE threadid = v_cur_threadid
                      AND kind IN (2, 10, 13)
                      AND created >= v_cur_time
                    ORDER BY created
                )
                WHERE ROWNUM = 1;
            EXCEPTION
                WHEN NO_DATA_FOUND THEN
                    v_end_time := NULL;
            END;
        END IF;

        -- Вставляем данные в таблицу, если есть начало и конец интервала
        IF v_start_time IS NOT NULL AND v_end_time IS NOT NULL THEN
            INSERT INTO ANALYTICS.TOLOG_TMP_WEB (
                threadid, department_id, got_into_common_queue_time, start_chatting_time
            ) VALUES (
                v_cur_threadid, v_cur_department_id, v_start_time, v_end_time
            );
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        -- Сохраняем текущий threadid для следующей итерации
        v_prev_threadid := v_cur_threadid;
    END LOOP;

    CLOSE cur;
    COMMIT;
END;
/
