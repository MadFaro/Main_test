
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
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
