import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


model_neiro_1 = 512
model_neiro_2 = 256
model_neiro_3 = 128
model_f_act_1 = 'relu'
model_f_act_2 = 'tanh'
model_f_act_3 = 'relu'
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
    print(model_neiro_1, model_neiro_2, model_neiro_3, model_f_act_1, model_f_act_2, model_f_act_3, model_last_sloi, learning_r, batch_s, file=f)

model = Sequential([
    Dense(model_neiro_1, activation=model_f_act_1, input_shape=(X_tfidf.shape[1],)),
    Dense(model_neiro_2, activation=model_f_act_2),
    Dense(model_neiro_3, activation=model_f_act_3),
    Dense(len(label_encoder.classes_), activation=model_last_sloi)
])

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=learning_r),
              metrics=['accuracy'])

early = EarlyStopping(monitor='loss', min_delta=learning_r, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model', monitor='loss', verbose=2, save_best_only=False, mode='auto', save_format='tf')
callbacks = [early, check]

model.fit(X_tfidf, y_encoded, epochs=1000, batch_size=batch_s, verbose=1, callbacks=callbacks)
