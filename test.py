Traceback (most recent call last):
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 2198, in dashboard_user
    put_datatable(
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\output.py", line 1692, in put_datatable
    return Output(spec)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\io_ctrl.py", line 69, in __init__
    self.spec = type(self).dump_dict(spec)  # this may raise TypeError
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\io_ctrl.py", line 55, in dump_dict
    return json.loads(json.dumps(data, default=cls.json_encoder))
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\io_ctrl.py", line 50, in json_encoder
    raise TypeError('Object of type  %s is not JSON serializable' % obj.__class__.__name__)
TypeError: Object of type  Timestamp is not JSON serializable
Unhandled error in pywebio app



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
               ORDER BY prom DESC, name ASC
                    """
    
    sql_user = """
               SELECT 
                    index,
                    fio,
                    login,
                    sdep,
                    a.status,
                    SUM(value_operation) AS balance
               FROM users a
               LEFT JOIN operations b ON a.login = b.login_customer
               WHERE login != 'ADMIN'
               GROUP BY index, fio, login, sdep, a.status
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
               WHERE login_customer = 'Замена' AND operation_type != 'test'
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
               WHERE id = 'Замена'
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
               WHERE operation_type NOT IN ('Начисление', 'test') AND status_operation != 'Отменен'
               ORDER BY status_operation
               """
    
    sql_order_count = """
               SELECT COUNT(*) AS count
               FROM operations
               WHERE status_operation = 'Принят'
               """
    
    sql_balance = """
               SELECT id,
                    datetime_insert,
                    operation_type,
                    login_customer,
                    value_operation,
                    status_operation
               FROM operations
               WHERE operation_type = 'Начисление' AND datetime_insert >= CURRENT_DATE - INTERVAL '90 days'
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
               WHERE login = 'Замена'
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
               ORDER BY date_time
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
               WHERE id = 'Замена'
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
               ORDER BY date_time
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
               WHERE id = 'Замена'
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
               ORDER BY date_time
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
               WHERE id = 'Замена'
               """
    
    sql_dash_one = """
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
                   GROUP BY DATE_TRUNC('month', date_time), DATE(date_time)
                   ORDER BY DATE_TRUNC('month', date_time), DATE(date_time)
               ) AS subquery
               """
    
    sql_online = """
               SELECT date_time AS "Дата",
                    user_ip AS "IP",
                    user_login AS "Логин"
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
               WHERE login_customer = 'Замена' AND operation_type != 'test' AND on_read = 1
               """
    
    sql_full_log = """
               SELECT id AS "ИД",
                    date_time AS "Дата",
                    login AS "Логин",
                    type_log AS "Событие"
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
               WHERE id = 'Замена'
               """
    
    sql_discount = """
               SELECT id,
                    name,
                    img
               FROM discount
               """
    
    sql_box_history = """
               SELECT id,
                    'Идея' AS type,
                    date_time,
                    fio,
                    offer AS question,
                    state,
                    login,
                    answer
               FROM offer_box
               WHERE login = 'Замена'
               UNION ALL
               SELECT id,
                    'Настроение' AS type,
                    date_time,
                    fio,
                    mood AS question,
                    state,
                    login,
                    answer
               FROM mood_box
               WHERE login = 'Замена'
               UNION ALL
               SELECT id,
                    'Вопрос' AS type,
                    date_time,
                    fio,
                    msg AS question,
                    state,
                    login,
                    answer
               FROM question
               WHERE login = 'Замена'
               """
    
    sql_advt = """
               SELECT id,
                    date_ad AS "Дата",
                    fio,
                    login,
                    phone,
                    category AS "Категория",
                    city AS "Город",
                    name AS "Тема",
                    text_ad,
                    file_ad,
                    moderation
               FROM advt
               WHERE moderation = 1 AND date_ad >= CURRENT_DATE - INTERVAL '30 days'
               """
    
    sql_advt_moderation = """
               SELECT id,
                    date_ad AS "Дата",
                    fio,
                    login,
                    phone,
                    category AS "Категория",
                    city AS "Город",
                    name AS "Тема",
                    text_ad,
                    file_ad,
                    moderation
               FROM advt
               WHERE moderation = 0
               """
    
    sql_advt_main = """
               SELECT id,
                    date_ad AS "Дата",
                    fio,
                    login,
                    phone,
                    category AS "Категория",
                    city AS "Город",
                    name AS "Тема",
                    text_ad,
                    file_ad,
                    moderation
               FROM advt
               WHERE moderation = 1 AND login = 'Замена'
               """
