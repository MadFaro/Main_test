
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav  


CREATE OR REPLACE PROCEDURE tolog_temp_chst_sl
(
    p_dtmfrom IN TIMESTAMP,
    p_dtmto IN TIMESTAMP,
    p_departmentid IN NUMBER,
    p_locale IN VARCHAR2
)
IS
BEGIN
    INSERT INTO ANALYTICS.TMP_STATS_SERVICE_LEVEL (threadid, department_id, got_into_common_queue_time, start_chatting_time)
    SELECT 
        threadid,
        departmentid,
        MIN(CASE WHEN state = 'queue' THEN dtm END) OVER (PARTITION BY threadid, departmentid) AS got_into_common_queue_time,
        MIN(CASE WHEN state = 'chatting' THEN dtm END) OVER (PARTITION BY threadid, departmentid) AS start_chatting_time
    FROM (
        SELECT 
            cth.threadid, 
            cth.departmentid, 
            cth.state, 
            cth.dtm,
            ROW_NUMBER() OVER (PARTITION BY cth.threadid ORDER BY cth.number_) AS rn
        FROM 
            ODS.ODS_WIS_CHATTHREADHISTORY@cdw.prod cth
        JOIN 
            ODS.ODS_WIS_CHATTHREAD@cdw.prod ct ON ct.threadid = cth.threadid
        WHERE 
            ct.OFFLINE_ = 0
            AND cth.dtm BETWEEN TRUNC(SYSDATE-1) AND TRUNC(SYSDATE)
    ) 
    WHERE rn = 1
    AND state IN ('queue', 'chatting')
    AND (
        state = 'chatting' 
        OR NOT EXISTS (
            SELECT 1 
            FROM ODS.ODS_WIS_CHATTHREADHISTORY@cdw.prod cth2 
            WHERE cth2.threadid = cth.threadid 
            AND cth2.state IN ('chatting_with_robot', 'closed_by_operator')
            AND cth2.dtm > cth.dtm
        )
    );
END;
