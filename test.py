sqlalchemy.exc.DatabaseError: (cx_Oracle.DatabaseError) ORA-00904: : недопустимый идентификатор
[SQL:
CREATE TABLE analytics."TOLOG_BI_WEBIM_CHATTHREAD" (
        threadid NUMERIC,
        operatorfullname VARCHAR(1500 CHAR),
        operatorid NUMERIC,
        created DATE,
        modified DATE,
        state VARCHAR(1500 CHAR),
        offline NUMERIC,
        category VARCHAR(1500 CHAR),
        subcategory VARCHAR(1500 CHAR),
        threadkind VARCHAR(1500 CHAR)
)

]
(Background on this error at: https://sqlalche.me/e/14/4xp6)

data_type = {
'threadid': NUMERIC,
'operatorfullname': VARCHAR(1500),
'operatorid': NUMERIC,
'state': VARCHAR(1500),
'offline': NUMERIC,
'category': VARCHAR(1500),
'subcategory': VARCHAR(1500),
'threadkind': VARCHAR(1500)
}

df.to_sql('TOLOG_BI_WEBIM_CHATTHREAD', connect, if_exists='replace', schema='analytics', index=False, dtype=data_type)
