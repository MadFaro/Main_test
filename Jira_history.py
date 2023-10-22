
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
import random

# Путь к вашей папке с файлами
source_folder = '/путь/к/вашей/папке'

# Путь к папкам, в которые нужно распределить файлы
destination_folders = ['/путь/к/папке1', '/путь/к/папке2', '/путь/к/папке3', '/путь/к/папке4', '/путь/к/папке5', '/путь/к/папке6', '/путь/к/папке7', '/путь/к/папке8', '/путь/к/папке9', '/путь/к/папке10']

# Получить список файлов в исходной папке
file_list = os.listdir(source_folder)

# Перемешать список файлов в случайном порядке
random.shuffle(file_list)

# Рассчитать, сколько файлов должно быть в каждой папке
files_per_folder = len(file_list) // len(destination_folders)
remainder = len(file_list) % len(destination_folders)

# Создать целевые папки, если они еще не существуют
for folder in destination_folders:
    os.makedirs(folder, exist_ok=True)

# Распределить файлы по папкам и переместить их
for i, folder in enumerate(destination_folders):
    start = i * files_per_folder
    end = (i + 1) * files_per_folder
    if i < remainder:
        end += 1
    for file in file_list[start:end]:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(folder, file)
        shutil.move(source_path, destination_path)

