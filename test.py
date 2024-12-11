WITH OperatorDepartments AS (
    SELECT 
        a.OPERATORID,
        b.FULLNAME, 
        CASE 
            WHEN a.DEPARTMENTID IN (16, 21, 26, 28) THEN 'mass'
            WHEN a.DEPARTMENTID = 22 THEN 'vip'
            WHEN a.DEPARTMENTID = 31 THEN '2line'
            WHEN a.DEPARTMENTID = 23 THEN 'reten'
            ELSE 'ckk' 
        END AS DEPARTMENT,
        ROW_NUMBER() OVER (PARTITION BY a.OPERATORID ORDER BY 
            CASE 
                WHEN a.DEPARTMENTID IN (16, 21, 26, 28) THEN 1
                WHEN a.DEPARTMENTID = 22 THEN 2
                WHEN a.DEPARTMENTID = 31 THEN 3
                WHEN a.DEPARTMENTID = 23 THEN 4
                ELSE 5 
            END) AS RN
    FROM ODS.ODS_WIS_CHATOPERATORDEPARTMENT@cdw.prod a
    LEFT JOIN ODS.ODS_WIH_CHATOPERATOR@cdw.prod b 
        ON a.OPERATORID = b.OPERATORID
    WHERE a.DEPARTMENTID IN (16, 21, 22, 23, 26, 28, 31, 34)
)
SELECT OPERATORID, FULLNAME, DEPARTMENT
FROM OperatorDepartments
WHERE RN = 1;
