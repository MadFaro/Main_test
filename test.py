CREATE TABLE analytics.tolog_ivr_event AS
WITH tab_1 AS (
    SELECT 
        TRUNC(event_time) AS event_date,
        event_type_id,
        event_time,
        FIRST_VALUE(event_time) OVER (PARTITION BY call_id ORDER BY rank) AS session_start_time
    FROM ods.ods_bpu_int_ivrchd_events@cdw.prod
),
tab_2 AS (
    SELECT 
        event_date,
        event_type_id,
        SUM(
            CASE 
                WHEN session_start_time IS NOT NULL THEN (event_time - session_start_time) * 24 * 60 * 60
                ELSE 0 
            END
        ) AS total_time_spent,
        COUNT(*) AS event_count
    FROM tab_1
    GROUP BY event_date, event_type_id
),
tab_3 AS (
    SELECT 
        TRUNC(event_time) AS event_date,
        event_type_id,
        COUNT(DISTINCT call_id) AS call_count
    FROM ods.ods_bpu_int_ivrchd_events@cdw.prod
    GROUP BY TRUNC(event_time), event_type_id
),
tab_4 AS (
    SELECT 
        event_date,
        event_type_id,
        total_time_spent / event_count AS avg_time_spent
    FROM tab_2
)
SELECT 
    a.event_date, 
    a.event_type_id,
    a.call_count, 
    b.total_time_spent, 
    d.avg_time_spent
FROM tab_3 a
LEFT JOIN tab_2 b ON a.event_date = b.event_date AND a.event_type_id = b.event_type_id
LEFT JOIN tab_4 d ON a.event_date = d.event_date AND a.event_type_id = d.event_type_id
ORDER BY a.event_date, a.event_type_id;
