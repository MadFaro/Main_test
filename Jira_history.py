Traceback (most recent call last):
  File "2.py", line 5, in <module>
    with wave.open('240002039936997.wav', 'rb') as wav_file:
  File "C:\Python38\lib\wave.py", line 510, in open
    return Wave_read(f)
  File "C:\Python38\lib\wave.py", line 164, in __init__
    self.initfp(f)
  File "C:\Python38\lib\wave.py", line 144, in initfp
    self._read_fmt_chunk(chunk)
  File "C:\Python38\lib\wave.py", line 269, in _read_fmt_chunk
    raise Error('unknown format: %r' % (wFormatTag,))
wave.Error: unknown format: 41216
