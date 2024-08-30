Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 1613, in dashboard_user
    chart = create_login_chart(dates, cnt_login)
  File "main.py", line 1556, in create_login_chart
    p = figure(x_range=dates, title="Входы", plot_width=800, plot_height=400,
  File "C:\Python38\lib\site-packages\bokeh\plotting\_figure.py", line 190, in __init__
    self._raise_attribute_error_with_matches(name, names | opts.properties())
  File "C:\Python38\lib\site-packages\bokeh\core\has_props.py", line 368, in _raise_attribute_error_with_matches
    raise AttributeError(f"unexpected attribute {name!r} to {self.__class__.__name__}, {text} attributes are {nice_join(matches)}")
AttributeError: unexpected attribute 'plot_width' to figure, similar attributes are outer_width, width or min_width
