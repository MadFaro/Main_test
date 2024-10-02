WITH ranked_calls AS (
    -- Определяем момент начала и завершения для каждого вызова
    SELECT 
        CALL_ID,
        NUMBER_,
        EVENT_TIME,
        START_EVENT_TIME,
        ROW_NUMBER() OVER (PARTITION BY NUMBER_ ORDER BY EVENT_TIME) AS call_rank
    FROM ods.ods_bpu_int_ivrchd_events@cdw.prod
    WHERE NUMBER_ = '9063705301' -- Номер клиента
),
call_durations AS (
    -- Находим момент завершения предыдущего вызова и начала следующего
    SELECT 
        t1.CALL_ID AS prev_call_id,
        t1.EVENT_TIME AS prev_end_time,
        t2.CALL_ID AS next_call_id,
        t2.EVENT_TIME AS next_start_time,
        t1.NUMBER_
    FROM ranked_calls t1
    LEFT JOIN ranked_calls t2 ON t1.call_rank = t2.call_rank - 1
        AND t1.NUMBER_ = t2.NUMBER_
)
SELECT 
    NUMBER_, 
    prev_call_id, 
    prev_end_time, 
    next_call_id, 
    next_start_time,
    ROUND((next_start_time - prev_end_time) * 1440) AS diff_minutes -- Разница во времени в минутах
FROM call_durations
WHERE next_start_time IS NOT NULL
ORDER BY prev_end_time;

