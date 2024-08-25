Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 197, in callback_coro
    res = callback(event['data'])
  File "C:\Python38\lib\site-packages\pywebio\output.py", line 839, in click_callback
    return onclick[btn_idx]()
  File "main.py", line 202, in <lambda>
    None if df.empty else put_widget(css.tpl, data={"contents": put_button("", onclick=lambda: popup("Уведомления" [put_html(df.to_html(index=False))]), color='light', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')}).style("margin: auto;"),
TypeError: string indices must be integers
