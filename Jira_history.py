import librosa

# Путь к вашему аудиофайлу
audio_file_path = 'path_to_your_audio_file.wav'

# Значение порога длительности паузы в секундах
pause_threshold = 0.5

# Загрузка аудиофайла с помощью librosa
samples, sample_rate = librosa.load(audio_file_path, sr=None)

# Обнаружение временных точек начала голосовых фрагментов
onset_frames = librosa.onset.onset_detect(y=samples, sr=sample_rate)

# Путь к папке для сохранения результатов
output_path = 'output_directory/'

# Создание отдельных аудиофайлов для каждого голосового фрагмента
for i in range(len(onset_frames) - 1):
    start_sample = librosa.frames_to_samples(onset_frames[i])
    end_sample = librosa.frames_to_samples(onset_frames[i + 1])
    
    segment = samples[start_sample:end_sample]
    
    if len(segment) > int(pause_threshold * sample_rate):  # Исключаем короткие паузы
        librosa.output.write_wav(f'{output_path}segment_{i + 1}.wav', segment, sample_rate)

