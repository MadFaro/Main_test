prod.py:25: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  df = pd.read_sql_query(query, conn)
Traceback (most recent call last):
  File "prod.py", line 65, in <module>
    cursor.executemany(insert_query, records)
psycopg2.ProgrammingError: can't adapt type 'numpy.int64'
