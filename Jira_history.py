import pandas as pd
import nlpaug.augmenter.word as naw
import random

# Загрузка данных из файла
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Выделение текстовых данных и соответствующих им категорий
texts = data['MSG']
categories = data['CATEGORY']

# Функция для аугментации текста: случайное удаление слов
def augment_text_delete(text, p=0.1):
    words = text.split()
    # Определение количества слов, которые нужно удалить
    num_delete = max(1, int(len(words) * p))
    # Случайное удаление слов
    words = [word for word in words if random.random() > p]
    return ' '.join(words)

# Функция для аугментации текста: случайное добавление синонимов
def augment_text_synonym(text):
    # Создание аугментера для замены синонимов
    aug = naw.SynonymAug(aug_src='wordnet')
    # Аугментация текста
    augmented_text = aug.augment(text)
    return augmented_text

# Список для хранения аугментированных текстов и соответствующих им категорий
augmented_texts = []
augmented_categories = []

# Проход по каждой паре текст-категория и создание аугментированных данных
for text, category in zip(texts, categories):
    # Оригинальный текст и его категория
    augmented_texts.append(text)
    augmented_texts_delete.append(text)
    augmented_texts_synonym.append(text)
    augmented_categories.append(category)
    
    # Аугментация текста: случайное удаление слов и добавление в список аугментированных данных
    augmented_text_delete = augment_text_delete(text)
    augmented_texts.append(augmented_text_delete)
    augmented_categories.append(category)

    # Аугментация текста: случайное добавление синонимов и добавление в список аугментированных данных
    augmented_text_synonym = augment_text_synonym(text)
    augmented_texts.append(augmented_text_synonym)
    augmented_categories.append(category)

# Создание DataFrame с исходными и аугментированными данными
augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

# Сохранение данных в новый файл
augmented_data.to_excel("augmented_data.xlsx", index=False)

