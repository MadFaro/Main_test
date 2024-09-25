Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\io_ctrl.py", line 193, in inner
    return func(*args, **kwargs)
TypeError: span() got an unexpected keyword argument 'width'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 617, in game_noadmin
    span("", width='auto'),
  File "C:\Python38\lib\site-packages\pywebio\io_ctrl.py", line 197, in inner
    bound = sig.bind(*args, **kwargs).arguments
  File "C:\Python38\lib\inspect.py", line 3025, in bind
    return self._bind(args, kwargs)
  File "C:\Python38\lib\inspect.py", line 3014, in _bind
    raise TypeError(
TypeError: got an unexpected keyword argument 'width'
