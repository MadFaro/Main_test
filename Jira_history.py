
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

    X_pred['predictions'] = abs(predictions) * X_pred['day'].apply(lambda x: 1.10 if x == 1 else 1)
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 2016, in __array_ufunc__
    return arraylike.array_ufunc(self, ufunc, method, *inputs, **kwargs)
  File "C:\Python38\lib\site-packages\pandas\core\arraylike.py", line 273, in array_ufunc
    result = maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
  File "pandas\_libs\ops_dispatch.pyx", line 113, in pandas._libs.ops_dispatch.maybe_dispatch_ufunc_to_dunder_op
  File "C:\Python38\lib\site-packages\pandas\core\ops\common.py", line 81, in new_method
    return method(self, other)
  File "C:\Python38\lib\site-packages\pandas\core\arraylike.py", line 206, in __rmul__
    return self._arith_method(other, roperator.rmul)
  File "C:\Python38\lib\site-packages\pandas\core\series.py", line 6108, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Python38\lib\site-packages\pandas\core\base.py", line 1350, in _arith_method
    return self._construct_result(result, name=res_name)
  File "C:\Python38\lib\site-packages\pandas\core\series.py", line 3101, in _construct_result
    out = self._constructor(result, index=self.index, dtype=dtype)
  File "C:\Python38\lib\site-packages\pandas\core\series.py", line 509, in __init__
    data = sanitize_array(data, index, dtype, copy)
  File "C:\Python38\lib\site-packages\pandas\core\construction.py", line 607, in sanitize_array
    subarr = _sanitize_ndim(subarr, data, dtype, index, allow_2d=allow_2d)
  File "C:\Python38\lib\site-packages\pandas\core\construction.py", line 666, in _sanitize_ndim
    raise ValueError(
ValueError: Data must be 1-dimensional, got ndarray of shape (1464, 1464) instead
