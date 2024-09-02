SELECT 
    TRUNC(CREATED, 'mm') AS created, 
    SUM(CASE WHEN FCR = 1 THEN 1 ELSE 0 END) / COUNT(*) AS fcr 
FROM (
    SELECT 
        a.OPERATORFULLNAME, 
        a.OPERATORID, 
        a.CREATED,
        a.VISITORID,
        CASE 
            WHEN COUNT(*) OVER (
                PARTITION BY a.VISITORID 
                ORDER BY a.CREATED 
                RANGE BETWEEN INTERVAL '0' DAY PRECEDING AND INTERVAL '2' DAY FOLLOWING
            ) = 1 
            THEN 1 
            ELSE 0 
        END AS FCR
    FROM 
        ODS.ODS_WIS_CHATTHREAD@cdw.prod a
    WHERE 
        a.CREATED >= DATE '2023-12-01'
        AND a.THREADID IN (
            SELECT DISTINCT THREADID 
            FROM ODS.ODS_WIS_chatthreadhistory@cdw.prod
            WHERE DTM >= DATE '2023-12-01' 
            AND DEPARTMENTID IN (22)
        )
)
GROUP BY 
    TRUNC(CREATED, 'mm')
ORDER BY 
    TRUNC(CREATED, 'mm');
