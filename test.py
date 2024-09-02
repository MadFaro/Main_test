WITH FirstContacts AS (
    SELECT 
        a.VISITORID,
        MIN(a.CREATED) AS FirstContactDate
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
    GROUP BY 
        a.VISITORID
),
RepeatedContacts AS (
    SELECT 
        fc.VISITORID,
        COUNT(*) AS RepeatCount
    FROM 
        ODS.ODS_WIS_CHATTHREAD@cdw.prod a
    JOIN 
        FirstContacts fc ON a.VISITORID = fc.VISITORID
    WHERE 
        a.CREATED BETWEEN fc.FirstContactDate AND fc.FirstContactDate + INTERVAL '3' DAY
        AND a.CREATED > fc.FirstContactDate
    GROUP BY 
        fc.VISITORID
)
SELECT 
    TRUNC(fc.FirstContactDate, 'mm') AS created,
    SUM(CASE WHEN rc.RepeatCount IS NULL THEN 1 ELSE 0 END) / COUNT(*) AS fcr
FROM 
    FirstContacts fc
LEFT JOIN 
    RepeatedContacts rc ON fc.VISITORID = rc.VISITORID
GROUP BY 
    TRUNC(fc.FirstContactDate, 'mm')
ORDER BY 
    created;
