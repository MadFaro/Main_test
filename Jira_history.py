
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
import time
from multiprocessing import Process

# Функция для обработки файла
def process_file(file_path):
    # Ваш код для обработки файла здесь

# Функция для мониторинга папки
def monitor_folder(folder_path):
    while True:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                process_file(file_path)
        time.sleep(1)  # Измените значение по желанию

if __name__ == '__main':
    folder1 = 'путь_к_папке_1'
    folder2 = 'путь_к_папке_2'

    process1 = Process(target=monitor_folder, args=(folder1,))
    process2 = Process(target=monitor_folder, args=(folder2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
