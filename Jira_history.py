import nemo
import nemo.collections.asr as nemo_asr
import json
import librosa
import os

# Путь к сохраненной модели
model_checkpoint = 'путь_к_сохраненной_модели.nemo'

# Инициализация NeMo ASR модели с использованием сохраненной модели
asr_model = nemo_asr.models.EncDecCTCModel.restore_from(model_checkpoint)

# Путь к аудиофайлу
audio_file = 'путь_к_аудиофайлу.wav'

# Загрузка аудиофайла
if os.path.exists(audio_file):
    audio, _ = librosa.load(audio_file, sr=16000)
else:
    print("Аудиофайл не найден.")
    exit(1)

# Преобразование массива NumPy в список Python
audio_list = audio.tolist()

# Распознавание речи
transcriptions = asr_model.transcribe([audio_list])

# Сохранение результатов в JSON
output_file = 'результат.json'
with open(output_file, 'w') as f:
    json.dump(transcriptions, f)

print("Результаты сохранены в", output_file)
