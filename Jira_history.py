WITH chat_data AS (
        SELECT
            cth.threadid,
            cth.departmentid,
            cth.state,
            cth.dtm,
            LAG(cth.threadid) OVER (ORDER BY cth.threadid, cth.number) AS prev_threadid,
            LAG(cth.state) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS prev_state,
            LAG(cth.dtm) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS prev_dtm,
            LEAD(cth.state) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS next_state,
            LEAD(cth.dtm) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS next_dtm
        FROM chatthreadhistory cth
        JOIN chatthread ct ON ct.threadid = cth.threadid
        WHERE ct.offline = 0
          AND cth.dtm BETWEEN p_dtmfrom AND p_dtmto
    ),
    queue_times AS (
        SELECT
            cd.threadid,
            cd.departmentid,
            cd.dtm AS got_into_common_queue_time,
            CASE
                WHEN cd.next_state = 'chatting' THEN (
                    SELECT MIN(cm.created)
                    FROM chatmessage cm
                    WHERE cm.threadid = cd.threadid
                      AND cm.kind IN (2, 10, 13)
                      AND cm.created > cd.dtm
                )
                ELSE NULL
            END AS start_chatting_time
        FROM chat_data cd
        WHERE cd.state = 'queue'
    )
    SELECT
        qt.threadid,
        qt.departmentid,
        qt.got_into_common_queue_time,
        qt.start_chatting_time
    FROM queue_times qt
    WHERE qt.start_chatting_time IS NOT NULL;
/

