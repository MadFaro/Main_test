import librosa
import numpy as np
import os

input_audio_path = "input_audio.mp3"
output_directory = "output_segments"

# Создаем папку для сегментов, если её нет
os.makedirs(output_directory, exist_ok=True)

segment_duration = 30  # Длительность сегмента в секундах
silence_threshold = 0.01  # Порог амплитуды для определения паузы

# Загружаем аудио
y, sr = librosa.load(input_audio_path, sr=None)

# Находим индексы, где амплитуда меньше порога (паузы)
pause_indices = np.where(y < silence_threshold)[0]

# Создаем сегменты на основе пауз
segments = []
start_idx = 0
for pause_idx in pause_indices:
    if pause_idx - start_idx >= sr * segment_duration:
        segments.append(y[start_idx:pause_idx])
        start_idx = pause_idx + 1

# Сохраняем сегменты
for idx, segment in enumerate(segments):
    output_path = os.path.join(output_directory, f"segment_{idx:03d}.wav")
    librosa.output.write_wav(output_path, segment, sr=sr)

print("Сегментация завершена.")
