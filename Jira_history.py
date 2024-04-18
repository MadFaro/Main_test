WITH TimeRange AS (
    SELECT 
        TRUNC(MIN(DTM), 'HH24') AS min_time,
        TRUNC(MAX(DTM) + 1/24, 'HH24') AS max_time -- Увеличиваем конечное время на 1 час, чтобы включить последний час
    FROM 
        your_table_name
),
HourlyLogins AS (
    SELECT 
        TRUNC(DTM, 'HH24') AS login_hour,
        OPERATORID,
        LEAD(TRUNC(DTM, 'HH24')) OVER (PARTITION BY OPERATORID ORDER BY DTM) AS next_login_hour,
        CASE 
            WHEN ACTIONTYPE = 'login' THEN LEAD(TRUNC(DTM, 'HH24')) OVER (PARTITION BY OPERATORID ORDER BY DTM)
            ELSE DTM + 1/24 -- Если действие logout, просто устанавливаем следующий час
        END AS logout_hour
    FROM 
        your_table_name
),
TimeSlots AS (
    SELECT 
        min_time + (LEVEL - 1)/24 AS hour_slot
    FROM 
        TimeRange
    CONNECT BY 
        min_time + (LEVEL - 1)/24 < max_time -- Используем < вместо <=
)

SELECT 
    TO_CHAR(TimeSlots.hour_slot, 'YYYY-MM-DD HH24:MI') AS hour_slot,
    COUNT(DISTINCT CASE 
                        WHEN TimeSlots.hour_slot >= HourlyLogins.login_hour AND 
                             TimeSlots.hour_slot < HourlyLogins.logout_hour
                        THEN HourlyLogins.OPERATORID
                    END) AS operators_count
FROM
    TimeSlots
LEFT JOIN
    HourlyLogins
ON
    TimeSlots.hour_slot >= HourlyLogins.login_hour AND 
    TimeSlots.hour_slot < HourlyLogins.next_login_hour
GROUP BY
    TimeSlots.hour_slot
ORDER BY
    hour_slot;
