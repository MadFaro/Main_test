
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav



from faster_whisper import WhisperModel
import pandas as pd
import time
import glob, os


folder_path = r'C:\Users\TologonovAB\Desktop\model_wisper\move'
file_pattern = '*.wav'
file_list = glob.glob(os.path.join(folder_path, file_pattern))

model = WhisperModel(model_size_or_path=r"C:\Users\TologonovAB\Desktop\model_wisper\whisper-int8-2", device='cpu', cpu_threads=4)

for file in file_list:
    file_record = os.path.basename(file).split("$")
    results = []
    start_time = time.time()
    segments, _ = model.transcribe(file, language="ru", task="transcribe", vad_filter = False)
    segments = list(segments)
    df_text = pd.DataFrame.from_dict(segments)
    if df_text.empty:
        text = ''
    else:
        text = ' '.join(df_text['text'])
    end_time = time.time()
    result_time = end_time - start_time
    results.append({
            'id': file_record[0],
            'callid': file_record[1],
            'calltype': file_record[2],
            'networkid': file_record[3],
            'agentname': file_record[4],
            'agentid': file_record[5],
            'text': text,
            'time' : result_time   
                })
    os.remove(file)
    df = pd.DataFrame(results)
    df.to_csv('text1.csv', mode='a', header=False, index=False, encoding='ANSI', lineterminator='\r\n', sep=';')

