2024-04-27 18:14:57.087412: W tensorflow/core/framework/op_kernel.cc:1830] OP_REQUIRES failed at serialize_sparse_op.cc:389 : INVALID_ARGUMENT: indices[1] = [0,346] is out of order. Many sparse ops require sorted indices.
    Use `tf.sparse.reorder` to create a correctly ordered copy.


Traceback (most recent call last):
  File "adam.py", line 43, in <module>
    model.fit(X_tfidf, y_encoded, epochs=100, batch_size=32, verbose=1, callbacks=callbacks)
  File "C:\Python38\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Python38\lib\site-packages\tensorflow\python\framework\ops.py", line 7262, in raise_from_not_ok_status
    raise core._status_to_exception(e) from None  # pylint: disable=protected-access
tensorflow.python.framework.errors_impl.InvalidArgumentError: {{function_node __wrapped__SerializeManySparse_device_/job:localhost/replica:0/task:0/device:CPU:0}} indices[1] = [0,346] is out of order. Many sparse ops require sorted indices.
    Use `tf.sparse.reorder` to create a correctly ordered copy.

 [Op:SerializeManySparse]
