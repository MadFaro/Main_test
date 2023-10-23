
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

# Список конкретных папок, в которые вы хотите распределить файлы
destination_folders = [
    "путь_к_папке_1",
    "путь_к_папке_2",
    "путь_к_папке_3",
    "путь_к_папке_4",
    "путь_к_папке_5",
    "путь_к_папке_6",
    "путь_к_папке_7",
    "путь_к_папке_8",
    "путь_к_папке_9",
    "путь_к_папке_10",
]

# Получаем список аудиофайлов в исходной папке
audio_files = os.listdir(source_folder)

# Распределяем файлы равномерно по заданным папкам
folder_index = 0
for audio_file in audio_files:
    destination_path = os.path.join(destination_folders[folder_index], audio_file)
    source_path = os.path.join(source_folder, audio_file)
    shutil.move(source_path, destination_path)

    # Переходим к следующей папке (циклично)
    folder_index = (folder_index + 1) % 10


