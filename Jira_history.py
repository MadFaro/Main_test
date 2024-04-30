import pandas as pd
import random
from faker import Faker

# Загрузка данных из файла
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Выделение текстовых данных и соответствующих им категорий
texts = data['MSG']
categories = data['CATEGORY']

# Инициализация Faker для генерации случайных слов
faker = Faker()

# Функция для случайной замены слов в тексте
def augment_text_replace(text, p=0.1):
    words = text.split()
    augmented_words = []
    for word in words:
        if random.random() < p:
            # Замена слова на случайное слово от Faker
            augmented_word = faker.word()
            augmented_words.append(augmented_word)
        else:
            augmented_words.append(word)
    return ' '.join(augmented_words)

# Список для хранения аугментированных текстов и соответствующих им категорий
augmented_texts = []
augmented_categories = []

# Проход по каждой паре текст-категория и создание аугментированных данных
for text, category in zip(texts, categories):
    # Оригинальный текст и его категория
    augmented_texts.append(text)
    augmented_categories.append(category)
    
    # Аугментация текста: случайная замена слов и добавление в список аугментированных данных
    augmented_text_replace = augment_text_replace(text)
    augmented_texts.append(augmented_text_replace)
    augmented_categories.append(category)

# Создание нового DataFrame с исходными и аугментированными данными
augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

# Сохранение аугментированных данных в новый файл
augmented_data.to_excel("augmented_data.xlsx", index=False)
