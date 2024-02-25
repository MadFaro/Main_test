<<<<<<< HEAD
﻿import vosk
import soundfile as sf
import numpy as np
import os
import concurrent.futures
import nltk
=======
>>>>>>> 5a99c49780f4d72714c4a0e85adf433fdafb12d8

ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
<<<<<<< HEAD


<<<<<<< HEAD
def process_audio_file(audio_file, model, phrases):
    audio_data, sample_rate = load_audio_data(audio_file)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)
    recognizer.AcceptWaveform(audio_data)
    result = recognizer.FinalResult()
    text = result['text']
    check_phrases(text, phrases)
    return {'audio_file': audio_file, 'text': text, 'found_phrases': check_phrases(text, phrases)}

def find_words(audio_files, model, phrases):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for audio_file in audio_files:
            future = executor.submit(process_audio_file, audio_file, model, phrases)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
    return results

if __name__ == '__main__':
    model = vosk.Model(model_path)
    audio_files = [os.path.join(audio_directory, filename) for filename in os.listdir(audio_directory) if filename.endswith('.wav')]
    phrases = ["пример текста", "мы будем", "не найдена"]
    found_words = find_words(audio_files, model, phrases)
    print(found_words)
=======
=======
>>>>>>> e1c8318d39fbc1d169083fff24a8b797a0e32883
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
<<<<<<< HEAD
ffmpeg -i output3.wav -af "crystalizer" output4.wav

audacity -nq -t "input.wav" --effect=Amplify:factor=2.0

import json
import os

# Инициализация пустого списка для результатов
results = []

for file in your_files:  # Замените на вашу итерацию по файлам
    left_channel_output_data = ...
    right_channel_output_data = ...
    dialog = ...
    result_time = ...

<<<<<<< HEAD
SELECT TRUNC(SYSDATE, 'HH24') + (FLOOR((TO_NUMBER(TO_CHAR(SYSDATE, 'MI')) / 30)) * (1/48)) AS rounded_date
FROM dual;
>>>>>>> 5a99c49780f4d72714c4a0e85adf433fdafb12d8
=======
    # Добавление результатов в список
    results.append({
        'audio_file_name': os.path.basename(file),
        'text_operator': left_channel_output_data["text"],
        'text_client': right_channel_output_data["text"],
        'text_join': dialog,
        'time_second': result_time
    })

    # Открываем JSON файл для дозаписи
    with open('text.json', 'a', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False)
        json_file.write('\n')  # Разделитель для каждой итерации
            
import json
import pandas as pd

# Открываем файл JSON и загружаем данные
with open('text.json', 'r', encoding='utf-8') as json_file:
    data = [json.loads(line) for line in json_file]

# data теперь представляет собой список словарей
# Преобразуем его в датафрейм
df = pd.DataFrame(data)
>>>>>>> e1c8318d39fbc1d169083fff24a8b797a0e32883
=======
ffmpeg -i output3.wav -af "crystalizer" output4.wav  
>>>>>>> 9c477e2e459e8d71114d7c3a1906719b4b897b66
