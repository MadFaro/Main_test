Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2200, in execute
    cur.execute(sql, *args)
sqlite3.Warning: You can only execute one statement at a time.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 101, in _start_main_task
    await target()
  File "main.py", line 113, in main
    await main_menu(sdep='noadmin', tab=user_login[0], fio=user_info[1], id = user_info[0])
  File "main.py", line 162, in main_menu
    df = pd.read_sql(sql.sql_msg.replace('Замена', str(tab)), connect("Convert/db/shop.db"))
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 633, in read_sql
    return pandas_sql.read_query(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2264, in read_query
    cursor = self.execute(sql, params)
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2212, in execute
    raise ex from exc
pandas.errors.DatabaseError: Execution failed on sql '
                    SELECT
                         login,
                         state,
                         date
                    FROM new_msg;
                    where login = 'TOLOGONOVAB@URALSIB.RU'
               ': You can only execute one statement at a time.
