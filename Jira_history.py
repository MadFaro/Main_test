WITH TimeSlots AS (
    SELECT 
        TRUNC(MIN(DTM), 'HH24') AS min_time,
        TRUNC(MAX(DTM), 'HH24') AS max_time
    FROM 
        your_table_name
),
HourlyLogins AS (
    SELECT 
        TRUNC(DTM, 'HH24') AS login_hour,
        OPERATORID,
        LEAD(TRUNC(DTM, 'HH24')) OVER (PARTITION BY OPERATORID ORDER BY DTM) AS next_login_hour
    FROM 
        your_table_name
    WHERE 
        ACTIONTYPE = 'login'
),
TimeRange AS (
    SELECT 
        min_time + (LEVEL - 1)/24 AS hour_slot
    FROM 
        TimeSlots
    CONNECT BY 
        min_time + (LEVEL - 1)/24 <= max_time
)

SELECT 
    TO_CHAR(TimeRange.hour_slot, 'YYYY-MM-DD HH24:MI') AS hour_slot,
    COUNT(DISTINCT CASE 
                        WHEN TimeRange.hour_slot >= HourlyLogins.login_hour AND 
                             (TimeRange.hour_slot < HourlyLogins.next_login_hour OR HourlyLogins.next_login_hour IS NULL)
                        THEN HourlyLogins.OPERATORID
                    END) AS operators_count
FROM
    TimeRange
LEFT JOIN
    HourlyLogins
ON
    TimeRange.hour_slot >= HourlyLogins.login_hour AND 
    (TimeRange.hour_slot < HourlyLogins.next_login_hour OR HourlyLogins.next_login_hour IS NULL)
GROUP BY
    TimeRange.hour_slot
ORDER BY
    hour_slot;

