    WITH cte_thread_history AS (
        SELECT 
            cth.threadid, 
            cth.departmentid, 
            cth.state, 
            cth.dtm,
            LAG(cth.state) OVER (PARTITION BY cth.threadid ORDER BY cth.dtm) AS prev_state,
            LEAD(cth.state) OVER (PARTITION BY cth.threadid ORDER BY cth.dtm) AS next_state,
            LEAD(cth.dtm) OVER (PARTITION BY cth.threadid ORDER BY cth.dtm) AS next_dtm
        FROM 
            ANALYTICS.TOLOG_CHATTHREADHISTORY cth
        JOIN 
            ANALYTICS.TOLOG_CHATTHREAD ct ON ct.threadid = cth.threadid
        WHERE 
            ct.created BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
            AND ct.offline_ = 0
            AND cth.dtm BETWEEN TRUNC(SYSDATE - 1) AND TRUNC(SYSDATE)
    ),
    cte_chat_messages AS (
        SELECT 
            cm.threadid,
            MIN(cm.created) AS min_created
        FROM 
            ANALYTICS.TOLOG_CHATMESSAGE cm
        WHERE 
            cm.kind IN (2, 10, 13)
        GROUP BY 
            cm.threadid
    )
    -- Вставляем данные в целевую таблицу
    INSERT INTO ANALYTICS.TOLOG_TMP_STATS_SERVICE_LEVEL (
        threadid, 
        department_id, 
        got_into_common_queue_time, 
        start_chatting_time
    )
    SELECT 
        th.threadid, 
        th.departmentid, 
        th.dtm AS got_into_common_queue_time, 
        cm.min_created AS start_chatting_time
    FROM 
        cte_thread_history th
    JOIN 
        cte_chat_messages cm ON th.threadid = cm.threadid
    WHERE 
        th.state = 'queue'
        AND th.next_state = 'chatting'
        AND th.dtm < cm.min_created
        AND (th.prev_state IS NULL OR th.prev_state <> th.state)
    ORDER BY 
        th.threadid, th.dtm;
