import soundfile as sf
import numpy as np

# Загрузка аудио данных
audio_data, sample_rate = sf.read(file)
left_channel = audio_data[:, 0]
right_channel = audio_data[:, 1]

# Нормализация каналов
max_value_l = np.max(np.abs(left_channel))
normalize_audio_l = left_channel / max_value_l if max_value_l > 0 else left_channel

max_value_r = np.max(np.abs(right_channel))
normalize_audio_r = right_channel / max_value_r if max_value_r > 0 else right_channel

# Объединение нормализованных каналов обратно
normalized_audio_data = np.column_stack((normalize_audio_l, normalize_audio_r))

# Сохранение аудио данных в том же формате
output_file = "normalized_audio.wav"
sf.write(output_file, normalized_audio_data, sample_rate)
