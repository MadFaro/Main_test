import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Загрузка данных из файла Excel
data = pd.read_excel("test.xlsx", sheet_name="Свод")

# Разделение данных на признаки (X) и метки (y)
X = data['MSG']
y = data['CATEGORY']

# Преобразование текста в числовые векторы с помощью TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_tfidf = tfidf_vectorizer.fit_transform(X)
X_tfidf.sort_indices()

# Кодирование меток категорий
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Сохранение TF-IDF векторизатора
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

# Сохранение label_encoder
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Создание нейронной сети
model = Sequential([
    Dense(512, activation='relu', input_shape=(X_tfidf.shape[1],)),
    Dense(256, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Компиляция модели
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'])

# Обучение модели на всем наборе данных
early = EarlyStopping(monitor='loss', min_delta=0.001, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model.h5', monitor='loss', verbose=2, save_best_only=False, mode='auto')
callbacks = [early, check]

model.fit(X_tfidf, y_encoded, epochs=1000, batch_size=32, verbose=1, callbacks=callbacks)
