Traceback (most recent call last):
  File "adam.py", line 33, in <module>
    model = Sequential([
  File "C:\Python38\lib\site-packages\tensorflow\python\trackable\base.py", line 205, in _method_wrapper
    result = method(self, *args, **kwargs)
  File "C:\Python38\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Python38\lib\site-packages\keras\engine\input_spec.py", line 235, in assert_input_compatibility
    raise ValueError(
ValueError: Input 0 of layer "lstm" is incompatible with the layer: expected ndim=3, found ndim=2. Full shape received: (None, 1000)
