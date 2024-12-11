SELECT 
    t.OPERATORID,
    COUNT(DISTINCT t.THREADID) AS ACTIVE_CHAT_COUNT
FROM your_table t
JOIN (
    -- Определяем последнее событие для каждого чата
    SELECT THREADID, MAX(NUMBER_) AS LAST_NUMBER
    FROM your_table
    GROUP BY THREADID
) le
ON t.THREADID = le.THREADID AND t.NUMBER_ = le.LAST_NUMBER
WHERE t.OPERATORID IS NOT NULL   -- Учитываем только заполненные OPERATORID
  AND t.STATE NOT LIKE '%closed%' -- Чаты, которые не закрыты
GROUP BY t.OPERATORID;

