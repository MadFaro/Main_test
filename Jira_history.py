
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav  


CREATE PROCEDURE `p_service_level` (IN p_dtmfrom datetime, IN p_dtmto datetime, IN p_departmentid int(11), IN p_locale char(2))
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

        # Сбрасываем для каждого нового треда
        IF v_prev_threadid <> v_cur_threadid THEN
            SET v_start_time = 0;
            SET v_end_time = 0;
        END IF;

        # Если сначала чат попал на бота, то учитываем время попадания в очередь после бота.
        # Не учитываем диалог, если он не был в состоянии chatting и был закрыт оператором.
        IF v_cur_state IN ('chatting_with_robot', 'closed_by_operator') THEN
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
