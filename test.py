Traceback (most recent call last):
  File "test.py", line 11, in <module>
    data.columns = new_columns
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 6002, in __setattr__
    return object.__setattr__(self, name, value)
  File "pandas\_libs\properties.pyx", line 69, in pandas._libs.properties.AxisProperty.__set__
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 730, in _set_axis
    self._mgr.set_axis(axis, labels)
  File "C:\Python38\lib\site-packages\pandas\core\internals\managers.py", line 225, in set_axis
    self._validate_set_axis(axis, new_labels)
  File "C:\Python38\lib\site-packages\pandas\core\internals\base.py", line 70, in _validate_set_axis
    raise ValueError(
ValueError: Length mismatch: Expected axis has 26 elements, new values have 25 elements
