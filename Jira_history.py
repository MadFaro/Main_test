
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav



from Stemmer import Stemmer
def cleaner(txt):
  txt = txt.lower() # приведение букв в нижний регистр 
  stemmer = Stemmer('russian')
  txt = ' '.join( stemmer.stemWords( txt.split() ) ) 
  txt = re.sub( r'\b\d+\b', ' digit ', txt ) # заменяем цифры 
  return  txt 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump, load
import re
import string

# Функция предобработки текста
def preprocess_text(text):
    # Приведение к нижнему регистру
    text = text.lower()
    
    # Удаление знаков пунктуации
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # Удаление переносов строк
    text = re.sub('\n', ' ', text)
    
    # Другие операции по необходимости, например, удаление стоп-слов
    
    return text

# Загрузка данных из Excel-файла
excel_file_path = 'путь_к_вашему_файлу.xlsx'
df = pd.read_excel(excel_file_path)

# Применение предобработки к тексту
df['текст_обращения'] = df['текст_обращения'].apply(preprocess_text)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(df['текст_обращения'], df['тематика'], test_size=0.2, random_state=42)

# Использование метода векторизации текста
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Обучение модели
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Сохранение модели
model_filename = 'trained_model.joblib'
dump(model, model_filename)

# Оценка модели
y_pred = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

print('\nClassification Report:')
print(classification_report(y_test, y_pred))

# Классификация нового текста
new_text = ['Новый текст обращения']
# Применение предобработки к новому тексту
new_text = [preprocess_text(text) for text in new_text]
new_text_vectorized = vectorizer.transform(new_text)

predicted_topic = model.predict(new_text_vectorized)
print(f'Предполагаемая тематика: {predicted_topic[0]}')

# Загрузка модели для последующего использования
loaded_model = load(model_filename)


