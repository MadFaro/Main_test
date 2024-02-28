import datetime
import cx_Oracle
import pandas as pd
import win32com.client
from sqlalchemy import create_engine

def connect_str(): 
    return cx_Oracle.connect(user='user',
                             password='pass', 
                             dsn='dsn')

connect = create_engine("oracle://", creator=connect_str)

# Список таблиц, которые вы хотите проверить
tables_to_check = ['tab1', 'tab2', 'tab3', 'tab4', 'tab5']

sql = """
select ACTION_DATE, ACTION_TYPE, RESULT_TYPE, TABLE_NAME, ROWS_COUNT, PROC_NAME from (
select ACTION_DATE, ACTION_TYPE, RESULT_TYPE, TABLE_NAME, ROWS_COUNT, PROC_NAME,
ROW_NUMBER() OVER (PARTITION BY TABLE_NAME ORDER BY ACTION_DATE desc) as rnk
from job_logs
where trunc(ACTION_DATE)=trunc(sysdate) and TABLE_NAME in (
{}
))
""".format(','.join(["'{}'".format(table) for table in tables_to_check]))

data = pd.read_sql(sql, connect)

# Создаем DataFrame с недостающими таблицами и заполняем остальные столбцы
missing_tables = set(tables_to_check) - set(data['TABLE_NAME'])
missing_data = pd.DataFrame(columns=['ACTION_DATE', 'ACTION_TYPE', 'RESULT_TYPE', 'TABLE_NAME', 'ROWS_COUNT', 'PROC_NAME'])
missing_data['TABLE_NAME'] = list(missing_tables)
missing_data['RESULT_TYPE'] = 'нет записи в логах'
missing_data.fillna('', inplace=True)

# Объединяем данные
final_data = pd.concat([data, missing_data], ignore_index=True)

# Отображаем результат
print(final_data.to_html(index=False))
