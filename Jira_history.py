import wave
import numpy as np

# Открываем WAV-файл для чтения
with wave.open('your_file.wav', 'rb') as wav_file:
    # Используем стандартные предположения
    num_channels = 2  # Стерео
    sample_width = 2  # 16 бит
    frame_rate = 44100  # 44.1 кГц

    # Чтение аудио данных
    audio_data = bytearray()
    chunk_size = 4096  # Размер блока для чтения

    while True:
        chunk = wav_file.readframes(chunk_size)
        if not chunk:
            break
        audio_data.extend(chunk)

# Преобразовываем байты в массив numpy
audio_data = np.frombuffer(audio_data, dtype=np.int16)

# Переформатируем данные в массив с двумя каналами
num_samples = len(audio_data) // num_channels
audio_data = np.reshape(audio_data, (num_samples, num_channels))

# В этом месте вы можете работать с переменной audio_data,
# которая содержит числовые данные аудио с предполагаемыми параметрами
