create or replace procedure tolog_test (
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
        FROM ANALYTICS.TOLOG_CHATTHREADHISTORY cth
        JOIN ANALYTICS.TOLOG_CHATTHREAD ct ON ct.threadid = cth.threadid
        WHERE ct.created BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
          AND ct.offline_ = 0
          AND cth.dtm BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
        ORDER BY cth.threadid, cth.dtm;
begin
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
            FROM ANALYTICS.TOLOG_CHATMESSAGE cm
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
CLOSE cur;
COMMIT;
end;



CREATE PROCEDURE p_service_level (IN p_dtmfrom datetime, IN p_dtmto datetime, IN p_departmentid int(11), IN p_locale char(2))
BEGIN
    DECLARE v_cur_threadid INT;
    DECLARE v_prev_threadid INT;
    DECLARE v_cur_department_id INT;
    DECLARE v_cur_state VARCHAR(128);
    DECLARE v_cur_time DATETIME;
    DECLARE v_start_time DATETIME DEFAULT 0;
    DECLARE v_end_time DATETIME DEFAULT 0;
    DECLARE l_done INT DEFAULT 0;
    DECLARE cur CURSOR FOR
        SELECT cth.threadid, cth.departmentid, cth.state, dtm FROM chatthreadhistory cth
        JOIN chatthread ct ON ct.threadid = cth.threadid
        WHERE ct.offline = 0
        AND dtm BETWEEN p_dtmfrom AND p_dtmto
        ORDER BY cth.threadid, cth.number;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET l_done = 1;

    CREATE TABLE IF NOT EXISTS tmp_stats_service_level
    (
        id INT AUTO_INCREMENT,
        threadid  INT NOT NULL,
        department_id INT,
        got_into_common_queue_time DATETIME NOT NULL,
        start_chatting_time DATETIME NOT NULL,
        PRIMARY KEY(id)
    ) ENGINE = MEMORY;

    TRUNCATE tmp_stats_service_level;

    OPEN cur;
    lbl:
    LOOP
        FETCH cur INTO v_cur_threadid, v_cur_department_id, v_cur_state, v_cur_time;
        IF l_done = 1 THEN
            LEAVE lbl;
        END IF;
IF v_prev_threadid <> v_cur_threadid THEN
            SET v_start_time = 0;
            SET v_end_time = 0;
        END IF;

        IF v_cur_state IN ('chatting_with_robot', 'closed_by_operator', 'on_hold') THEN
            SET v_start_time = 0;
            SET v_end_time = 0;
        END IF;

        IF v_cur_state IN ('queue') AND v_start_time = 0 THEN
            SET v_start_time = v_cur_time;
        END IF;

        IF v_cur_state IN ('chatting') AND v_start_time <> 0 THEN
            SET v_end_time = (
                SELECT created
                FROM chatmessage
                WHERE threadid = v_cur_threadid
                  AND kind in (2, 10, 13)
                  AND created > v_cur_time
                ORDER BY created
                LIMIT 1
            );
        END IF;

        IF v_start_time <> 0 AND v_end_time <> 0 THEN
            INSERT INTO tmp_stats_service_level (
                threadid,
                department_id,
                got_into_common_queue_time,
                start_chatting_time
            ) VALUES (
                v_cur_threadid,
                v_cur_department_id,
                v_start_time,
                v_end_time
            );
            SET v_start_time = 0;
            SET v_end_time = 0;
        END IF;
        SET v_prev_threadid = v_cur_threadid;
    END LOOP;
    CLOSE cur;
END

