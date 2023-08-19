import nemo
import nemo.collections.asr as nemo_asr
import os

# Путь к аудиофайлу
audio_file = 'путь_к_аудиофайлу.wav'

# Путь к сохраненной модели
model_checkpoint = 'путь_к_сохраненной_модели.nemo'

# Инициализация NeMo ASR модели с использованием сохраненной модели
asr_model = nemo_asr.models.EncDecCTCModel.restore_from(model_checkpoint)

# Загрузка аудиофайла
if os.path.exists(audio_file):
    audio, _ = librosa.load(audio_file, sr=16000)
else:
    print("Аудиофайл не найден.")
    exit(1)

# Преобразование аудио в текст
transcriptions = asr_model.transcribe([audio])

# Вывод результата
print("Распознанный текст:", transcriptions[0])

