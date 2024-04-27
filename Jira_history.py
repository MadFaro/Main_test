import numpy as np

# Преобразование TF-IDF матрицы в трехмерный тензор
X_tfidf_3d = X_tfidf.reshape(X_tfidf.shape[0], 1, X_tfidf.shape[1])


model = Sequential([
    LSTM(60, activation='relu', input_shape=(1, X_tfidf.shape[1]), return_sequences=True),
    LSTM(120, activation='softmax'),
    Dense(1)
])
