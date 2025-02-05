D:\PostgreSQL\17\pgAdmin 4\web>Python pgAdmin4.py
Traceback (most recent call last):
  File "pgAdmin4.py", line 38, in <module>
    import config
  File "D:\PostgreSQL\17\pgAdmin 4\web\config.py", line 33, in <module>
    from pgadmin.utils import env, IS_WIN, fs_short_path
  File "D:\PostgreSQL\17\pgAdmin 4\web\pgadmin\__init__.py", line 24, in <module>
    from flask import Flask, abort, request, current_app, session, url_for
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\flask\__init__.py", line 5, in <module>
    from .app import Flask as Flask
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\flask\app.py", line 34, in <module>
    from . import cli
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\flask\cli.py", line 15, in <module>
    from click.core import ParameterSource
ImportError: cannot import name 'ParameterSource' from 'click.core' (C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\click\core.py)
