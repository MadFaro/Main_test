
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav  


create or replace PROCEDURE                                                   tolog_temp_chst_sl
(
    p_dtmfrom IN TIMESTAMP,
    p_dtmto IN TIMESTAMP,
    p_departmentid IN INT,
    p_locale IN VARCHAR2
)
IS
    v_cur_threadid INT;
    v_prev_threadid INT;
    v_cur_department_id INT;
    v_cur_state VARCHAR2(128);
    v_cur_time TIMESTAMP;
    v_start_time TIMESTAMP := NULL;
    v_end_time TIMESTAMP := NULL;
    l_done INT := 0;
    CURSOR cur IS
        SELECT cth.threadid, cth.departmentid, cth.state, dtm FROM ODS.ODS_WIS_chatthreadhistory@cdw.prod cth
        JOIN ODS.ODS_WIS_chatthread@cdw.prod ct ON ct.threadid = cth.threadid
        WHERE ct.offline = 0
        AND dtm BETWEEN trunc(sysdate-1) AND trunc(sysdate)
        ORDER BY cth.threadid, cth.number_;
BEGIN
    FOR cur_rec IN cur LOOP
        v_cur_threadid := cur_rec.threadid;
        v_cur_department_id := cur_rec.departmentid;
        v_cur_state := cur_rec.state;
        v_cur_time := cur_rec.dtm;
        IF v_prev_threadid <> v_cur_threadid THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        IF v_cur_state IN ('chatting_with_robot', 'closed_by_operator') THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        IF v_cur_state = 'queue' AND v_start_time IS NULL THEN
            v_start_time := v_cur_time;
        END IF;

        IF v_cur_state = 'chatting' AND v_start_time IS NOT NULL THEN
            SELECT MIN(created) INTO v_end_time
            FROM ODS.ODS_WIS_CHATMESSAGE@cdw.prod
            WHERE threadid = v_cur_threadid
              AND kind IN (2, 10, 13)
              AND created > v_cur_time;
        END IF;

        IF v_start_time IS NOT NULL AND v_end_time IS NOT NULL THEN
            INSERT INTO ANALYTICS.TMP_STATS_SERVICE_LEVEL (
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
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        v_prev_threadid := v_cur_threadid;
    END LOOP;
END;
