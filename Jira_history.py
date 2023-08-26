ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
import librosa
import numpy as np

# Путь к исходному аудио
audio_path = "путь_к_аудио/ваш_аудиофайл.wav"

# Чтение аудио
audio, sr = librosa.load(audio_path, sr=8000, mono=False)

# Применение высокочастотной фильтрации для повышения четкости речи
cutoff_freq = 300  # Задайте желаемую частоту отсечения
b, a = librosa.effects.high_pass_filter(audio[0], sr, cutoff_freq)

# Применение фильтра к аудио
enhanced_audio = np.zeros_like(audio)
for channel_idx in range(audio.shape[0]):
    enhanced_audio[channel_idx] = librosa.effects.preemphasis(
        librosa.lfilter(b, a, audio[channel_idx])
    )

# Сохранение обработанного аудио в новый файл
output_path = "улучшенное_аудио.wav"
librosa.output.write_wav(output_path, enhanced_audio, sr)

print("Улучшенное аудио сохранено:", output_path)

