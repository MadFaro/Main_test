SELECT
    TO_CHAR(entry_time, 'YYYY-MM-DD HH24') AS hour_slot,
    COUNT(DISTINCT operator_id) AS operators_count
FROM
    your_table_name
CONNECT BY
    LEVEL <= (SELECT MAX((logout_time - entry_time) * 24) FROM your_table_name)
START WITH
    TRUNC(entry_time, 'HH24') = TRUNC(SYSDATE, 'HH24')
GROUP BY
    TO_CHAR(entry_time, 'YYYY-MM-DD HH24')
ORDER BY
    hour_slot;

