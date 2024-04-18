SELECT 
    TO_CHAR(h.hour_slot, 'YYYY-MM-DD HH24:MI') AS hour_slot,
    COUNT(DISTINCT operatorfullname) AS operators_count
FROM
    (SELECT TRUNC(dtm, 'HH24') + (LEVEL - 1)/24 AS hour_slot
     FROM dual
     CONNECT BY TRUNC(dtm, 'HH24') + (LEVEL - 1)/24 < TRUNC(SYSDATE) + 1) h
LEFT JOIN
    (SELECT operatorfullname,
            TRUNC(dtm, 'HH24') + (LEVEL - 1)/24 AS hour_slot
     FROM your_table_name
     WHERE actiontype = 'login'
     CONNECT BY PRIOR operatorfullname = operatorfullname
                AND PRIOR TRUNC(dtm, 'HH24') + (LEVEL - 1)/24 < TRUNC(dtm, 'HH24') + 1) logins
ON
    h.hour_slot = logins.hour_slot
GROUP BY
    TO_CHAR(h.hour_slot, 'YYYY-MM-DD HH24:MI')
ORDER BY
    hour_slot;
