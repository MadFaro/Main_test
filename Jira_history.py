import pandas as pd
import nltk
from nltk.corpus import wordnet

# Загрузка данных из файла
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Выделение текстовых данных и соответствующих им категорий
texts = data['MSG']
categories = data['CATEGORY']

# Функция для замены слов синонимами
def augment_text_synonym(text):
    tokens = nltk.word_tokenize(text)
    synonyms = []
    for token in tokens:
        syns = wordnet.synsets(token)
        if syns:
            synonym = syns[0].lemmas()[0].name()
            synonyms.append(synonym)
        else:
            synonyms.append(token)
    return ' '.join(synonyms)

# Список для хранения аугментированных текстов и соответствующих им категорий
augmented_texts = []
augmented_categories = []

# Проход по каждой паре текст-категория и создание аугментированных данных
for text, category in zip(texts, categories):
    # Оригинальный текст и его категория
    augmented_texts.append(text)
    augmented_categories.append(category)
    
    # Аугментация текста: замена слов синонимами и добавление в список аугментированных данных
    augmented_text_synonym = augment_text_synonym(text)
    augmented_texts.append(augmented_text_synonym)
    augmented_categories.append(category)

# Создание нового DataFrame с исходными и аугментированными данными
augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

# Сохранение аугментированных данных в новый файл
augmented_data.to_excel("augmented_data.xlsx", index=False)
