Unhandled error in pywebio app
Traceback (most recent call last):
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 427, in exit_shop
    await main()
  File "main.py", line 125, in main
    user_token = cipher_suite.decrypt(str(user_login_token).encode()).decode()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\cryptography\fernet.py", line 86, in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\cryptography\fernet.py", line 122, in _get_unverified_token_data
    raise InvalidToken
cryptography.fernet.InvalidToken
Unhandled error in pywebio app
Traceback (most recent call last):
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 427, in exit_shop
    await main()
  File "main.py", line 125, in main
    user_token = cipher_suite.decrypt(str(user_login_token).encode()).decode()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\cryptography\fernet.py", line 86, in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\cryptography\fernet.py", line 122, in _get_unverified_token_data
    raise InvalidToken
cryptography.fernet.InvalidToken
Unhandled error in pywebio app
Traceback (most recent call last):
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 427, in exit_shop
    await main()
  File "main.py", line 125, in main
    user_token = cipher_suite.decrypt(str(user_login_token).encode()).decode()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\cryptography\fernet.py", line 86, in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\cryptography\fernet.py", line 122, in _get_unverified_token_data
    raise InvalidToken
cryptography.fernet.InvalidToken


