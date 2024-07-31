WITH monetary_conditions AS (
    SELECT 'Отмена комиссии по 120 дней_КК' AS condition FROM DUAL UNION ALL
    SELECT 'Отмена комиссии по Прибыли' FROM DUAL UNION ALL
    SELECT 'Сниж.ставки на POS/ATM 3мес_КК' FROM DUAL UNION ALL
    SELECT 'Повыш. %на остаток 2мес._ДК' FROM DUAL UNION ALL
    SELECT 'Доп.2% УБ на 6мес_ДК' FROM DUAL UNION ALL
    SELECT 'Доп.2% по УБ на 6мес_КК' FROM DUAL UNION ALL
    SELECT 'Кэшбэк 10% на 1 мес_ДК' FROM DUAL UNION ALL
    SELECT 'Кэшбэк 10% на 1 мес_КК' FROM DUAL
),
non_monetary_conditions AS (
    SELECT 'Сохранена без механики_ДК' AS condition FROM DUAL UNION ALL
    SELECT 'Сохранена без механики_КК' FROM DUAL
),
all_conditions AS (
    SELECT condition FROM monetary_conditions
    UNION ALL
    SELECT condition FROM non_monetary_conditions
)
SELECT DISTINCT CALL_ID,
    CASE 
        WHEN rez1 IN (SELECT condition FROM monetary_conditions) OR
             rez2 IN (SELECT condition FROM monetary_conditions) OR
             rez3 IN (SELECT condition FROM monetary_conditions) OR
             rez4 IN (SELECT condition FROM monetary_conditions) OR
             rez5 IN (SELECT condition FROM monetary_conditions)
        THEN 'Денежная механика'
        ELSE NULL 
    END AS money,
    CASE 
        WHEN rez1 IN (SELECT condition FROM non_monetary_conditions) OR
             rez2 IN (SELECT condition FROM non_monetary_conditions) OR
             rez3 IN (SELECT condition FROM non_monetary_conditions) OR
             rez4 IN (SELECT condition FROM non_monetary_conditions) OR
             rez5 IN (SELECT condition FROM non_monetary_conditions)
        THEN 'Неденежная механика'
        ELSE NULL 
    END AS no_money
FROM ANALYTICS.KDI_SIEBEL_PAST
WHERE DIRECTION = 'ДТ'
  AND (rez1 IN (SELECT condition FROM all_conditions) OR
       rez2 IN (SELECT condition FROM all_conditions) OR
       rez3 IN (SELECT condition FROM all_conditions) OR
       rez4 IN (SELECT condition FROM all_conditions) OR
       rez5 IN (SELECT condition FROM all_conditions))
