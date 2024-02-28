import datetime
import cx_Oracle
import pandas as pd
import win32com.client
from sqlalchemy import create_engine


def connect_str(): return cx_Oracle.connect(user='user',
                                            password='pass', 
                                            dsn='dsn')

connect = create_engine("oracle://", creator=connect_str)

sql = """
select ACTION_DATE, ACTION_TYPE, RESULT_TYPE, TABLE_NAME, ROWS_COUNT, PROC_NAME from (
select ACTION_DATE, ACTION_TYPE, RESULT_TYPE, TABLE_NAME, ROWS_COUNT, PROC_NAME,
ROW_NUMBER() OVER (PARTITION BY TABLE_NAME ORDER BY ACTION_DATE desc) as rnk
from job_logs
where trunc(ACTION_DATE)=trunc(sysdate) and TABLE_NAME in (
'tab1',
'tab2',
'tab3',
'tab4',
'tab5'
))
where rnk = 1
    """

data = pd.read_sql(sql, connect).to_html(index=False)

print(data)
