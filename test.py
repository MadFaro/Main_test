async def my_monitoring(sdep, tab, fio, id, img_logo):

    try:
        clear()
    except:
        pass

    connect_str = lambda: cx_Oracle.connect(user='', password='', dsn = '')
    connect = create_engine("oracle://", creator=connect_str)
    
    while True:
        df_chat_wait = pd.read_sql(sql_oracle.sql_chat_wait, connect)
        
        if not df_chat_wait.empty:
            df_chat_wait = df_chat_wait.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, pd.Timestamp) else x)
        else:
            df_chat_wait = pd.DataFrame([['Нет данных']], columns=['Сообщение'])

        clear('table')
        put_column([put_datatable(df_chat_wait.to_dict('records'), theme='alpine-dark', cell_content_bar=False)], scope='table')
        use_scope
        await asyncio.sleep(30)
