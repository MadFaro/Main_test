Traceback (most recent call last):
  File "3.py", line 13, in <module>
    data[4] = (data[4] * 1.4).round(0).astype(int)
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 6324, in astype
    new_data = self._mgr.astype(dtype=dtype, copy=copy, errors=errors)
  File "C:\Python38\lib\site-packages\pandas\core\internals\managers.py", line 451, in astype
    return self.apply(
  File "C:\Python38\lib\site-packages\pandas\core\internals\managers.py", line 352, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Python38\lib\site-packages\pandas\core\internals\blocks.py", line 511, in astype
    new_values = astype_array_safe(values, dtype, copy=copy, errors=errors)
  File "C:\Python38\lib\site-packages\pandas\core\dtypes\astype.py", line 242, in astype_array_safe
    new_values = astype_array(values, dtype, copy=copy)
  File "C:\Python38\lib\site-packages\pandas\core\dtypes\astype.py", line 187, in astype_array
    values = _astype_nansafe(values, dtype, copy=copy)
  File "C:\Python38\lib\site-packages\pandas\core\dtypes\astype.py", line 105, in _astype_nansafe
    return _astype_float_to_int_nansafe(arr, dtype, copy)
  File "C:\Python38\lib\site-packages\pandas\core\dtypes\astype.py", line 150, in _astype_float_to_int_nansafe
    raise IntCastingNaNError(
pandas.errors.IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer
