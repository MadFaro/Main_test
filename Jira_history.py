import glob, vosk, os, nltk, pymorphy2, time
import soundfile as sf
import numpy as np
import pandas as pd




# Получаем весь список файлов их папки
folder_path = r'C:\Users\TologonovAB\Desktop\text\audio\audio'
file_pattern = '*.wav'
file_list = glob.glob(os.path.join(folder_path, file_pattern))

# Загружаем модель и обозначем фразы для поиска
model = vosk.Model('vosk-model-ru-0.22/')
phrases_l = ["выиграть автомобиль", 
             "подарок автомобиль", 
             "приз автомобиль",
             "от банка автомобиль"
             "автомобиль подарок",
             "автомобиль в подарок",
             "автомобиль главный приз",
             "выбрать автомобиль",
             "автомобиль от банка",
             "акция автомобиль",
             "акция машина",
             ]
phrases_r = [""]

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
    results = [] # Пустой словарь для записи
    start_time = time.time() # обозначаем начало выполнения цикла
    audio_data, sample_rate = sf.read(file) # Читаем файл
    left_channel = audio_data[:, 0] # Берем левый канал - то что говорит оператор
    right_channel = audio_data[:, 1] # Берем правый канал - то что говорит клиент

# Выравниваем громкость для левого канала
    max_value_l = np.max(np.abs(left_channel))
    if max_value_l > 0:
        normalize_audio_l = left_channel / max_value_l
    else:
        normalize_audio_l = left_channel

# Выравниваем громкость для правого канала
    max_value_r = np.max(np.abs(right_channel))
    if max_value_r > 0:
        normalize_audio_r = right_channel / max_value_r
    else:
        normalize_audio_r = right_channel

# Сохраняем каналы
    sf.write(f'audio/left/{os.path.basename(file)}', normalize_audio_l, sample_rate) # Сохраняем левый канал
    sf.write(f'audio/right/{os.path.basename(file)}', normalize_audio_r, sample_rate) # Сохраняем правый канал

# Инициализация модели
    recognizer = vosk.KaldiRecognizer(model, sample_rate)

# Прогоняем левый канал через модельку и ищем фразы
    with open(f'audio/left/{os.path.basename(file)}', 'rb') as file_l:
        data_l = file_l.read()
    recognizer.AcceptWaveform(data_l)
    text_l = recognizer.FinalResult()
    found_phrases_l = check_phrases(text_l, phrases_l)

# Прогоняем правый канал через модельку и ищем фразы
    with open(f'audio/right/{os.path.basename(file)}', 'rb') as file_r:
        data_r = file_r.read()
    recognizer.AcceptWaveform(data_r)
    text_r = recognizer.FinalResult()
#    found_phrases_r = check_phrases(text_r, phrases_r)

# Записываем результат в словарь
    end_time = time.time()
    result_time = end_time - start_time
    results.append({
        'audio_file_name': os.path.basename(file), 
        'text_operator': text_l, 
        'found_phrases_operator': found_phrases_l,
        'text_client': text_r, 
#       'found_phrases_client': found_phrases_r,
        'time_second' : result_time   
        })

# Чистим папки с аудио
    os.remove(file)
    os.remove(f'audio/left/{os.path.basename(file)}')
    os.remove(f'audio/right/{os.path.basename(file)}')

# Записываем данные в CSV файл
    df = pd.DataFrame(results)
    df.to_csv('text.csv', mode='a', header=False, index=False, encoding='ANSI', lineterminator='\r\n', sep=';')
