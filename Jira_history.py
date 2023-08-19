import glob
import os
import soundfile as sf
from pydub import AudioSegment
from scipy import signal
import vosk
import pymorphy2
import nltk
import numpy as np
import pandas as pd
import time

# Получаем весь список файлов из папки
folder_path = r'C:\Users\TologonovAB\Desktop\text\audio\audio'
file_pattern = '*.wav'
file_list = glob.glob(os.path.join(folder_path, file_pattern))

# Загрузка модели vosk
model = vosk.Model('vosk-model-ru-0.22/')
phrases_l = ["выиграть автомобиль", "подарок автомобиль", "приз автомобиль", "от банка автомобиль", "автомобиль подарок", "автомобиль в подарок", "автомобиль главный приз", "выбрать автомобиль", "автомобиль от банка", "акция автомобиль", "акция машина"]

# Функция для поиска фраз
def check_phrases(text, phrases):
    normal = pymorphy2.MorphAnalyzer()
    tokens = nltk.word_tokenize(text)
    normal_tokens = [normal.parse(token)[0].normal_form for token in tokens]
    found_phrases = []
    for phrase in phrases:
        phrase_tokens = nltk.word_tokenize(phrase)
        normal_phrase = [normal.parse(token)[0].normal_form for token in phrase_tokens]
        if all(token in normal_tokens for token in normal_phrase):
            found_phrases.append(phrase)
    return found_phrases

# Запускаем основной цикл
for file in file_list:
    results = [] # Пустой список для результатов
    start_time = time.time() # Начало замера времени

    # Чтение аудиофайла
    audio_data, sample_rate = sf.read(file)
    
    # Разбиение на два канала
    left_channel = audio_data[:, 0]
    right_channel = audio_data[:, 1]

    # Фильтрация высоких и низких частот для левого канала
    cutoff_low = 300
    cutoff_high = 3000
    b, a = signal.butter(4, [cutoff_low, cutoff_high], btype="band", fs=sample_rate)
    filtered_audio_l = signal.lfilter(b, a, left_channel)

    # Фильтрация высоких и низких частот для правого канала
    filtered_audio_r = signal.lfilter(b, a, right_channel)

    # Скорректировать скорость воспроизведения
    speed_change = 1 / speed_change
    adjusted_audio_l = AudioSegment(
        data=filtered_audio_l.tobytes(),
        frame_rate=int(sample_rate * speed_change),
        sample_width=filtered_audio_l.dtype.itemsize,
        channels=1
    )

    adjusted_audio_r = AudioSegment(
        data=filtered_audio_r.tobytes(),
        frame_rate=int(sample_rate * speed_change),
        sample_width=filtered_audio_r.dtype.itemsize,
        channels=1
    )

    # Инициализация модели vosk для левого канала
    recognizer_l = vosk.KaldiRecognizer(model, int(sample_rate * speed_change))
    recognizer_l.AcceptWaveform(adjusted_audio_l.raw_data)
    text_l = recognizer_l.FinalResult()
    found_phrases_l = check_phrases(text_l, phrases_l)

    # Инициализация модели vosk для правого канала
    recognizer_r = vosk.KaldiRecognizer(model, int(sample_rate * speed_change))
    recognizer_r.AcceptWaveform(adjusted_audio_r.raw_data)
    text_r = recognizer_r.FinalResult()

    end_time = time.time()
    result_time = end_time - start_time

    results.append({
        'audio_file_name': os.path.basename(file),
        'text_operator': text_l,
        'found_phrases_operator': found_phrases_l,
        'text_client': text_r,
        'time_second': result_time
    })

    # Запись данных в CSV-файл
    df = pd.DataFrame(results)
    df.to_csv('text.csv', mode='a', header=False, index=False, encoding='ANSI', lineterminator='\r\n', sep=';')

print("Обработка и транскрибация завершены.")
