# Рассчитываем веса классов
class_weights = {}
total_samples = len(y)
for cls in np.unique(y):
    cls_samples = np.sum(y == cls)
    weight = total_samples / (len(np.unique(y)) * cls_samples)
    class_weights[cls] = weight

# Создаем модель
model = Sequential([
    Dense(model_neiro_1, activation=model_f_act_1, input_shape=(X_tfidf.shape[1],)),
    Dense(model_neiro_2, activation=model_f_act_2),
    Dense(len(label_encoder.classes_), activation=model_last_sloi)
])

# Компилируем модель
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=learning_r),
              metrics=['accuracy'])

# Определяем коллбэки
early = EarlyStopping(monitor='loss', min_delta=learning_r, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model', monitor='loss', verbose=2, save_best_only=False, mode='auto', save_format='tf')
callbacks = [early, check]

# Обучаем модель с учетом весов классов
model.fit(X_tfidf, y_encoded, epochs=1000, batch_size=batch_s, verbose=1, callbacks=callbacks, class_weight=class_weights)

# Оцениваем модель на тестовой выборке
data_test = pd.read_excel("test1.xlsx", sheet_name="Свод")
X_test = data_test['MSG']
y_test = data_test['CATEGORY']

X_test_tfidf = tfidf_vectorizer.transform(X_test)
X_test_tfidf.sort_indices()
y_test_encoded = label_encoder.transform(y_test)

loss, accuracy = model.evaluate(X_test_tfidf, y_test_encoded, verbose=0)

print("Loss на тестовой выборке:", loss)
print("Accuracy на тестовой выборке:", accuracy)

# Предсказание на тестовой выборке
y_pred = model.predict(X_test_tfidf)
y_pred_classes = np.argmax(y_pred, axis=1)

# Рассчитываем F1-меру и ROC-AUC
f1 = f1_score(y_test_encoded, y_pred_classes, average='weighted')
roc_auc = roc_auc_score(y_test_encoded, y_pred, average='weighted', multi_class='ovo')

print("F1-мера на тестовой выборке:", f1)
print("ROC-AUC на тестовой выборке:", roc_auc)
print("\nОтчет о классификации на тестовой выборке:")
print(classification_report(y_test_encoded, y_pred_classes))
