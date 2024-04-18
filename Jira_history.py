WITH TimeRange AS (
    SELECT 
        TRUNC(MIN(DTM), 'HH24') AS min_time,
        TRUNC(MAX(DTM), 'HH24') AS max_time
    FROM 
        your_table_name
),
TimeSlots AS (
    SELECT 
        min_time + (LEVEL - 1)/24 AS hour_slot
    FROM 
        TimeRange
    CONNECT BY 
        min_time + (LEVEL - 1)/24 <= max_time
)

SELECT 
    TO_CHAR(TimeSlots.hour_slot, 'YYYY-MM-DD HH24:MI') AS hour_slot,
    COUNT(DISTINCT CASE WHEN TimeSlots.hour_slot BETWEEN your_table_name.DTM AND your_table_name.logout_time THEN OPERATORID END) AS operators_count
FROM
    TimeSlots
LEFT JOIN
    your_table_name
ON
    TimeSlots.hour_slot BETWEEN your_table_name.DTM AND NVL(your_table_name.logout_time, SYSDATE)
GROUP BY
    TimeSlots.hour_slot
ORDER BY
    hour_slot;


