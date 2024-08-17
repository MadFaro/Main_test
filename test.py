Uncaught exception GET /?app=index&session=NEW (::1)
HTTPServerRequest(protocol='http', host='localhost:8080', method='GET', uri='/?app=index&session=NEW', version='HTTP/1.1', remote_ip='::1')
Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\tornado\websocket.py", line 630, in _run_callback
    result = callback(*args, **kwargs)
  File "C:\Python38\lib\site-packages\pywebio\platform\tornado.py", line 152, in on_message
    self._handler.send_client_data(message)
  File "C:\Python38\lib\site-packages\pywebio\platform\adaptor\ws.py", line 200, in send_client_data
    self.session.send_client_event(event)
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 141, in send_client_event
    coro_id = event['task_id']
KeyError: 'task_id'
