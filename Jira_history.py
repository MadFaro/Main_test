WITH chat_data AS (
        SELECT
            cth.threadid,
            cth.departmentid,
            cth.state,
            cth.dtm,
            LEAD(cth.state) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS next_state,
            LEAD(cth.dtm) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS next_dtm
        FROM chatthreadhistory cth
        JOIN chatthread ct ON ct.threadid = cth.threadid
        WHERE ct.offline = 0
          AND cth.dtm BETWEEN p_dtmfrom AND p_dtmto
    ),
    filtered_chat_data AS (
        SELECT
            threadid,
            departmentid,
            dtm,
            next_dtm,
            state,
            next_state
        FROM chat_data
        WHERE state IN ('queue', 'chatting_with_robot', 'closed_by_operator', 'chatting')
    ),
    queue_to_chat AS (
        SELECT
            fcd.threadid,
            fcd.departmentid,
            fcd.dtm AS got_into_common_queue_time,
            cm.created AS start_chatting_time
        FROM filtered_chat_data fcd
        JOIN chatmessage cm ON fcd.threadid = cm.threadid
        WHERE fcd.state = 'queue'
          AND fcd.next_state = 'chatting'
          AND cm.kind IN (2, 10, 13)
          AND cm.created > fcd.dtm
    )
    SELECT
        threadid,
        department_id,
        MIN(got_into_common_queue_time) AS got_into_common_queue_time,
        MIN(start_chatting_time) AS start_chatting_time
    FROM queue_to_chat
    GROUP BY threadid, department_id;
/
