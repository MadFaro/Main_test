import pandas as pd
from googletrans import Translator
import random

# Загрузка данных из файла
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Выделение текстовых данных и соответствующих им категорий
texts = data['MSG']
categories = data['CATEGORY']

# Инициализация объекта Translator для перевода
translator = Translator()

# Функция для аугментации текста: перевод на английский, испанский и обратно на русский
def augment_text_translate(text):
    # Перевод текста на английский
    translated_en = translator.translate(text, dest='en').text
    # Перевод текста на испанский
    translated_es = translator.translate(translated_en, dest='es').text
    # Перевод текста обратно на русский
    translated_ru = translator.translate(translated_es, dest='ru').text
    return translated_ru

# Список для хранения аугментированных текстов и соответствующих им категорий
augmented_texts = []
augmented_categories = []

# Проход по каждой паре текст-категория и создание аугментированных данных
for text, category in zip(texts, categories):
    # Оригинальный текст и его категория
    augmented_texts.append(text)
    augmented_categories.append(category)
    
    # Аугментация текста: перевод на английский, испанский и обратно на русский
    augmented_text_translate = augment_text_translate(text)
    augmented_texts.append(augmented_text_translate)
    augmented_categories.append(category)

# Создание нового DataFrame с исходными и аугментированными данными
augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

# Сохранение аугментированных данных в новый файл
augmented_data.to_excel("augmented_data.xlsx", index=False)
