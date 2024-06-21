Traceback (most recent call last):
  File "1.py", line 33, in <module>
    df.to_sql('NP_ACC_FILLING', connect, if_exists='append', schema='analytics', index=False, dtype=data_type)
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 2878, in to_sql
    return sql.to_sql(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 767, in to_sql
    return pandas_sql.to_sql(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 1918, in to_sql
    total_inserted = sql_engine.insert_records(
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 1459, in insert_records
    return table.insert(chunksize=chunksize, method=method)
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 1021, in insert
    num_inserted = exec_insert(conn, keys, chunk_iter)
  File "C:\Python38\lib\site-packages\pandas\io\sql.py", line 927, in _execute_insert
    result = conn.execute(self.table.insert(), data)
  File "C:\Python38\lib\site-packages\sqlalchemy\engine\base.py", line 1385, in execute
    return meth(self, multiparams, params, _EMPTY_EXECUTION_OPTS)
  File "C:\Python38\lib\site-packages\sqlalchemy\sql\elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
  File "C:\Python38\lib\site-packages\sqlalchemy\engine\base.py", line 1577, in _execute_clauseelement
    ret = self._execute_context(
  File "C:\Python38\lib\site-packages\sqlalchemy\engine\base.py", line 1948, in _execute_context
    self._handle_dbapi_exception(
  File "C:\Python38\lib\site-packages\sqlalchemy\engine\base.py", line 2133, in _handle_dbapi_exception
    util.raise_(exc_info[1], with_traceback=exc_info[2])
  File "C:\Python38\lib\site-packages\sqlalchemy\util\compat.py", line 211, in raise_
    raise exception
  File "C:\Python38\lib\site-packages\sqlalchemy\engine\base.py", line 1885, in _execute_context
    self.dialect.do_executemany(
  File "C:\Python38\lib\site-packages\sqlalchemy\dialects\oracle\cx_oracle.py", line 1424, in do_executemany
    cursor.executemany(statement, parameters)
TypeError: expecting number

