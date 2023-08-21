from pyAudioAnalysis import audioBasicIO, audioSegmentation
import soundfile as sf

# Загрузка аудиофайла
audio_file = 'путь_к_вашему_аудиофайлу.wav'
signal, sample_rate, _ = audioBasicIO.read_audio_file(audio_file)

# Выполнение VAD
segments = audioSegmentation.silence_removal(signal, sample_rate, 0.02, 0.02, smooth_window=1.0, weight=0.3)

# Создание нового аудиофайла без пауз
filtered_signal = []
for segment in segments:
    start_sample = int(segment[0] * sample_rate)
    end_sample = int(segment[1] * sample_rate)
    filtered_signal.extend(signal[start_sample:end_sample])

# Сохранение отфильтрованных данных в новый аудиофайл
output_file = 'путь_к_вашему_выходному_аудиофайлу.wav'
sf.write(output_file, filtered_signal, sample_rate)
