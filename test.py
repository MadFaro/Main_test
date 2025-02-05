Traceback (most recent call last):
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 2198, in dashboard_user
    put_datatable(
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\output.py", line 1692, in put_datatable
    return Output(spec)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\io_ctrl.py", line 69, in __init__
    self.spec = type(self).dump_dict(spec)  # this may raise TypeError
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\io_ctrl.py", line 55, in dump_dict
    return json.loads(json.dumps(data, default=cls.json_encoder))
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\io_ctrl.py", line 50, in json_encoder
    raise TypeError('Object of type  %s is not JSON serializable' % obj.__class__.__name__)
TypeError: Object of type  Timestamp is not JSON serializable
