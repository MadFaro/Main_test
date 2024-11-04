async def my_monitoring(sdep, tab, fio, id, img_logo):
    # Функция для подключения к базе данных
    connect_str = lambda: cx_Oracle.connect(user='', password='', dsn='')
    connect = create_engine("oracle://", creator=connect_str)
    
    # Создаем и используем область с именем 'table_scope'
    with use_scope('table_scope', clear=True):
        put_html("<h2>Мониторинг чатов</h2>")
        
    while True:
        # Чтение данных из базы
        df_chat_wait = pd.read_sql(sql_oracle.sql_chat_wait, connect)
        
        # Обработка пустого DataFrame
        if not df_chat_wait.empty:
            df_chat_wait = df_chat_wait.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, pd.Timestamp) else x)
        else:
            df_chat_wait = pd.DataFrame([['Нет данных']], columns=['Сообщение'])
        
        # Обновление таблицы внутри области
        with use_scope('table_scope', clear=True):
            put_datatable(df_chat_wait.to_dict('records'), theme='alpine-dark', cell_content_bar=False)
        
        # Ожидание перед следующей итерацией
        await asyncio.sleep(30)
