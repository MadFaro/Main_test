  File "3.py", line 10, in <module>
    data[4] = data[4] * 1.4
  File "C:\Python38\lib\site-packages\pandas\core\ops\common.py", line 81, in new_method
    return method(self, other)
  File "C:\Python38\lib\site-packages\pandas\core\arraylike.py", line 202, in __mul__
    return self._arith_method(other, operator.mul)
  File "C:\Python38\lib\site-packages\pandas\core\series.py", line 6108, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Python38\lib\site-packages\pandas\core\base.py", line 1348, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "C:\Python38\lib\site-packages\pandas\core\ops\array_ops.py", line 232, in arithmetic_op
    res_values = _na_arithmetic_op(left, right, op)  # type: ignore[arg-type]
  File "C:\Python38\lib\site-packages\pandas\core\ops\array_ops.py", line 178, in _na_arithmetic_op
    result = _masked_arith_op(left, right, op)
  File "C:\Python38\lib\site-packages\pandas\core\ops\array_ops.py", line 135, in _masked_arith_op
    result[mask] = op(xrav[mask], y)
TypeError: can't multiply sequence by non-int of type 'float'
