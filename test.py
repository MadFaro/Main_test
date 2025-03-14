  File "webim.py", line 551, in <module>                                                                                    schedule.run_pending()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\schedule\__init__.py", line 854, in run_pending                                                                                                               default_scheduler.run_pending()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\schedule\__init__.py", line 101, in run_pending                                                                                                               self._run_job(job)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\schedule\__init__.py", line 173, in _run_job                                                                                                                  ret = job.run()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\schedule\__init__.py", line 691, in run                                                                                                                       ret = self.job_func()
  File "webim.py", line 526, in job
    last_load = get_max_dtm_from_chat()                                                                                   File "webim.py", line 134, in get_max_dtm_from_chat
    cursor.close()
UnboundLocalError: local variable 'cursor' referenced before assignment
