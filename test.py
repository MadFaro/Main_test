Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2200, in execute
    cur.execute(sql, *args)
sqlite3.OperationalError: no such function: json_extract

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 1472, in dashboard_user
    df3 = pd.read_sql(sql.sql_top_product, connect("Convert/db/shop.db"))
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 633, in read_sql
    return pandas_sql.read_query(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2264, in read_query
    cursor = self.execute(sql, params)
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2212, in execute
    raise ex from exc
pandas.errors.DatabaseError: Execution failed on sql '
                    WITH RECURSIVE
                    json_data(id, datetime_insert, operation_type, json, login_customer, value_operation, status_operation, idx, product_id, count) AS (
                    -- Начальный запрос: извлечение первого элемента
                    SELECT
                         id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation,
                         0 AS idx, -- Индекс элемента в массиве
                         json_extract(json, '$[0].product_id') AS product_id,
                         json_extract(json, '$[0].count') AS count
                    FROM
                         operations
                    WHERE
                         json_extract(json, '$[0].product_id') IS NOT NULL --and datetime_insert >= date('now', 'start of month', '-1 month')
                    UNION ALL
                    SELECT
                         id,
                         datetime_insert,
                         operation_type,
                         json,
                         login_customer,
                         value_operation,
                         status_operation,
                         idx + 1,
                         json_extract(json, printf('$[%d].product_id', idx + 1)) AS product_id,
                         json_extract(json, printf('$[%d].count', idx + 1)) AS count
                    FROM
                         json_data
                    WHERE
                         json_extract(json, printf('$[%d].product_id', idx + 1)) IS NOT NULL
                         AND idx < 10
                    )

                    SELECT
                    b.name,
                    sum(count) as cnt
                    FROM
                    json_data a
                    left join product b on a.product_id = b.id
                    group by b.name
                    order by sum(count)
                    limit 5    
    
    ': no such function: json_extract
