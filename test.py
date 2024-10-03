df = pd.read_sql(sql.sql_operations_one_money.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))

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
