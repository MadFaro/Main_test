WITH RankedData AS (
    SELECT 
        TYPE, 
        DATE_CREATED, 
        ID, 
        CLIENT_FIO, 
        CLIENT_DID, 
        IBSO_ID_OR_CALLED_FROM_NUM, 
        CARD_TYPE, 
        HAVE_REDIRECT, 
        MONEY,
        ROW_NUMBER() OVER (PARTITION BY CLIENT_DID ORDER BY 
            CASE 
                WHEN CARD_TYPE = 'Кредитная карта' THEN 1  -- Приоритет для Кредитной карты
                WHEN CARD_TYPE = 'Дебетовая карта' THEN 2  -- Приоритет для Дебетовой карты
                ELSE 3  -- Для "Не определено" минимальный приоритет
            END, 
            DATE_CREATED DESC) AS RN  -- Второй уровень сортировки по дате
    FROM (
        -- Чаты
        SELECT 
            'Чаты' AS TYPE, 
            CREATED AS DATE_CREATED, 
            THREADID AS ID, 
            CLIENT_NAME AS CLIENT_FIO, 
            CLIENT_DID,
            CLIENT_IBSO_ID AS IBSO_ID_OR_CALLED_FROM_NUM,
            CASE 
                WHEN SUBCATEGORY IS NULL AND CATEGORY IS NULL THEN 'Не определено'
                WHEN (SUBCATEGORY IN ('РБ_Закрытие_ДейстПотреб','РБ_Закрытие_Прибыль','РБ_Закрытие_МИР','РБ_Закрытие_Эконом','Дебетовые карты') 
                      OR CATEGORY IN ('РБ_Закрытие_ДейстПотреб','РБ_Закрытие_Прибыль','РБ_Закрытие_МИР','РБ_Закрытие_Эконом','Дебетовые карты') 
                      OR LOWER(SUBCATEGORY) LIKE '%дебет%' OR LOWER(CATEGORY) LIKE '%дебет%') THEN 'Дебетовая карта' 
                WHEN (SUBCATEGORY IN ('РБ_Закрытие_120','РБ_Закрытие_кредитная карта с кэшбеком','РБ_Закрытие_ДейстКК','РБ_Закрытие_КК MIR Supreme','РБ_Закрытие_КЦ_СКБ','Кредитные карты') 
                      OR CATEGORY IN ('РБ_Закрытие_120','РБ_Закрытие_кредитная карта с кэшбеком','РБ_Закрытие_ДейстКК','РБ_Закрытие_КК MIR Supreme','РБ_Закрытие_КЦ_СКБ','Кредитные карты') 
                      OR LOWER(SUBCATEGORY) LIKE '%кредит%' OR LOWER(CATEGORY) LIKE '%кредит%') THEN 'Кредитная карта' 
                ELSE 'Не определено' 
            END AS card_type,
            HAVE_REDIRECT,
            0 AS MONEY
        FROM ANALYTICS.TOLOG_RETENTIONS_CHATS_TABLE
        WHERE CLIENT_DID IS NOT NULL
        UNION ALL
        -- Звонки
        SELECT 
            'Звонки' AS TYPE,
            a.dt - INTERVAL '2' HOUR AS DATE_CREATED,
            CAST(a.call_id AS NUMBER) AS ID, 
            a.FIO AS CLIENT_FIO,
            d.CLIENT_DID,
            a.CALLED_FROM_NUM AS IBSO_ID_OR_CALLED_FROM_NUM,
            CASE 
                WHEN (LOWER(a.SUBJ1) LIKE '%дебет%' OR LOWER(a.SUBJ2) LIKE '%дебет%' OR LOWER(a.SUBJ3) LIKE '%дебет%' OR LOWER(a.SUBJ4) LIKE '%дебет%' OR LOWER(a.SUBJ5) LIKE '%дебет%') THEN 'Дебетовая карта'
                WHEN (LOWER(a.PRODUCT1) LIKE '%дебет%' OR LOWER(a.PRODUCT2) LIKE '%дебет%' OR LOWER(a.PRODUCT3) LIKE '%дебет%' OR LOWER(a.PRODUCT4) LIKE '%дебет%' OR LOWER(a.PRODUCT5) LIKE '%дебет%') THEN 'Дебетовая карта'
                WHEN (LOWER(a.SUBJ1R) LIKE '%дебет%' OR LOWER(a.SUBJ2R) LIKE '%дебет%' OR LOWER(a.SUBJ3R) LIKE '%дебет%' OR LOWER(a.SUBJ4R) LIKE '%дебет%' OR LOWER(a.SUBJ5R) LIKE '%дебет%') THEN 'Дебетовая карта'
                WHEN (LOWER(a.PRODUCT1R) LIKE '%дебет%' OR LOWER(a.PRODUCT2R) LIKE '%дебет%' OR LOWER(a.PRODUCT3R) LIKE '%дебет%' OR LOWER(a.PRODUCT4R) LIKE '%дебет%' OR LOWER(a.PRODUCT5R) LIKE '%дебет%') THEN 'Дебетовая карта'
                WHEN (LOWER(a.SUBJ1) LIKE '%кредит%' OR LOWER(a.SUBJ2) LIKE '%кредит%' OR LOWER(a.SUBJ3) LIKE '%кредит%' OR LOWER(a.SUBJ4) LIKE '%кредит%' OR LOWER(a.SUBJ5) LIKE '%кредит%') THEN 'Кредитная карта'
                WHEN (LOWER(a.PRODUCT1) LIKE '%кредит%' OR LOWER(a.PRODUCT2) LIKE '%кредит%' OR LOWER(a.PRODUCT3) LIKE '%кредит%' OR LOWER(a.PRODUCT4) LIKE '%кредит%' OR LOWER(a.PRODUCT5) LIKE '%кредит%') THEN 'Кредитная карта'
                WHEN (LOWER(a.SUBJ1R) LIKE '%кредит%' OR LOWER(a.SUBJ2R) LIKE '%кредит%' OR LOWER(a.SUBJ3R) LIKE '%кредит%' OR LOWER(a.SUBJ4R) LIKE '%кредит%' OR LOWER(a.SUBJ5R) LIKE '%кредит%') THEN 'Кредитная карта'
                WHEN (LOWER(a.PRODUCT1R) LIKE '%кредит%' OR LOWER(a.PRODUCT2R) LIKE '%кредит%' OR LOWER(a.PRODUCT3R) LIKE '%кредит%' OR LOWER(a.PRODUCT4R) LIKE '%кредит%' OR LOWER(a.PRODUCT5R) LIKE '%кредит%') THEN 'Кредитная карта'
                ELSE 'Не определено'
            END AS card_type,
            HAVE_REDIRECT,
            0 AS MONEY
        FROM ANALYTICS.TOLOG_RETENTIONS_CALLS_TABLE a
        LEFT JOIN cmdm2.CLIENT_AGR_ID_X_CLIENT_DID d ON a.client_id = d.client_kih_id
        WHERE d.client_did IS NOT NULL
    )
)
SELECT 
    MAX(TYPE) AS TYPE, 
    MAX(DATE_CREATED) AS DATE_CREATED, 
    MAX(ID) AS ID, 
    CLIENT_FIO, 
    CLIENT_DID,
    MAX(IBSO_ID_OR_CALLED_FROM_NUM) AS IBSO_ID_OR_CALLED_FROM_NUM, 
    MAX(CARD_TYPE) AS CARD_TYPE, 
    MAX(HAVE_REDIRECT) AS HAVE_REDIRECT,
    MAX(MONEY) AS MONEY
FROM RankedData
WHERE RN = 1  -- Выбираем только первую строку для каждого клиента
GROUP BY CLIENT_FIO, CLIENT_DID
