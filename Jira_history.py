import pandas as pd
from googletrans import Translator

# Загрузка данных из файла
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Выделение текстовых данных и соответствующих им категорий
texts = data['MSG']
categories = data['CATEGORY']

# Инициализация объекта Translator для перевода
translator = Translator()

# Функция для перевода текста на три языка поочередно
def translate_text(text):
    # Перевод текста на английский
    translated_en = translator.translate(text, dest='en').text
    # Перевод текста на испанский
    translated_es = translator.translate(translated_en, dest='es').text
    # Перевод текста обратно на русский
    translated_ru = translator.translate(translated_es, dest='ru').text
    return translated_ru

# Функция для разбиения текста на части, если он превышает 5000 символов
def split_text(text, max_chars=5000):
    if len(text) <= max_chars:
        return [text]
    else:
        return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

# Список для хранения аугментированных текстов и соответствующих им категорий
augmented_texts = []
augmented_categories = []

# Проход по каждой паре текст-категория и создание аугментированных данных
for text, category in zip(texts, categories):
    # Оригинальный текст и его категория
    augmented_texts.append(text)
    augmented_categories.append(category)
    
    # Проверка длины текста и его перевод на три языка поочередно
    if len(text) > 5000:
        # Разбиение текста на части и их перевод
        translated_parts = []
        for part in split_text(text):
            translated_part = translate_text(part)
            translated_parts.append(translated_part)
        augmented_text_translate = ''.join(translated_parts)
    else:
        # Перевод текста на три языка поочередно
        augmented_text_translate = translate_text(text)
    
    # Добавление аугментированного текста и его категории в список
    augmented_texts.append(augmented_text_translate)
    augmented_categories.append(category)

# Создание нового DataFrame с исходными и аугментированными данными
augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

# Сохранение аугментированных данных в новый файл
augmented_data.to_excel("augmented_data.xlsx", index=False)
