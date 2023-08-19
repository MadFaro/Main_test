  File "Nemo.py", line 22, in <module>
    transcriptions = asr_model.transcribe([audio])
  File "C:\Python38\lib\site-packages\torch\utils\_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "C:\Python38\lib\site-packages\nemo\collections\asr\models\ctc_models.py", line 183, in transcribe
    fp.write(json.dumps(entry) + '\n')
  File "C:\Python38\lib\json\__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "C:\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type ndarray is not JSON serializable
