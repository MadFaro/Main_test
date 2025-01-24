WITH SourceData AS (
    SELECT 
        *,
        TRUNC(DTM) AS DTM_DATE,
        CASE 
            WHEN DESCRIPTION IN (
                'ДДО АктивКредит', 
                'ДДО Группа 1', 
                'ДДО Группа 2', 
                'ДДО Группа 5', 
                'ДДО Группа 8', 
                'ДДО Группа 9', 
                'ДДО Группа 10', 
                'ДДО Группа 11', 
                'ДДО Группа 12', 
                'ДДО Группа 13', 
                'ДДО Группа 14'
            ) THEN 'Общая'
            WHEN DESCRIPTION = 'ДДО Премиум' 
                AND FIRSTNAME NOT IN (
                    'Шекеринская Екатерина Евгеньевна', 
                    'Сатарова Сайера Алиевна', 
                    'Максимов Дмитрий Владимирович'
                ) THEN 'Премиум'
            ELSE DESCRIPTION
        END AS Группа,
        TO_CHAR(TRUNC(DTM, 'IW'), 'DD') || '-' || TO_CHAR(TRUNC(DTM + 6, 'IW'), 'DD.MM') AS Неделя,
        TO_CHAR(DTM, 'YY') || '.' || TO_CHAR(DTM, 'MON', 'NLS_DATE_LANGUAGE=RUSSIAN') AS Месяц
    FROM analytics.tolog_call_evaluations_scores
)
SELECT *
FROM SourceData;
