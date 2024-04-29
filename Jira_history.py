from tensorflow.keras.callbacks import TensorBoard

# Создание обратного вызова TensorBoard
tensorboard_callback = TensorBoard(log_dir='./logs', histogram_freq=1)

# Запуск обучения модели с использованием обратного вызова TensorBoard
model.fit(X_train, y_train, epochs=10, callbacks=[tensorboard_callback])
