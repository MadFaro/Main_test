WITH ranked_data AS (
    SELECT 
        trunc(DT, 'mm') AS DT, 
        TABEL, 
        DIRECTION, 
        PODRAZDELENIE, 
        OPERATOR,  
        SUBJ1, 
        PRODUCT1, 
        REZ1, 
        count(distinct CALL_ID) AS cnt,
        ROW_NUMBER() OVER (PARTITION BY trunc(DT, 'mm'), OPERATOR 
                           ORDER BY count(distinct CALL_ID) DESC) AS rn
    FROM 
        ANALYTICS.KDI_SIEBEL_PAST
    WHERE 
        DT >= DATE '2024-01-01' 
        AND TYPE = 'Вызов - входящий'
    GROUP BY 
        trunc(DT, 'mm'), TABEL, DIRECTION, PODRAZDELENIE, OPERATOR, SUBJ1, PRODUCT1, REZ1
)
SELECT 
    DT, 
    TABEL, 
    DIRECTION, 
    PODRAZDELENIE, 
    OPERATOR,  
    SUBJ1, 
    PRODUCT1, 
    REZ1, 
    cnt
FROM 
    ranked_data
WHERE 
    rn <= 5
ORDER BY 
    DT, 
    OPERATOR, 
    rn;
