SELECT a.*,
       CASE 
           WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 8 
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 20 
           THEN DATE_BEGIN_CRIF
           
           WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 8 
           THEN TRUNC(DATE_BEGIN_CRIF) + 8/24
           
           WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 20 
           THEN TRUNC(DATE_BEGIN_CRIF) + 1 + 8/24
           
           WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 7 
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 20 
           THEN DATE_BEGIN_CRIF
           
           WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 7 
           THEN TRUNC(DATE_BEGIN_CRIF) + 7/24
           
           WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 20 
           THEN TRUNC(DATE_BEGIN_CRIF) + 1 + 7/24
           
           ELSE NULL 
       END AS DATE_BEGIN_CRIF_FIX,
       
       CASE 
           WHEN DATE_IN_WORK >= DATE_BEGIN_CRIF 
                AND DATE_IN_WORK < 
                    CASE 
                        WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 8 
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 20 
                        THEN DATE_BEGIN_CRIF
                        
                        WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 8 
                        THEN TRUNC(DATE_BEGIN_CRIF) + 8/24
                        
                        WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 20 
                        THEN TRUNC(DATE_BEGIN_CRIF) + 1 + 8/24
                        
                        WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 7 
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 20 
                        THEN DATE_BEGIN_CRIF
                        
                        WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 7 
                        THEN TRUNC(DATE_BEGIN_CRIF) + 7/24
                        
                        WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                             AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 20 
                        THEN TRUNC(DATE_BEGIN_CRIF) + 1 + 7/24
                        
                        ELSE NULL 
                    END 
           THEN 
               CASE 
                   WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                        AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 8 
                   THEN TRUNC(DATE_BEGIN_CRIF) + 8/24 + 1/(24*60)
                   
                   WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') IN ('Воскресенье', 'Суббота')
                        AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 8 
                   THEN TRUNC(DATE_BEGIN_CRIF) + 1 + 8/24 + 1/(24*60)
                   
                   WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                        AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) < 7 
                   THEN TRUNC(DATE_BEGIN_CRIF) + 7/24 + 1/(24*60)
                   
                   WHEN TO_CHAR(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') NOT IN ('Воскресенье', 'Суббота')
                        AND TO_NUMBER(TO_CHAR(DATE_BEGIN_CRIF, 'HH24')) >= 7 
                   THEN TRUNC(DATE_BEGIN_CRIF) + 1 + 7/24 + 1/(24*60)
                   
                   ELSE NULL 
               END 
           ELSE DATE_IN_WORK 
       END AS DATE_IN_WORK_FIX
FROM analytics.kdi_ipoteka_final a;
