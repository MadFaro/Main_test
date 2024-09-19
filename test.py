with tab_1 as (select 
PRODUCTNAME AS type, 
TRUNC(ENTERED_AT_MSK, 'HH24') + (FLOOR((TO_NUMBER(TO_CHAR(ENTERED_AT_MSK, 'MI')) / 30)) * (1/48)) AS request_date
from ANALYTICS.TOLOG_TEMP_DEL)
SELECT 
    TO_CHAR(request_date, 'D') AS day_of_week,                 -- День недели (1 - воскресенье, 7 - суббота)
    TO_CHAR(TRUNC(request_date, 'HH24') + 
            (FLOOR((TO_CHAR(request_date, 'MI') / 30)) * (30/1440)), 
            'HH24:MI') AS time_interval,                      -- 30-минутные интервалы
    COUNT(*) AS total_requests,                               -- Количество заявок в этом интервале
    ROUND(COUNT(*) / COUNT(DISTINCT TRUNC(request_date)), 2) AS avg_per_interval -- Среднее по дням
FROM 
    tab_1
GROUP BY 
    TO_CHAR(request_date, 'D'), 
    TRUNC(request_date, 'HH24') + 
    (FLOOR((TO_CHAR(request_date, 'MI') / 30)) * (30/1440))  -- Группировка по 30-минутным интервалам
ORDER BY 
    TO_CHAR(request_date, 'D'), 
    time_interval;
