
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from joblib import dump

# Загрузка данных из Excel-файла
excel_file_path = 'путь_к_вашему_файлу.xlsx'
df = pd.read_excel(excel_file_path)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(df['текст_обращения'], df['тематика'], test_size=0.2, random_state=42)

# Создание конвейера (pipeline) с векторизатором и классификатором
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Определение сетки параметров для подбора
param_grid = {
    'vectorizer__ngram_range': [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3)],  # Попробуйте разные диапазоны n-gram
    'vectorizer__max_df': [0.5, 0.6, 0.7, 0.8, 0.9],       # Максимальная документная частота
    'classifier__alpha': [0.01, 0.1, 0.5, 1.0, 2.0],          # Параметр сглаживания в Naive Bayes
}

# Инициирование Grid Search с кросс-валидацией
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)

# Обучение модели с подбором параметров
grid_search.fit(X_train, y_train)

# Вывод наилучших параметров
print("Наилучшие параметры:", grid_search.best_params_)

# Получение наилучшей модели
best_model = grid_search.best_estimator_

# Сохранение модели с лучшими параметрами
model_filename = 'best_model.joblib'
dump(best_model, model_filename)

# Оценка модели с наилучшими параметрами
y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy с наилучшими параметрами: {accuracy}')

# Другие метрики оценки
print('\nClassification Report:')
print(classification_report(y_test, y_pred))

