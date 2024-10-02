WITH last_call_events AS (
    -- Определяем последнее событие (по времени) для каждого вызова (это завершение вызова)
    SELECT 
        CALL_ID,
        NUMBER_,
        MAX(EVENT_TIME) AS end_time -- Завершаем вызов (последнее событие)
    FROM ods.ods_bpu_int_ivrchd_events@cdw.prod
    WHERE NUMBER_ = '9063705301' -- Номер клиента (можно убрать это условие для всех номеров)
    GROUP BY CALL_ID, NUMBER_
),
next_call_times AS (
    -- Используем оконную функцию для поиска следующего вызова того же клиента
    SELECT 
        CALL_ID AS prev_call_id,
        NUMBER_,
        end_time AS prev_end_time,
        LEAD(end_time) OVER (PARTITION BY NUMBER_ ORDER BY end_time) AS next_start_time -- Следующее событие (окном)
    FROM last_call_events
)
SELECT 
    NUMBER_, 
    prev_call_id, 
    prev_end_time, 
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
