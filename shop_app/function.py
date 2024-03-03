class sql:
    sql_product =   """
               SELECT 
                    id,
                    name,
                    price,
                    description,
                    img
               FROM product
                    """
    sql_user = """
               SELECT 
                    "index",
                    fio,
                    login,
                    sdep,
                    sum(value_operation) as balance
               FROM users a
               left join operations b on a.login = b.login_customer
               where login != 'admin'
               group by "index", fio, login, sdep
               """

    sql_operations = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation
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
                         status_operation
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
                         status_operation
                    FROM operations
                    where operation_type not in ('Начисление', 'test')
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
                    where operation_type = 'Начисление'
               """
    sql_basket = """
                    SELECT 
                         product_id,
                         login,
                         price,
                         img,
                         size,
                         color
                    FROM basket
                    where login = 'Замена'

               """