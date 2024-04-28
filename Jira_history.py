  File "adam.py", line 81, in <module>
    loss, accuracy = model.evaluate(X_test_tfidf, y_test_encoded, verbose=0)
  File "C:\Program Files\Python38\lib\site-packages\keras\src\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Program Files\Python38\lib\site-packages\tensorflow\python\framework\ops.py", line 6656, in raise_from_not_ok_status
    raise core._status_to_exception(e) from None  # pylint: disable=protected-access
tensorflow.python.framework.errors_impl.InvalidArgumentError: {{function_node __wrapped__SerializeManySparse_device_/job:localhost/replica:0/task:0/device:CPU:0}} indices[1] = [0,4766] is out of order. Many sparse ops require sorted indices.
    Use `tf.sparse.reorder` to create a correctly ordered copy.

 [Op:SerializeManySparse] name:
