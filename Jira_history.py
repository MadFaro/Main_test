model = Sequential([
    Dense(len(label_encoder.classes_), activation='linear', input_shape=(X_train_tfidf.shape[1],)),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='tanh'),
    Dense(len(label_encoder.classes_), activation='softmax')
])
