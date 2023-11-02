
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
ffmpeg -i audio.wav -f ffmetadata -i metadata.xml -map_metadata 1 -c:v copy output.wav

import os
import subprocess
import xml.etree.ElementTree as ET

# Путь к папке "аудио"
audio_folder = 'путь_к_папке_аудио'
output_folder = 'путь_к_папке_аудио2'

# Рекурсивно обойти все подпапки
for root, dirs, files in os.walk(audio_folder):
    for file in files:
        if file.endswith('.wav'):
            wav_file = os.path.join(root, file)
            xml_file = os.path.join(root, file.replace('.wav', '.xml'))

            # Проверка наличия XML-файла с таким же именем
            if os.path.isfile(xml_file):
                # Парсинг XML-файла
                tree = ET.parse(xml_file)
                root = tree.getroot()

                # Извлекаем необходимые данные из XML
                timestamp = root.find(".//x:tag[@x:taggedbycomponent='IFServices']/@x:timestamp", namespaces={'x': 'http://www.verint.com/xmlns/recording20080320'}).get("x:timestamp")
                calltype = root.find(".//x:tag[@x:taggedbycomponent='IFServices']/x:attribute[@x:key='calltype']", namespaces={'x': 'http://www.verint.com/xmlns/recording20080320'}).text
                ani = root.find(".//x:session/x:ani", namespaces={'x': 'http://www.verint.com/xmlns/recording20080320'}).text
                agentname = root.find(".//x:tag[@x:taggedbycomponent='IFServices']/x:attribute[@x:key='agentname']", namespaces={'x': 'http://www.verint.com/xmlns/recording20080320'}).text
                agentid = root.find(".//x:tag[@x:taggedbycomponent='IFServices']/x:attribute[@x:key='agentid']", namespaces={'x': 'http://www.verint.com/xmlns/recording20080320'}).text

                # Формируем новое имя файла
                new_filename = f"{timestamp}|{calltype}|{ani}|{agentname}|{agentid}.wav"
                output_file = os.path.join(output_folder, new_filename)

                # Используем FFmpeg для объединения аудио и метаданных
                cmd = [
                    'ffmpeg',
                    '-i', wav_file,
                    '-f', 'ffmetadata',
                    '-i', xml_file,
                    '-map_metadata', '1',
                    '-c:v', 'copy',
                    output_file
                ]
                subprocess.run(cmd)

print('Объединение завершено.')

