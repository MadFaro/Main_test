WITH base_data AS (
    SELECT
        DT,
        PODRAZDELENIE,
        SUBJ1,
        -- Добавление поля "Неделя"
        TO_CHAR(TRUNC(DT, 'IW'), 'DD') || '-' || TO_CHAR(TRUNC(DT + 6, 'IW'), 'DD.MM') AS "Неделя",
        -- Добавление поля "Месяц"
        TO_CHAR(DT, 'YY') || '.' || TO_CHAR(DT, 'MON') AS "Месяц",
        -- Добавление поля "Группа"
        CASE
            WHEN PODRAZDELENIE NOT IN (
                'Группа по работе с ключевыми клиентами',
                'Группа сопровождения ипотечных сделок'
            ) THEN 'Общая'
            ELSE PODRAZDELENIE
        END AS "Группа",
        -- Добавление поля "Тематики брокер"
        CASE
            WHEN SUBJ1 IN ('Уралсиб Брокер', 'Твой Брокер') THEN 1
            ELSE 0
        END AS "Тематики брокер"
    FROM
        analytics.tolog_fcr_call_them
)
SELECT
    DT,
    PODRAZDELENIE,
    SUBJ1,
    "Неделя",
    "Месяц",
    "Группа",
    "Тематики брокер"
FROM
    base_data;
