WITH tab_1 AS (
    SELECT 
        call_id, 
        number_, 
        VARIABLE_7, 
        MAX(event_time) AS end_time
    FROM ods.ods_bpu_int_ivrchd_events@cdw.prod
    WHERE 
        START_EVENT_TIME >= DATE '2025-03-01' 
        AND VARIABLE_7 IS NOT NULL 
        AND AGENT_ID IS NULL
    GROUP BY call_id, number_, VARIABLE_7
)
SELECT 
    t1.call_id AS prev_call_id, 
    t1.number_, 
    t1.end_time AS prev_end_time,
    MIN(t2.START_EVENT_TIME) AS next_start_time, -- находим первый повторный звонок
    MIN(CASE WHEN t2.AGENT_ID IS NOT NULL THEN t2.START_EVENT_TIME END) AS connected_time -- фиксируем момент дозвона
FROM tab_1 t1
JOIN ods.ods_bpu_int_ivrchd_events@cdw.prod t2 
    ON t1.number_ = t2.number_ 
    AND t2.START_EVENT_TIME > t1.end_time  -- только последующие звонки
WHERE t2.START_EVENT_TIME >= DATE '2025-03-01' 
GROUP BY t1.call_id, t1.number_, t1.end_time
ORDER BY t1.number_, t1.end_time;
