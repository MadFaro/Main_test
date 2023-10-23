
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)

import os
import shutil

# Путь к папке с аудиофайлами
source_folder = "путь_к_вашей_папке_с_аудиофайлами"

# Создаем 10 папок (если они еще не существуют)
for i in range(1, 11):
    folder_name = f"папка_{i}"
    os.makedirs(folder_name, exist_ok=True)

# Получаем список аудиофайлов в исходной папке
audio_files = os.listdir(source_folder)

# Распределяем файлы по 10 папкам равномерно
current_folder_index = 1
for audio_file in audio_files:
    folder_name = f"папка_{current_folder_index}"
    source_path = os.path.join(source_folder, audio_file)
    destination_path = os.path.join(folder_name, audio_file)
    shutil.move(source_path, destination_path)

    # Переходим к следующей папке (циклично)
    current_folder_index = (current_folder_index % 10) + 1

