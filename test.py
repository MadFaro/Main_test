Traceback (most recent call last):
  File "test.py", line 12, in <module>
    data = data.applymap(lambda x: int(x) if pd.notnull(x) else 0)
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 9518, in applymap
    return self.apply(infer).__finalize__(self, "applymap")
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 9433, in apply
    return op.apply().__finalize__(self, method="apply")
  File "C:\Python38\lib\site-packages\pandas\core\apply.py", line 678, in apply
    return self.apply_standard()
  File "C:\Python38\lib\site-packages\pandas\core\apply.py", line 798, in apply_standard
    results, res_index = self.apply_series_generator()
  File "C:\Python38\lib\site-packages\pandas\core\apply.py", line 814, in apply_series_generator
    results[i] = self.f(v)
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 9516, in infer
    return lib.map_infer(x.astype(object)._values, func, ignore_na=ignore_na)
  File "pandas\_libs\lib.pyx", line 2834, in pandas._libs.lib.map_infer
  File "test.py", line 12, in <lambda>
    data = data.applymap(lambda x: int(x) if pd.notnull(x) else 0)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'Timestamp'
