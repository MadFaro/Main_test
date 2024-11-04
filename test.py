Unhandled error in pywebio app
Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 2068, in my_monitoring
    put_datatable(df_chat_wait.to_dict('records'), theme='alpine-dark', cell_content_bar=False)], scope='table')]).style('width:99%;height:100%;')
  File "C:\Python38\lib\site-packages\pywebio\output.py", line 1692, in put_datatable
    return Output(spec)
  File "C:\Python38\lib\site-packages\pywebio\io_ctrl.py", line 69, in __init__
    self.spec = type(self).dump_dict(spec)  # this may raise TypeError
  File "C:\Python38\lib\site-packages\pywebio\io_ctrl.py", line 55, in dump_dict
    return json.loads(json.dumps(data, default=cls.json_encoder))
  File "C:\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Python38\lib\site-packages\pywebio\io_ctrl.py", line 50, in json_encoder
    raise TypeError('Object of type  %s is not JSON serializable' % obj.__class__.__name__)
TypeError: Object of type  Timestamp is not JSON serializable


async def my_monitoring(sdep, tab, fio, id, img_logo):

    try:
        clear()
    except:
        pass

    connect_str = lambda: cx_Oracle.connect(user='', password='', dsn = '')
    connect = create_engine("oracle://", creator=connect_str)
    
    while True:
        df_chat_wait = pd.read_sql(sql_oracle.sql_chat_wait, connect)
        
        print(df_chat_wait)
        if df_chat_wait.empty:
            df_chat_wait = pd.DataFrame([['Нет данных']], columns=['Сообщение'])

        clear('table')
        put_row([
        None,
        put_image(img_logo, width='auto', height='auto').style('place-self: center;'),
        put_button("\U0001F3E0\n\r        Главная        ", onclick=lambda: noadmin(sdep, tab, fio, id), color='dark', outline=True).style('font-size: 2vh')]).style('padding:0.4em;background:rgb(255 255 255);grid-template-columns:0.1fr 1fr 0.1fr;')
                    
        put_row([
                None,
                None,
        put_column([
                None,
            put_datatable(df_chat_wait.to_dict('records'), theme='alpine-dark', cell_content_bar=False)], scope='table')]).style('width:99%;height:100%;')
        put_html(f"""
            <footer class="footer">
            {fio}
            </footer>
        """).style("width:100%;z-index:21;position:absolute;bottom:0px")
        await asyncio.sleep(120)
