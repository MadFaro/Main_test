SELECT 
    TO_CHAR(h.hour_slot, 'YYYY-MM-DD HH24:MI') AS hour_slot,
    COUNT(DISTINCT operator_id) AS operators_count
FROM
    (SELECT TRUNC(entry_time, 'HH24') + (LEVEL - 1)/24 AS hour_slot
     FROM dual
     CONNECT BY TRUNC(entry_time, 'HH24') + (LEVEL - 1)/24 < TRUNC(SYSDATE) + 1) h
LEFT JOIN
    (SELECT operator_id,
            TRUNC(entry_time, 'HH24') + (LEVEL - 1)/24 AS hour_slot
     FROM your_table_name
     WHERE status = 'login'
     CONNECT BY PRIOR operator_id = operator_id
                AND PRIOR TRUNC(logout_time, 'HH24') + (LEVEL - 1)/24 < TRUNC(logout_time, 'HH24') + 1) logins
ON
    h.hour_slot = logins.hour_slot
GROUP BY
    TO_CHAR(h.hour_slot, 'YYYY-MM-DD HH24:MI')
ORDER BY
    hour_slot;
