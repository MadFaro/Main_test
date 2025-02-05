class sql:
    sql_product =   """
               SELECT 
                    id,
                    name,
                    price,
                    description,
                    img,
                    color,
                    size,
                    prom
               FROM product
               ORDER BY prom desc, name asc
                    """
    sql_user = """
               SELECT 
                    "index",
                    fio,
                    login,
                    sdep,
                    a.status,
                    sum(value_operation) as balance
               FROM users a
               left join operations b on a.login = b.login_customer
               where login != 'ADMIN'
               group by "index", fio, login, sdep,  a.status
               """

    sql_operations = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation,
                         cancel
                    FROM operations
                    where login_customer = 'Замена' and operation_type != 'test'
               """
    
    sql_operations_one = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation,
                         cancel
                    FROM operations
                    where id = Замена
               """
    
    sql_order = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation,
                         cancel
                    FROM operations
                    where operation_type not in ('Начисление', 'test') and status_operation != 'Отменен'
                    order by status_operation
                    
               """
    sql_order_count = """
                    SELECT count(*)
                         status_operation
                    FROM operations
                    where status_operation = 'Принят'
                    """
    sql_balance = """
                     SELECT id,
                         datetime_insert,
                         operation_type,
                         login_customer,
                         value_operation,
                         status_operation
                    FROM operations
                    where operation_type = 'Начисление' and datetime_insert >= DATE('now', '-90 days')
               """
    sql_basket = """
                    SELECT 
                         product_id,
                         login,
                         price,
                         img,
                         size,
                         color,
                         name
                    FROM basket
                    where login = 'Замена'

               """
    sql_question = """
                    SELECT id,
                         date_time,
                         login,
                         fio,
                         state,
                         category,
                         msg,
                         answer
                    FROM question
                    order by date_time
               """
    sql_question_one = """
                    SELECT id,
                         date_time,
                         login,
                         fio,
                         msg,
                         state,
                         category,
                         answer
                    FROM question
                    where id = 'Замена'
               """
    sql_offer = """
                    SELECT id,
                         date_time,
                         login,
                         fio_bd,
                         fio,
                         state,
                         offer,
                         answer
                    FROM offer_box
                    order by date_time
               """
    sql_offer_one = """
                    SELECT id,
                         date_time,
                         login,
                         fio_bd,
                         fio,
                         offer,
                         state,
                         answer
                    FROM offer_box
                    where id = 'Замена'
               """
    sql_mood = """
                    SELECT id,
                         date_time,
                         login,
                         fio,
                         state,
                         mood,
                         answer
                    FROM mood_box
                    order by date_time
               """
    sql_mood_one = """
                    SELECT id,
                         date_time,
                         login,
                         fio,
                         mood,
                         state,
                         answer
                    FROM mood_box
                    where id = 'Замена'
"""
    sql_dash_one = """
SELECT * FROM (
    SELECT 
        date(date_time, 'start of month') AS [Месяц],
        date(date_time) AS [Дата],
        COUNT(DISTINCT CASE WHEN type_log = 'Вход' THEN login END) AS [Входы],
        COUNT(DISTINCT CASE WHEN type_log = 'Открыл магазин' THEN login END) AS [Открыл магазин],
        COUNT(DISTINCT CASE WHEN type_log = 'Открыл гейм' THEN login END) AS [Открыл гейм],
        COUNT(DISTINCT CASE WHEN type_log = 'Открыл скидки' THEN login END) AS [Открыл скидки],
        COUNT(DISTINCT CASE WHEN type_log = 'Открыл объявления' THEN login END) AS [Открыл объявления],
        COUNT(CASE WHEN type_log = 'Задал вопрос' OR type_log = 'Отправил предложение' OR type_log = 'Отправил настроение' THEN 1 END) AS [Воспользовался боксом],
        COUNT(CASE WHEN type_log = 'Задал вопрос' THEN 1 END) AS [Задал вопрос],
        COUNT(CASE WHEN type_log = 'Отправил предложение' THEN 1 END) AS [Отправил предложение],
        COUNT(CASE WHEN type_log = 'Отправил настроение' THEN 1 END) AS [Отправил настроение],
        COUNT(CASE WHEN type_log = 'Сделал заказ' THEN 1 END) AS [Сделал заказ],
        COUNT(CASE WHEN type_log = 'Заказ отменен' THEN 1 END) AS [Отменил заказ]
    FROM log
    WHERE login != 'ADMIN' and date_time >= DATE('now', '-60 days')
    GROUP BY date(date_time)
    ORDER BY date(date_time)
)             """
    sql_online = """
                    SELECT date_time as [Дата],
                         user_ip as [IP],
                         user_login as [Логин]
                    FROM session

    """
    sql_msg = """
                    SELECT 
                         id,
                         operation_type,
                         status_operation,
                         value_operation,
                         datetime_insert
                    FROM operations
                    where login_customer = 'Замена' and operation_type != 'test' and on_read = 1
               """
    sql_full_log = """
    SELECT id as [ИД],
       date_time as [Дата],
       login as [Логин],
       type_log as [Событие]
  FROM log
    """
    sql_operations_one_money = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation,
                         cancel,
                         case1,
                         case2,
                         case3,
                         case4,
                         case5,
                         case6,
                         case7,
                         case8,
                         case9,
                         case10,
                         case11,
                         case12,
                         case13

                    FROM operations
                    where id = Замена
               """
    sql_discount = """
               SELECT id,
                    name,
                    img
               FROM discount
               """
    sql_box_history = """
               SELECT id,
                    'Идея' as type,
                    date_time,
                    fio,
                    offer as question,
                    state,
                    login,
                    answer
               FROM offer_box
               where login = 'Замена'
               union all
               SELECT id,
               'Настроение' as type,
                    date_time,
                    fio,
                    mood as question,
                    state,
                    login,
                    answer
               FROM mood_box
               where login = 'Замена'
               union all
               SELECT id,
               'Вопрос' as type,
                    date_time,
                    fio,
                    msg as question,
                    state,
                    login,
                    answer
               FROM question
               where login = 'Замена'    
    """

    sql_advt = """
               SELECT id,
                    date_ad [Дата],
                    fio,
                    login,
                    phone,
                    category [Категория],
                    city [Город],
                    name [Тема],
                    text_ad,
                    file_ad,
                    moderation
               FROM advt
               where moderation = 1 and date_ad >= DATE('now', '-30 days')
    """
    sql_advt_moderation = """
               SELECT id,
                    date_ad [Дата],
                    fio,
                    login,
                    phone,
                    category [Категория],
                    city [Город],
                    name [Тема],
                    text_ad,
                    file_ad,
                    moderation
               FROM advt
               where moderation = 0
    """
    sql_advt_main = """
               SELECT id,
                    date_ad [Дата],
                    fio,
                    login,
                    phone,
                    category [Категория],
                    city [Город],
                    name [Тема],
                    text_ad,
                    file_ad,
                    moderation
               FROM advt
               where moderation = 1 and login = 'Замена'
    """
