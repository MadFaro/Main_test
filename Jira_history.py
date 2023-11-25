
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav



  File "C:\Program Files\Python38\lib\multiprocessing\process.py", line 313, in _bootstrap
    self.run()
  File "C:\Program Files\Python38\lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\TologonovAB\Desktop\ASR_W\main.py", line 40, in monitor_folder
    transcribe_worker(file_path, folder_path, text_file, results_list)
  File "C:\Users\TologonovAB\Desktop\ASR_W\main.py", line 21, in transcribe_worker
    results_list.append({
  File "<string>", line 2, in append
  File "C:\Program Files\Python38\lib\multiprocessing\managers.py", line 831, in _callmethod
    self._connect()
  File "C:\Program Files\Python38\lib\multiprocessing\managers.py", line 818, in _connect
    conn = self._Client(self._token.address, authkey=self._authkey)
  File "C:\Program Files\Python38\lib\multiprocessing\connection.py", line 500, in Client
    c = PipeClient(address)
  File "C:\Program Files\Python38\lib\multiprocessing\connection.py", line 701, in PipeClient
    _winapi.WaitNamedPipe(address, 1000)
FileNotFoundError: [WinError 2] Не удается найти указанный файл
