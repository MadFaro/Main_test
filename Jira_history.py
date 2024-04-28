import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint



model_neiro_1 = 256
model_neiro_2 = 512
model_f_act_1 = 'relu'
model_f_act_2 = 'tanh'
model_last_sloi = 'softmax'
learning_r = 0.001
batch_s = 128

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

model = Sequential([
    Dense(model_neiro_1, activation=model_f_act_1, input_shape=(X_tfidf.shape[1],)),
    Dense(model_neiro_2, activation=model_f_act_2),
    Dense(len(label_encoder.classes_), activation=model_last_sloi)
])

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=learning_r),
              metrics=['accuracy'])

early = EarlyStopping(monitor='loss', min_delta=learning_r, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model', monitor='loss', verbose=2, save_best_only=False, mode='auto', save_format='tf')
callbacks = [early, check]

model.fit(X_tfidf, y_encoded, epochs=1000, batch_size=batch_s, verbose=1, callbacks=callbacks)

data_test = pd.read_excel("test1.xlsx", sheet_name="Свод")
X_test = data_test['MSG']
y_test = data_test['CATEGORY']

X_test_tfidf = tfidf_vectorizer.transform(X_test)
X_test_tfidf.sort_indices()
y_test_encoded = label_encoder.transform(y_test)

model = load_model('model')
loss, accuracy = model.evaluate(X_test_tfidf, y_test_encoded, verbose=0)

print("Loss на тестовой выборке:", loss)
print("Accuracy на тестовой выборке:", accuracy)
