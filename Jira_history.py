import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import load_model

# Загрузка модели
model = load_model("model.h5")

# Загрузка TF-IDF векторизатора
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

# Загрузка label_encoder
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Загрузка новых данных для предсказания
data_new = pd.read_excel("test1.xlsx", sheet_name="Свод")
X_new = data_new['MSG']

# Преобразование текста в числовые векторы с помощью TF-IDF
X_new_tfidf = tfidf_vectorizer.transform(X_new)

# Предсказание категорий
predictions = model.predict(X_new_tfidf)

# Декодирование предсказанных меток категорий
predicted_categories = label_encoder.inverse_transform(predictions.argmax(axis=1))

# Добавление предсказанных категорий в новый DataFrame
data_new['CATEGORY'] = predicted_categories

# Запись данных в новый файл CSV
data_new.to_csv("itog.csv", index=False)
