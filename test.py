SELECT 
    date(date_time) AS date,
    COUNT(CASE WHEN type_log = 'Сделал заказ' THEN 1 END) AS cnt_orders,
    COUNT(CASE WHEN type_log = 'Отменил заказ' THEN 1 END) AS cnt_cancellations
FROM log
WHERE login != 'ADMIN'
GROUP BY date(date_time)
ORDER BY date(date_time);
