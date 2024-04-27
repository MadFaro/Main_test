# Преобразование текста в числовые векторы с помощью TF-IDF
X_new = data_new['MSG']
X_new_tfidf = tfidf_vectorizer.transform(X_new)
X_new_tfidf.sort_indices()

# Предсказание категорий
predictions = model.predict(X_new_tfidf)
predicted_categories = label_encoder.inverse_transform(predictions.argmax(axis=1))

# Добавление предсказанных категорий в датафрейм
data_new['CATEGORY'] = predicted_categories

# Сохранение данных в новый файл Excel
data_new.to_excel("itog.xlsx", index=False)
