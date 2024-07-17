CREATE OR REPLACE PROCEDURE tolog_webim_sl (
    p_dtmfrom IN DATE,
    p_dtmto IN DATE,
    p_departmentid IN NUMBER,
    p_locale IN CHAR
) AS
    v_cur_threadid NUMBER;
    v_prev_threadid NUMBER := NULL;
    v_cur_department_id NUMBER;
    v_cur_state VARCHAR2(128);
    v_cur_time DATE;
    v_start_time DATE := NULL;
    v_end_time DATE := NULL;
    CURSOR cur IS
        SELECT cth.threadid, cth.departmentid, cth.state, cth.dtm 
        FROM ODS.ODS_WIS_chatthreadhistory@cdw.prod cth
        JOIN ODS.ODS_WIS_chatthread@cdw.prod ct ON ct.threadid = cth.threadid
        WHERE ct.created BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
          AND ct.offline_ = 0
          AND cth.dtm BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
        ORDER BY cth.threadid, cth.dtm;
BEGIN
    OPEN cur;
    LOOP
        FETCH cur INTO v_cur_threadid, v_cur_department_id, v_cur_state, v_cur_time;
        EXIT WHEN cur%NOTFOUND;

        -- Сбрасываем для каждого нового треда
        IF v_prev_threadid IS NULL OR v_prev_threadid <> v_cur_threadid THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        -- Если сначала чат попал на бота, то учитываем время попадания в очередь после бота.
        -- Не учитываем диалог, если он не был в состоянии chatting и был закрыт оператором.
        IF v_cur_state IN ('chatting_with_robot', 'closed_by_operator') THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        IF v_cur_state = 'queue' AND v_start_time IS NULL THEN
            v_start_time := v_cur_time;
        END IF;

        IF v_cur_state = 'chatting' AND v_start_time IS NOT NULL THEN 
            SELECT MIN(cm.created)
            INTO v_end_time
            FROM ODS.ODS_WIS_CHATMESSAGE@cdw.prod cm
            WHERE cm.threadid = v_cur_threadid
              AND cm.kind IN (2, 10, 13)
              AND cm.created > v_cur_time;

            IF v_end_time IS NOT NULL THEN
                INSERT INTO ANALYTICS.TOLOG_TMP_STATS_SERVICE_LEVEL (
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

    -- Закрытие курсора
    CLOSE cur;

    -- Коммит изменений (для временной таблицы)
    COMMIT;
END;
/
