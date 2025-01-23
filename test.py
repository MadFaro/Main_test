WITH base_data AS (
    SELECT
        TRUNC(a.DATE_) AS DATETIME,
        b.DESCRIPTION,
        b.FULLNAME,
        COALESCE(a.CREDITFLOW, 0) AS CREDITFLOW,
        SUM(b.LOGGEDONTIME) AS LOGGEDONTIME,
        SUM(b.TALKTIME) AS TALKTIME,
        SUM(b.HOLDTIME) AS HOLDTIME,
        SUM(b.WRAPTIME) AS WRAPTIME,
        SUM(b.AVAILTIME) AS AVAILTIME,
        SUM(b.RESERVEDTIME) AS RESERVEDTIME,
        SUM(b.CALLSHANDLED) AS CALLSHANDLED,
        SUM(b.HANDLEDCALLSTIME) AS HANDLEDCALLSTIME,
        SUM(b.ANSWERWAITTIME) AS ANSWERWAITTIME,
        SUM(b.CALLSANSWERED) AS CALLSANSWERED
    FROM
        ANALYTICS.TOLOG_CISCO_OPERATOR_STATE a
    LEFT JOIN
        ANALYTICS.CISCO_OPERATOR b
        ON a.OPERATOR_ = SUBSTR(b.FULLNAME, INSTR(b.FULLNAME, ', ') + 2)
        AND a.DATE_ = TRUNC(b.DATETIME)
    WHERE
        b.DESCRIPTION LIKE '%ДДО%'
        AND b.DATETIME >= TRUNC(ADD_MONTHS(SYSDATE, -6), 'MM')
    GROUP BY
        TRUNC(a.DATE_),
        b.DESCRIPTION,
        b.FULLNAME,
        a.CREDITFLOW
),
processed_data AS (
    SELECT
        DATETIME,
        CASE
            WHEN DESCRIPTION = 'ДДО Брокер' THEN 'ДДО Премиум'
            ELSE DESCRIPTION
        END AS DESCRIPTION,
        FULLNAME,
        LOGGEDONTIME,
        TALKTIME,
        HOLDTIME,
        WRAPTIME,
        AVAILTIME,
        RESERVEDTIME,
        CALLSHANDLED,
        HANDLEDCALLSTIME,
        ANSWERWAITTIME,
        CALLSANSWERED,
        CREDITFLOW,
        -- Добавление поля "Неделя"
        TO_CHAR(TRUNC(DATETIME, 'IW'), 'DD') || '-' || TO_CHAR(TRUNC(DATETIME + 6, 'IW'), 'DD.MM') AS "Неделя",
        -- Добавление поля "Месяц"
        TO_CHAR(DATETIME, 'YY') || '.' || TO_CHAR(DATETIME, 'MON') AS "Месяц",
        -- Добавление поля "Фильтр"
        'Да' AS "Фильтр",
        -- Добавление поля "Группа"
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
                AND FULLNAME NOT IN (
                    '11317, Шекеринская Екатерина Евгеньевна',
                    '12288, Сатарова Сайера Алиевна',
                    '12296, Максимов Дмитрий Владимирович'
                ) THEN 'Премиум'
            ELSE DESCRIPTION
        END AS "Группа"
    FROM
        base_data
)
SELECT
    DATETIME,
    DESCRIPTION,
    FULLNAME,
    LOGGEDONTIME,
    TALKTIME,
    HOLDTIME,
    WRAPTIME,
    AVAILTIME,
    RESERVEDTIME,
    CALLSHANDLED,
    HANDLEDCALLSTIME,
    ANSWERWAITTIME,
    CALLSANSWERED,
    "Неделя",
    "Месяц",
    "Фильтр",
    "Группа",
    CREDITFLOW
FROM
    processed_data
ORDER BY
    DATETIME ASC;
