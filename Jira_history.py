model = Sequential([
    LSTM(60, activation='relu', input_shape=(X_tfidf.shape[1],), return_sequences=True),
    LSTM(120, activation='softmax'),
    Dense(1)
])

# Компиляция модели
model.compile(optimizer=Adam(learning_rate=0.006), loss='mse', metrics=['mae'])
