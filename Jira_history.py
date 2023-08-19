Traceback (most recent call last):
  File "Nemo.py", line 2, in <module>
    import nemo.collections.asr as nemo_asr
  File "C:\Python38\lib\site-packages\nemo\collections\asr\__init__.py", line 15, in <module>
    from nemo.collections.asr import data, losses, models, modules
  File "C:\Python38\lib\site-packages\nemo\collections\asr\losses\__init__.py", line 15, in <module>
    from nemo.collections.asr.losses.angularloss import AngularSoftmaxLoss
  File "C:\Python38\lib\site-packages\nemo\collections\asr\losses\angularloss.py", line 18, in <module>
    from nemo.core.classes import Loss, Typing, typecheck
  File "C:\Python38\lib\site-packages\nemo\core\__init__.py", line 16, in <module>
    from nemo.core.classes import *
  File "C:\Python38\lib\site-packages\nemo\core\classes\__init__.py", line 20, in <module>
    from nemo.core.classes.common import (
  File "C:\Python38\lib\site-packages\nemo\core\classes\common.py", line 36, in <module>
    from nemo.core.connectors.save_restore_connector import SaveRestoreConnector
  File "C:\Python38\lib\site-packages\nemo\core\connectors\save_restore_connector.py", line 30, in <module>
    from nemo.utils import logging, model_utils
  File "C:\Python38\lib\site-packages\nemo\utils\model_utils.py", line 27, in <module>
    from nemo.utils.data_utils import resolve_cache_dir  # imported for compatibility: model_utils.resolve_cache_dir()
  File "C:\Python38\lib\site-packages\nemo\utils\data_utils.py", line 21, in <module>
    from nemo import __version__ as NEMO_VERSION
ImportError: cannot import name '__version__' from 'nemo' (C:\Python38\lib\site-packages\nemo\__init__.py)

