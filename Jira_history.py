import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Загрузка данных из файла Excel
data = pd.read_excel("test.xlsx", sheet_name="свод")

# Разделение данных на признаки (X) и метки (y)
X = data['MSG']
y = data['CATEGORY']

# Преобразование текста в числовые векторы с помощью TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Кодирование меток категорий
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Создание нейронной сети
model = Sequential([
    Dense(512, activation='relu', input_shape=(X_tfidf.shape[1],)),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Компиляция модели
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'])

# Обучение модели на всем наборе данных
model.fit(X_tfidf, y_encoded, epochs=10, batch_size=32)

# Сохранение модели
model.save("model.h5")
print("Модель сохранена в файл model.h5")
