  File "2.py", line 5, in <module>
    data, _ = soundfile.read('240002039936997.wav', channels=2, samplerate=8000)
  File "C:\Python38\lib\site-packages\soundfile.py", line 285, in read
    with SoundFile(file, 'r', samplerate, channels,
  File "C:\Python38\lib\site-packages\soundfile.py", line 656, in __init__
    self._info = _create_info_struct(file, mode, samplerate, channels,
  File "C:\Python38\lib\site-packages\soundfile.py", line 1483, in _create_info_struct
    raise TypeError("Not allowed for existing files (except 'RAW'): "
TypeError: Not allowed for existing files (except 'RAW'): samplerate, channels, format, subtype, endian
