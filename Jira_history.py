import soundfile as sf
import numpy as np

# Загрузка аудио данных
audio_data, sample_rate = sf.read(file)
left_channel = audio_data[:, 0]
right_channel = audio_data[:, 1]

# RMS нормализация для левого канала
rms_left = np.sqrt(np.mean(left_channel**2))
normalized_audio_l = left_channel / rms_left

# RMS нормализация для правого канала
rms_right = np.sqrt(np.mean(right_channel**2))
normalized_audio_r = right_channel / rms_right

# Объединение нормализованных каналов обратно
normalized_audio_data = np.column_stack((normalized_audio_l, normalized_audio_r))

# Сохранение аудио данных в том же формате
output_file = "normalized_audio.wav"
sf.write(output_file, normalized_audio_data, sample_rate)
