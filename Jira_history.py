
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

from pydub import AudioSegment
import xml.etree.ElementTree as ET

# Загрузите аудиофайл WAV
audio = AudioSegment.from_file("audio.wav")

# Загрузите XML-файл
tree = ET.parse("metadata.xml")
root = tree.getroot()

# Извлеките необходимые метаданные из XML
# Например, если метаданные хранятся в теге <metadata>:
metadata = root.find("metadata").text

# Объедините аудио и метаданные, добавив метаданные в конец аудио
audio_with_metadata = audio + AudioSegment.from_file(BytesIO(metadata.encode("utf-8")))

# Сохраните объединенный файл
audio_with_metadata.export("combined_audio.wav", format="wav")
