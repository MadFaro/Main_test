import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Загрузка данных
data = pd.read_csv('customer_questions.csv', encoding='cp1251', delimiter=";")

print(data)
# Предварительная обработка текста
stop_words = set(stopwords.words('russian'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(tokens)

data['processed_text'] = data['Вопрос'].apply(preprocess_text)

# Вычисление TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000)
X = vectorizer.fit_transform(data['processed_text'])

# Кластеризация вопросов
num_clusters = 3  # Выбор оптимального числа кластеров
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Вывод наиболее частых вопросов в каждом кластере
for cluster_num in range(num_clusters):
    print(f"Кластер {cluster_num}:")
    cluster_data = data[data['cluster'] == cluster_num]
    frequent_questions = cluster_data['Вопрос'].value_counts().head(5)
    print(frequent_questions)
    print()

