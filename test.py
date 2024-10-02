WITH last_call_events AS (
    -- Определяем последний EVENT_TIME для каждого CALL_ID (завершение вызова)
    SELECT 
        CALL_ID,
        NUMBER_,
        MAX(EVENT_TIME) AS end_time
    FROM ods.ods_bpu_int_ivrchd_events@cdw.prod
    WHERE NUMBER_ = '9063705301' -- Здесь можно указать конкретный номер или убрать это условие для всех номеров
    GROUP BY CALL_ID, NUMBER_
),
next_call_times AS (
    -- Определяем начало следующего звонка для каждого клиента
    SELECT 
        t1.CALL_ID AS prev_call_id,
        t1.end_time AS prev_end_time,
        t2.CALL_ID AS next_call_id,
        MIN(t2.end_time) AS next_start_time,
        t1.NUMBER_
    FROM last_call_events t1
    LEFT JOIN last_call_events t2 
        ON t1.NUMBER_ = t2.NUMBER_ 
        AND t1.end_time < t2.end_time -- Следующий вызов должен быть после предыдущего
    GROUP BY t1.CALL_ID, t1.end_time, t1.NUMBER_
)
SELECT 
    NUMBER_, 
    prev_call_id, 
    prev_end_time, 
    next_call_id, 
    next_start_time,
    ROUND((next_start_time - prev_end_time) * 1440) AS diff_minutes, -- Разница во времени в минутах
    CASE 
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 1 THEN '1 минута'
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 2 THEN '2 минуты'
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 5 THEN '5 минут'
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 10 THEN '10 минут'
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 15 THEN '15 минут'
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 20 THEN '20 минут'
        WHEN ROUND((next_start_time - prev_end_time) * 1440) <= 30 THEN '30 минут'
        ELSE 'Более 30 минут или не вернулся'
    END AS return_time_category
FROM next_call_times
ORDER BY prev_end_time;
