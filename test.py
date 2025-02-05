C:\Users\TologonovAB\Desktop>Python prod.py
prod.py:24: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  df = pd.read_sql_query(query, conn)
Traceback (most recent call last):
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\base.py", line 3652, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'JSON'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "prod.py", line 36, in <module>
    json_data = row['JSON']
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\series.py", line 1007, in __getitem__
    return self._get_value(key)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\series.py", line 1116, in _get_value
    loc = self.index.get_loc(label)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\base.py", line 3654, in get_loc
    raise KeyError(key) from err
KeyError: 'JSON'
