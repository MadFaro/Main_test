WITH tab_2 AS (
    SELECT trunc(min(DTM)) AS min_time, 
           trunc(min(DTM)) + interval '24' hour AS max_time
    FROM dual
),
tab_3 AS (
    SELECT min_time + (LEVEL - 1)/24 AS hour_slot
    FROM tab_2
    CONNECT BY min_time + (LEVEL - 1)/24 < max_time
),
employee_schedules AS (
    SELECT
        FIO,
        TO_DATE(SUBSTR(SCHEDULE, 1, 5), 'HH24:MI') AS START_TIME,
        TO_DATE(SUBSTR(SCHEDULE, 7, 5), 'HH24:MI') AS END_TIME,
        DTM
    FROM your_table
    WHERE DTM >= trunc(sysdate-1)
)
SELECT
    sh.hour_slot,
    COUNT(es.FIO) AS EMPLOYEE_COUNT
FROM
    tab_3 sh
LEFT JOIN employee_schedules es
    ON sh.hour_slot BETWEEN es.DTM + (TO_NUMBER(TO_CHAR(es.START_TIME, 'HH24')) / 24) 
    AND es.DTM + (TO_NUMBER(TO_CHAR(es.END_TIME, 'HH24')) / 24)
GROUP BY
    sh.hour_slot
ORDER BY
    sh.hour_slot;
