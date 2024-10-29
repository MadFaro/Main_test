Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 101, in _start_main_task
    await target()
  File "main.py", line 48, in main
    cipher_suite = Fernet(key)
  File "C:\Python38\lib\site-packages\cryptography\fernet.py", line 40, in __init__
    raise ValueError(
ValueError: Fernet key must be 32 url-safe base64-encoded bytes.
