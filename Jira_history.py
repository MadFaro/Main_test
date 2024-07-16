WITH tab_2 as (
select trunc(min(sysdate-1)) as min_time, 
trunc(min(sysdate-1)) + interval '24' hour as max_time
from dual),
tab_3 as (
select min_time + (level - 1)/24 as hour_slot
from tab_2
connect by min_time + (level - 1)/24 < max_time),
employee_schedules AS (
    SELECT
        FIO,
        TO_DATE(START_SCHEDULE, 'HH24:MI') AS START_TIME,
        TO_DATE(END_SCHEDULE, 'HH24:MI') AS END_TIME,
        DATE_SCHEDULE
    FROM ANALYTICS.TOLOG_OPERATORS_SCHEDULE
    where DATE_SCHEDULE >= trunc(sysdate-1)
)
SELECT
    sh.hour_slot,
    COUNT(es.FIO) AS EMPLOYEE_COUNT
FROM
    tab_3 sh
LEFT JOIN employee_schedules es
    ON sh.hour_slot BETWEEN es.DATE_SCHEDULE + (EXTRACT(HOUR FROM es.START_TIME) / 24) 
    AND es.DATE_SCHEDULE + (EXTRACT(HOUR FROM es.END_TIME) / 24)
GROUP BY
    sh.hour_slot
ORDER BY
    sh.hour_slot;

    ORA-30076: неверное поле выборки для источника выборки
30076. 00000 -  "invalid extract field for extract source"
*Cause:    The extract source does not contain the specified extract field.
*Action:
Error at Line: 24 Column: 67

