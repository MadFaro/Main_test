  File "webim.py", line 154, in job
    new_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') - datetime.timedelta(minutes=2)
AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'
