import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from collections import Counter
from textblob import TextBlob

# Предварительная обработка текста
def preprocess_text(text):
    stop_words = set(stopwords.words('russian'))
    word_tokens = word_tokenize(text.lower(), language='russian')
    stemmer = SnowballStemmer('russian')
    filtered_text = [stemmer.stem(w) for w in word_tokens if not w in stop_words and w.isalpha()]
    return filtered_text

# Анализ ключевых слов
def extract_keywords(text):
    filtered_text = preprocess_text(text)
    word_freq = Counter(filtered_text)
    return word_freq.most_common(10)  # 10 наиболее часто встречающихся слов

# Анализ тональности
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Положительное значение указывает на позитивную тональность

# Пример использования
transcript = "Ваш текст транскрипции здесь."
keywords = extract_keywords(transcript)
print("Топ ключевых слов:", keywords)

sentiment_score = analyze_sentiment(transcript)
print("Оценка тональности:", sentiment_score)

nltk.download('stopwords')
nltk.download('punkt')
pip install nltk textblob
