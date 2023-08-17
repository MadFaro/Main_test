import wave
import numpy as np

# Открываем WAV-файл для чтения
with wave.open('your_file.wav', 'rb') as wav_file:
    # Используем стандартные предположения, если заголовки недоступны
    num_channels = 2  # Стерео
    sample_width = 2  # 16 бит
    frame_rate = 44100  # 44.1 кГц
    num_frames = wav_file.getnframes()

    # Чтение аудио данных
    audio_data = np.frombuffer(wav_file.readframes(num_frames), dtype=np.int16)

# Переформатируем данные в массив с двумя каналами
audio_data = np.reshape(audio_data, (num_frames, num_channels))

# В этом месте вы можете работать с переменной audio_data,
# которая содержит числовые данные аудио с предполагаемыми параметрами

