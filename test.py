TO_CHAR(TO_DATE('00:00:00', 'HH24:MI:SS') + NUMTODSINTERVAL(SUM(det."Duration"), 'SECOND'),'HH24:MI:SS') AS formatted_time
