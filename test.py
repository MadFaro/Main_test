sqlalchemy.exc.ProgrammingError: (psycopg2.errors.GroupingError) ОШИБКА:  столбец "log.date_time" должен фигурировать в предложении GROUP BY или использоваться в агрегатной функции
LINE 4:                        DATE_TRUNC('month', date_time) AS "Ме...
                                                   ^

[SQL:
               SELECT * FROM (
                   SELECT
                       DATE_TRUNC('month', date_time) AS "Месяц",
                       DATE(date_time) AS "Дата",
                       COUNT(DISTINCT CASE WHEN type_log = 'Вход' THEN login END) AS "Входы",
                       COUNT(DISTINCT CASE WHEN type_log = 'Открыл магазин' THEN login END) AS "Открыл магазин",
                       COUNT(DISTINCT CASE WHEN type_log = 'Открыл гейм' THEN login END) AS "Открыл гейм",
                       COUNT(DISTINCT CASE WHEN type_log = 'Открыл скидки' THEN login END) AS "Открыл скидки",
                       COUNT(DISTINCT CASE WHEN type_log = 'Открыл объявления' THEN login END) AS "Открыл объявления",
                       COUNT(CASE WHEN type_log IN ('Задал вопрос', 'Отправил предложение', 'Отправил настроение') THEN 1 END) AS "Воспользовался боксом",
                       COUNT(CASE WHEN type_log = 'Задал вопрос' THEN 1 END) AS "Задал вопрос",
                       COUNT(CASE WHEN type_log = 'Отправил предложение' THEN 1 END) AS "Отправил предложение",
                       COUNT(CASE WHEN type_log = 'Отправил настроение' THEN 1 END) AS "Отправил настроение",
                       COUNT(CASE WHEN type_log = 'Сделал заказ' THEN 1 END) AS "Сделал заказ",
                       COUNT(CASE WHEN type_log = 'Заказ отменен' THEN 1 END) AS "Отменил заказ"
                   FROM log
                   WHERE login != 'ADMIN' AND date_time >= CURRENT_DATE - INTERVAL '60 days'
                   GROUP BY DATE(date_time)
                   ORDER BY DATE(date_time)
               ) AS subquery
