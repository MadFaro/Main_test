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
                         product_id,
                         login_customer,
                         value_operation,
                         status_operation
                    FROM operations
                    where login_customer = 'Замена' and operation_type != 'test'
               """

    sql_order = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         product_id,
                         login_customer,
                         value_operation,
                         status_operation
                    FROM operations
                    where product_id>=1
                    order by status_operation
                    
               """
    sql_order_count = """
                    SELECT count(*)
                         status_operation
                    FROM operations
                    where status_operation = 'accept'
                    """
    sql_balance = """
                    SELECT id,
                         datetime_insert,
                         operation_type,
                         product_id,
                         login_customer,
                         value_operation,
                         status_operation
                    FROM operations
                    where operation_type = 'addition'
               """