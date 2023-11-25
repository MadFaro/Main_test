
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav


Traceback (most recent call last):
  File "main.py", line 59, in <module>
    process1.start()
  File "C:\Program Files\Python38\lib\multiprocessing\process.py", line 121, in start
    self._popen = self._Popen(self)
  File "C:\Program Files\Python38\lib\multiprocessing\context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "C:\Program Files\Python38\lib\multiprocessing\context.py", line 326, in _Popen
    return Popen(process_obj)
  File "C:\Program Files\Python38\lib\multiprocessing\popen_spawn_win32.py", line 93, in __init__
    reduction.dump(process_obj, to_child)
  File "C:\Program Files\Python38\lib\multiprocessing\reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
TypeError: cannot pickle 'ctranslate2._ext.Whisper' object

C:\Users\TologonovAB\Desktop\ASR_W>Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "C:\Program Files\Python38\lib\multiprocessing\spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "C:\Program Files\Python38\lib\multiprocessing\spawn.py", line 126, in _main
    self = reduction.pickle.load(from_parent)
EOFError: Ran out of input
