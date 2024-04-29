import pandas as pd
import nlpaug.augmenter.word as naw

# Загрузка данных из файла
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Выделение текстовых данных и соответствующих им категорий
texts = data['MSG']
categories = data['CATEGORY']

# Функция для аугментации текста
def augment_text(text):
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
    augmented_categories.append(category)
    
    # Аугментация текста и добавление в список аугментированных данных
    augmented_text = augment_text(text)
    augmented_texts.append(augmented_text)
    augmented_categories.append(category)

# Создание нового DataFrame с аугментированными данными
augmented_data = pd.DataFrame({'MSG': augmented_texts, 'CATEGORY': augmented_categories})

# Сохранение аугментированных данных в новый файл
augmented_data.to_excel("augmented_data.xlsx", index=False)
