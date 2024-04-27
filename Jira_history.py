import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Загрузка данных из файла Excel
data = pd.read_excel("test.xlsx", sheet_name="свод")

# Разделение данных на обучающий и тестовый наборы
X = data['MSG']
y = data['CATEGORY']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Преобразование текста в числовые векторы с помощью TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Кодирование меток категорий
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Создание нейронной сети
model = Sequential([
    Dense(512, activation='relu', input_shape=(X_train_tfidf.shape[1],)),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Компиляция модели
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'])

# Обучение модели
model.fit(X_train_tfidf, y_train_encoded, epochs=10, batch_size=32, validation_split=0.1)

# Оценка модели на тестовых данных
loss, accuracy = model.evaluate(X_test_tfidf, y_test_encoded)
print("Test Accuracy:", accuracy)

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
