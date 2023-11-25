
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav


import os
import time
import soundfile as sf
import pandas as pd
from multiprocessing import spawn, Manager
from faster_whisper import WhisperModel

def transcribe_worker(file, folder, text_file, results_list):
    model = WhisperModel(model_size_or_path=r"C:\Users\TologonovAB\Desktop\model_wisper\whisper-large-v2",
                         device="cpu", compute_type="float32", cpu_threads=8, num_workers=3)
    
    print(f'Обработка {folder}')
    file_record = os.path.basename(file).split("$")
    start_time = time.time()
    segments, _ = model.transcribe(file, language="ru", task="transcribe", vad_filter=False)
    segments = list(segments)
    df_text = pd.DataFrame.from_dict(segments)
    text = ' '.join(df_text['text'])
    end_time = time.time()
    result_time = end_time - start_time
    results_list.append({
        'id': file_record[0],
        'callid': file_record[1],
        'calltype': file_record[2],
        'networkid': file_record[3],
        'agentname': file_record[4],
        'agentid': file_record[5],
        'text': text,
        'time': result_time
    })
    os.remove(file)
    df = pd.DataFrame(results_list)
    df.to_csv(text_file, mode='a', header=False, index=False, encoding='ANSI', lineterminator='\r\n', sep=';')

def monitor_folder(folder_path, text_file, results_list):
    while True:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                transcribe_worker(file_path, folder_path, text_file, results_list)
        time.sleep(1)

if __name__ == "__main__":
    manager = Manager()
    results_list1 = manager.list()
    results_list2 = manager.list()
    results_list3 = manager.list()

    folder1 = r'C:\Users\TologonovAB\Desktop\ASR_W\1'
    file1 = r'C:\Users\TologonovAB\Desktop\ASR_W\text1.csv'
    folder2 = r'C:\Users\TologonovAB\Desktop\ASR_W\2'
    file2 = r'C:\Users\TologonovAB\Desktop\ASR_W\text2.csv'
    folder3 = r'C:\Users\TologonovAB\Desktop\ASR_W\3'
    file3 = r'C:\Users\TologonovAB\Desktop\ASR_W\text3.csv'

    spawn.Process(target=monitor_folder, args=(folder1, file1, results_list1)).start()
    spawn.Process(target=monitor_folder, args=(folder2, file2, results_list2)).start()
    spawn.Process(target=monitor_folder, args=(folder3, file3, results_list3)).start()
