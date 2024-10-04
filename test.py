WITH tab_1 AS (
    SELECT 
        PRODUCTNAME AS type,                                  -- Продукт
        TRUNC(ENTERED_AT_MSK, 'HH24') + (FLOOR((TO_NUMBER(TO_CHAR(ENTERED_AT_MSK, 'MI')) / 30)) * (1/48)) AS request_date,
        TO_CHAR(ENTERED_AT_MSK, 'MM.YYYY') AS month           -- Месяц и год
    FROM ANALYTICS.TOLOG_TEMP_DEL
)
SELECT 
    type,                                                    -- Продукт
    month,                                                   -- Месяц и год (формат MM.YYYY)
    TO_CHAR(request_date, 'D') AS day_of_week,               -- День недели (1 - воскресенье, 7 - суббота)
    TO_CHAR(request_date, 'HH24:MI') AS time_interval,       -- 30-минутные интервалы
    COUNT(*) AS total_requests,                              -- Количество заявок в этом интервале
    ROUND(COUNT(*) / COUNT(DISTINCT TRUNC(request_date)), 2) AS avg_per_interval -- Среднее по дням
FROM 
    tab_1
GROUP BY 
    type,                                                    -- Группировка по продукту
    month, 
    TO_CHAR(request_date, 'D'), 
    TO_CHAR(request_date, 'HH24:MI')                         -- Группировка по 30-минутным интервалам
ORDER BY 
    type,                                                    -- Сортировка по продукту
    month, 
    TO_CHAR(request_date, 'D'), 
    time_interval;

