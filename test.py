import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Загрузка данных
data = pd.read_csv('employee_data.csv', parse_dates=['MONTH'])

# 2. Преобразование категориальных признаков в числовые
label_encoders = {}
categorical_columns = ['PODRAZDELENIE', 'DOLZHHNOST', 'DIRECT', 'TYPE_CODE']

for column in categorical_columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# 3. Преобразование целевой переменной (STATUS)
data['STATUS'] = data['STATUS'].apply(lambda x: 1 if x == 'Уволен' else 0)

# 4. Разделение данных на признаки и целевую переменную
X = data.drop(columns=['STATUS', 'MONTH', 'TABNUM'])  # Признаки
y = data['STATUS']  # Целевая переменная (уволен или нет)

# 5. Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 6. Масштабирование признаков
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7. Обучение модели
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 8. Оценка модели
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

