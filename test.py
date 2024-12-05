Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pywebio\session\coroutinebased.py", line 325, in step
    coro_yield = self.coro.send(result)
  File "main.py", line 2412, in advt_update
    BotDS.update_advt(advt_id)
  File "C:\Users\TologonovAB\Desktop\shop_app\db.py", line 293, in update_advt
    self.cursor.execute("UPDATE `advt` SET `date_ad` = strftime('%s', 'now', '0 days') WHERE `id` = ?", (id))
ValueError: parameters are of unsupported type
