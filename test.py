def insert_history_data_to_oracle(rows):
    """Вставляем новые записи истории в Oracle."""
    if not rows:
        print("Нет данных для загрузки истории.")
        return False

    try:
        # Создаем DataFrame для вставки данных
        df = pd.DataFrame(rows)

        oracle_conn = cx_Oracle.connect(user='', password='', dsn = '')
        cursor = oracle_conn.cursor()
        data_type = {
            'THREADHISTORYID': Integer,
            'THREADID': Integer,
            'NUMBER_': Integer,
            'STATE': String(1500),
            'OPERATORID': Integer,
            'DEPARTMENTID': Integer,
            'EVENT': String(1500)
        }
        # Используем to_sql для вставки данных в Oracle
        df.to_sql('TOLOG_BI_WEBIM_CHATTHREADHISTORY', con=oracle_conn, if_exists='append', schema='analytics', index=False, dtype=data_type)
        
        oracle_conn.commit()
        print("Данные истории успешно загружены в Oracle.")
        return True 

    except cx_Oracle.DatabaseError as e:
        print("Ошибка подключения к Oracle:", e)
        return False

    finally:
        cursor.close()
        oracle_conn.close()

40415 записей извлечено из chatthreadhistory.
webim.py:140: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  df.to_sql('TOLOG_BI_WEBIM_CHATTHREADHISTORY', con=oracle_conn, if_exists='append', schema='analytics', index=False, dtype=data_type)
Traceback (most recent call last):
  File "webim.py", line 264, in <module>
    schedule.run_pending()
  File "C:\Python38\lib\site-packages\schedule\__init__.py", line 854, in run_pending
    default_scheduler.run_pending()
  File "C:\Python38\lib\site-packages\schedule\__init__.py", line 101, in run_pending
    self._run_job(job)
  File "C:\Python38\lib\site-packages\schedule\__init__.py", line 173, in _run_job
    ret = job.run()
  File "C:\Python38\lib\site-packages\schedule\__init__.py", line 691, in run
    ret = self.job_func()
  File "webim.py", line 254, in job
    if insert_history_data_to_oracle(history_rows):
  File "webim.py", line 140, in insert_history_data_to_oracle
    df.to_sql('TOLOG_BI_WEBIM_CHATTHREADHISTORY', con=oracle_conn, if_exists='append', schema='analytics', index=False, dtype=data_type)
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 2878, in to_sql
    return sql.to_sql(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 767, in to_sql
    return pandas_sql.to_sql(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 2365, in to_sql
    raise ValueError(f"{col} ({my_type}) not a string")
ValueError: THREADHISTORYID (<class 'sqlalchemy.sql.sqltypes.Integer'>) not a string
