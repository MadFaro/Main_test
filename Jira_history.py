# Преобразование текста в числовые векторы с помощью TF-IDF
X_new_tfidf = tfidf_vectorizer.transform(X_new)
X_new_tfidf.sort_indices()  # Упорядочивание индексов
