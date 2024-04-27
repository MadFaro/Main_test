import numpy as np

# Преобразование TF-IDF матрицы в трехмерный массив
X_tfidf_3d = np.reshape(X_tfidf.toarray(), (X_tfidf.shape[0], 1, X_tfidf.shape[1]))
