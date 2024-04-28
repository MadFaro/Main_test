
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils.class_weight import compute_class_weight
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import f1_score, roc_auc_score, classification_report
import numpy as np

model_neiro_1 = 66
model_neiro_2 = 126
model_f_act_1 = 'relu'
model_f_act_2 = 'relu'
model_last_sloi = 'softmax'
learning_r = 0.001
batch_s = 16

data = pd.read_excel("test.xlsx", sheet_name="Свод")
X = data['MSG']
y = data['CATEGORY']

tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf_vectorizer.fit_transform(X)
X_tfidf.sort_indices()

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

with open('model/tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

with open('model/param.txt', 'w') as f:
    print(model_neiro_1, model_neiro_2, model_f_act_1, model_f_act_2, model_last_sloi, learning_r, batch_s, file=f)

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


  File "test.py", line 67, in <module>
    model.fit(X_tfidf, y_encoded, epochs=1000, batch_size=batch_s, verbose=1, callbacks=callbacks, class_weight=class_weights)
  File "C:\Program Files\Python38\lib\site-packages\keras\src\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Program Files\Python38\lib\site-packages\keras\src\engine\data_adapter.py", line 1702, in _make_class_weight_map_fn
    raise ValueError(error_msg)
ValueError: Expected `class_weight` to be a dict with keys from 0 to one less than the number of classes,
