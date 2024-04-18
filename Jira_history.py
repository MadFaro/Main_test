WITH HourSequence AS (
  SELECT TRUNC(SYSDATE, 'HH24') + (LEVEL - 1)/24 AS hour_slot
  FROM dual
  CONNECT BY LEVEL <= 24
)

SELECT 
    TO_CHAR(HourSequence.hour_slot, 'YYYY-MM-DD HH24:MI') AS hour_slot,
    COUNT(DISTINCT operatorfullname) AS operators_count
FROM
    HourSequence
LEFT JOIN
    your_table_name
ON
    HourSequence.hour_slot BETWEEN your_table_name.entry_time AND NVL(your_table_name.logout_time, SYSDATE)
    AND your_table_name.actiontype = 'login'
GROUP BY
    HourSequence.hour_slot
ORDER BY
    hour_slot;
