import soundfile as sf
data, _ = sf.read('240002039934923.wav', channels=2, samplerate=8000)

print(data)

Traceback (most recent call last):
  File "1.py", line 6, in <module>
    data, _ = sf.read('240002039934923.wav', channels=2, samplerate=8000)
  File "C:\Python38\lib\site-packages\soundfile.py", line 285, in read
    with SoundFile(file, 'r', samplerate, channels,
  File "C:\Python38\lib\site-packages\soundfile.py", line 656, in __init__
    self._info = _create_info_struct(file, mode, samplerate, channels,
  File "C:\Python38\lib\site-packages\soundfile.py", line 1483, in _create_info_struct
    raise TypeError("Not allowed for existing files (except 'RAW'): "
TypeError: Not allowed for existing files (except 'RAW'): samplerate, channels, format, subtype, endian

