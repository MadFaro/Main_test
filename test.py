SELECT created
INTO v_end_time
FROM (
    SELECT created
    FROM ANALYTICS.TOLOG_CHATMESSAGE
    WHERE threadid = v_cur_threadid
      AND kind IN (2, 10, 13)
      AND created >= v_cur_time
    ORDER BY created
)
WHERE ROWNUM = 1;
