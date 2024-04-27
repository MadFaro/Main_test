import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint

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

# Создание нейронной сети
model = Sequential([
    Dense(512, activation='relu', input_shape=(X_tfidf.shape[1],)),
    Dense(256, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

early = EarlyStopping(monitor='loss', min_delta=0.001, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model.h5', monitor='loss', verbose=2, save_best_only=False, mode='auto')
callbacks = [early, check]

# Компиляция модели
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'])

# Обучение модели на всем наборе данных
model.fit(X_tfidf, y_encoded, epochs=1000, batch_size=32, verbose=1, callbacks=callbacks)


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# Загрузка сохраненной модели
model = load_model("model.h5")

# Загрузка новых данных для предсказания
data_new = pd.read_excel("test1.xlsx", sheet_name="Свод")
X_new = data_new['MSG']

# Преобразование текста в числовые векторы с помощью TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_new_tfidf = tfidf_vectorizer.transform(X_new)

# Предсказание категорий
predictions = model.predict(X_new_tfidf)

# Декодирование предсказанных меток категорий
predicted_categories = LabelEncoder.inverse_transform(predictions.argmax(axis=1))

# Добавление предсказанных категорий в новый DataFrame
data_new['CATEGORY'] = predicted_categories

# Запись данных в новый файл CSV
data_new.to_csv("itog.csv", index=False)

Traceback (most recent call last):
  File "adam_predict.py", line 15, in <module>
    X_new_tfidf = tfidf_vectorizer.transform(X_new)
  File "C:\Python38\lib\site-packages\sklearn\feature_extraction\text.py", line 2155, in transform
    check_is_fitted(self, msg="The TF-IDF vectorizer is not fitted")
  File "C:\Python38\lib\site-packages\sklearn\utils\validation.py", line 1390, in check_is_fitted
    raise NotFittedError(msg % {"name": type(estimator).__name__})
sklearn.exceptions.NotFittedError: The TF-IDF vectorizer is not fitted
