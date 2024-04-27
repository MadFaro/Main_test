import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import load_model


model = load_model("model.h5")

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

data_new = pd.read_excel("test1.xlsx")
X_new = data_new['MSG']
X_new_tfidf = tfidf_vectorizer.transform(X_new)
X_new_tfidf.sort_indices()

predictions = model.predict(X_new_tfidf)
predicted_categories = label_encoder.inverse_transform(predictions.argmax(axis=1))

data_new['CATEGORY'] = predicted_categories
data_new[['ID', 'MSG', 'CATEGORY']].to_csv("itog.csv", index=False,  encoding='utf-8-sig')

ID	MSG
121	"А в остальном те же условия по кэшбэку, по проходам в бизнес залы, по страхованию?
Хорошо, спасибо за информацию
Добрый день, расскажите, пожалуйста, про премиальную карту. Там одно из условий бесплатного выполнения 150 т.р. поступлений на карту. Это обязательно должна быть зарплата или может быть просто перевод с другой карты?
У юнион платный выпуск карты?
А подскажите ещё про отличия платёжных систем мир суприм и юнион пэй?
Он засчитывается, правильно?"
122	"Свяжите с оператором
Моя карта арестована ?
Добрый вечер, сейчас уточню информацию и вернусь к Вам
Мне потребуется еще пару минут, ожидайте, пожалуйста
Ожидаю
Благодарю Вас за ожидание! Александр, арест действующий у Вас
Все поступившие средства на карте сразу же будут списываться ?
При поступление средств, сумма может быть списана согласна постановлению ареста, но также необходимо учитывать с каким кодом дохода поступления"

