import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import load_model

# Загрузка сохраненной модели
model = load_model("model.h5")

# Загрузка новых данных для предсказания
data_new = pd.read_excel("test1.xlsx")
X_new = data_new['MSG']

# Преобразование текста в числовые векторы с помощью TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_new_tfidf = tfidf_vectorizer.transform(X_new)

# Предсказание категорий
predictions = model.predict(X_new_tfidf)

# Декодирование предсказанных меток категорий
predicted_categories = label_encoder.inverse_transform(predictions.argmax(axis=1))

# Добавление предсказанных категорий в новый DataFrame
data_new['CATEGORY'] = predicted_categories

# Запись данных в новый файл CSV
data_new.to_csv("itog.csv", index=False)

print("Предсказания сохранены в файл itog.csv")
