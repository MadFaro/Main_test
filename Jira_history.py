Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\sklearn\utils\_encode.py", line 224, in _encode
    return _map_to_integer(values, uniques)
  File "C:\Python38\lib\site-packages\sklearn\utils\_encode.py", line 164, in _map_to_integer
    return np.array([table[v] for v in values])
  File "C:\Python38\lib\site-packages\sklearn\utils\_encode.py", line 164, in <listcomp>
    return np.array([table[v] for v in values])
  File "C:\Python38\lib\site-packages\sklearn\utils\_encode.py", line 158, in __missing__
    raise KeyError(key)
KeyError: '   РБ_Подключение_Уралсиб-Бонус'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "adam.py", line 26, in <module>
    y_test_encoded = label_encoder.transform(y_test)
  File "C:\Python38\lib\site-packages\sklearn\utils\_set_output.py", line 140, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Python38\lib\site-packages\sklearn\preprocessing\_label.py", line 139, in transform
    return _encode(y, uniques=self.classes_)
  File "C:\Python38\lib\site-packages\sklearn\utils\_encode.py", line 226, in _encode
    raise ValueError(f"y contains previously unseen labels: {str(e)}")
ValueError: y contains previously unseen labels: '   РБ_Подключение_Уралсиб-Бонус'
