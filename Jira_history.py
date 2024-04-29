from tensorflow.keras.utils import plot_model

# Построение модели
model = Sequential([
    Dense(len(label_encoder.classes_), activation='linear', input_shape=(X_train_tfidf.shape[1],)),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='tanh'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Сохранение визуализации модели в файл 'model_architecture.jpg'
plot_model(model, to_file='model_architecture.jpg', show_shapes=True)
