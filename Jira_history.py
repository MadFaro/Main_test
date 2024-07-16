WITH tab_2 AS (
    SELECT trunc(min(sysdate-1)) AS min_time, 
           trunc(min(sysdate-1)) + interval '24' hour AS max_time
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
        TO_DATE(START_SCHEDULE, 'HH24:MI') AS START_TIME,
        TO_DATE(END_SCHEDULE, 'HH24:MI') AS END_TIME,
        DATE_SCHEDULE
    FROM ANALYTICS.TOLOG_OPERATORS_SCHEDULE
    WHERE DATE_SCHEDULE >= trunc(sysdate-1)
)
SELECT
    sh.hour_slot,
    COUNT(es.FIO) AS EMPLOYEE_COUNT
FROM
    tab_3 sh
LEFT JOIN employee_schedules es
    ON sh.hour_slot BETWEEN es.DATE_SCHEDULE + (TO_NUMBER(TO_CHAR(es.START_TIME, 'HH24')) / 24) 
    AND es.DATE_SCHEDULE + (TO_NUMBER(TO_CHAR(es.END_TIME, 'HH24')) / 24)
GROUP BY
    sh.hour_slot
ORDER BY
    sh.hour_slot;
