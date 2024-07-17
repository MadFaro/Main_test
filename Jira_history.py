WITH chat_data AS (
        SELECT
            cth.threadid,
            cth.departmentid,
            cth.state,
            cth.dtm,
            LAG(cth.threadid) OVER (ORDER BY cth.threadid, cth.number) AS prev_threadid,
            LEAD(cth.state) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS next_state,
            LEAD(cth.dtm) OVER (PARTITION BY cth.threadid ORDER BY cth.number) AS next_dtm
        FROM chatthreadhistory cth
        JOIN chatthread ct ON ct.threadid = cth.threadid
        WHERE ct.offline = 0
          AND cth.dtm BETWEEN p_dtmfrom AND p_dtmto
    ),
    queue_times AS (
        SELECT
            threadid,
            departmentid,
            dtm AS got_into_common_queue_time,
            next_dtm AS end_time,
            next_state
        FROM chat_data
        WHERE state = 'queue'
    ),
    chatting_times AS (
        SELECT
            q.threadid,
            q.departmentid,
            q.got_into_common_queue_time,
            cm.created AS start_chatting_time
        FROM queue_times q
        JOIN chatmessage cm ON q.threadid = cm.threadid
        WHERE q.next_state = 'chatting'
          AND cm.kind IN (2, 10, 13)
          AND cm.created > q.got_into_common_queue_time
          AND cm.created <= q.end_time
    )
