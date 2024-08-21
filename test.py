SELECT trunc(DT, 'mm') AS created, 
       SUM(CASE WHEN FCR = 1 THEN 1 ELSE 0 END) / COUNT(*) AS fcr
FROM (
    SELECT 
        a.call_id, 
        a.OPERATOR, 
        a.DT, 
        a.CLIENT_ID,
        COUNT(DISTINCT a.OPERATOR) OVER (PARTITION BY a.call_id) AS operator_count,
        COUNT(TRUNC(DT)) OVER (PARTITION BY TRUNC(DT), a.CLIENT_ID) AS FCR
    FROM 
        ANALYTICS.KDI_SIEBEL_PAST a
    WHERE 
        a.DT >= DATE '2024-01-01' 
        AND a.CLIENT_ID IS NOT NULL 
        AND a.TYPE = 'Вызов - входящий' 
        AND a.DIRECTION = 'ДДО'
) 
WHERE operator_count = 1 -- Исключаем звонки с переводом на другого оператора
GROUP BY trunc(DT, 'mm')
ORDER BY trunc(DT, 'mm');
