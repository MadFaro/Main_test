
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Program Files\Python38\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "C:\Program Files\Python38\lib\threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "main_punc.py", line 34, in monitor_folder
    process_file(file_path, folder_path)
  File "main_punc.py", line 64, in process_file
    BotDS.add_log(
  File "C:\Users\TologonovAB\Desktop\ASR\db.py", line 10, in add_log
    self.cursor.execute("INSERT INTO `transcrib` (`callid`, `networkid`, `agentname`, `agentid`, `text_oper`, `text_client`, `time`, `date_time`) VALUES (?,?,?,?,?,?,?,?,?,?)", (callid, networkid, agentname, agentid, text_oper, text_client, time, date_time))
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 9960 and this is thread id 10664.
