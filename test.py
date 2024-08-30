SELECT * FROM (
    SELECT 
        date(date_time) AS date,
        COUNT(DISTINCT CASE WHEN type_log = 'Вход' THEN login END) AS cnt_up,
        COUNT(CASE WHEN type_log = 'Открыл магазин' THEN 1 END) AS cnt_shop,
        COUNT(CASE WHEN type_log = 'Открыл гейм' THEN 1 END) AS cnt_game,
        COUNT(CASE WHEN type_log = 'Задал вопрос' OR type_log = 'Отправил предложение' OR type_log = 'Отправил настроение' THEN 1 END) AS cnt_box,
        COUNT(CASE WHEN type_log = 'Задал вопрос' THEN 1 END) AS cnt_quest,
        COUNT(CASE WHEN type_log = 'Отправил предложение' THEN 1 END) AS cnt_offer,
        COUNT(CASE WHEN type_log = 'Отправил настроение' THEN 1 END) AS cnt_mood,
        COUNT(CASE WHEN type_log = 'Сделал заказ' THEN 1 END) AS cnt_orders,
        COUNT(CASE WHEN type_log = 'Заказ отменен' THEN 1 END) AS cnt_cancellations
    FROM log
    WHERE login != 'ADMIN'
    GROUP BY date(date_time)
    ORDER BY date(date_time)
);
