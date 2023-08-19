import librosa
from pydub import AudioSegment

# Путь к вашему аудиофайлу
audio_file_path = 'path_to_your_audio_file.wav'

# Значение порога длительности паузы в секундах
pause_threshold = 0.5

# Загрузка аудиофайла и преобразование в формат, понятный librosa
audio = AudioSegment.from_file(audio_file_path)
samples = audio.raw_data
sample_rate = audio.frame_rate

# Обнаружение временных точек начала голосовых фрагментов
samples, sample_rate = librosa.load(audio_file_path, sr=None)
onset_frames = librosa.onset.onset_detect(y=samples, sr=sample_rate)

# Путь к папке для сохранения результатов
output_path = 'output_directory/'

# Создание отдельных аудиофайлов для каждого голосового фрагмента
for i in range(len(onset_frames) - 1):
    start_sample = librosa.frames_to_samples(onset_frames[i])
    end_sample = librosa.frames_to_samples(onset_frames[i + 1])
    
    segment = AudioSegment(
        data=samples[start_sample:end_sample],
        sample_width=audio.sample_width,
        frame_rate=sample_rate,
        channels=audio.channels
    )
    
    if len(segment) > pause_threshold * 1000:  # Исключаем короткие паузы
        segment.export(f'{output_path}segment_{i + 1}.wav', format='wav')
