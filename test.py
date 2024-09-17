DATE_TIME_FORMAT
DD.MM.YYYY HH:mm
Имя очереди	Дата	Время	Интервал времени	Объём	СВО (Секунды)
SG_Operator	01.10.2024	00:00	00:15	12	508
SG_Operator	01.10.2024	00:15	00:15	13	493
SG_Operator	01.10.2024	00:30	00:15	7	376
SG_Operator	01.10.2024	00:45	00:15	8	361
SG_Operator	01.10.2024	01:00	00:15	7	460
SG_Operator	01.10.2024	01:15	00:15	7	486
SG_Operator	01.10.2024	01:30	00:15	7	414
SG_Operator	01.10.2024	01:45	00:15	7	394
SG_Operator	01.10.2024	02:00	00:15	6	326
SG_Operator	01.10.2024	02:15	00:15	5	318

import pandas as pd
from log import log, passw, dsn, sql, temp

import cx_Oracle
from sqlalchemy import create_engine

from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, GRU, Dropout





# Конект к БД
connect_str = lambda: cx_Oracle.connect(user=log, password=passw, dsn = dsn)
connect = create_engine("oracle://", creator=connect_str)

# Загружаем датасет для обучения
df = pd.read_sql(sql, connect)
df_h = pd.read_sql('select CLD_DAY_DT as dt from ORL.ORL_CLD_PROD_CALENDAR@cdw.prod where HOL_MSK_FLG = 1', connect)
df_h['dt'] = df_h['dt'].apply(lambda x: x.date())
holidays_list = df_h['dt'].tolist()

# Создаем признаки
df['datetime'] = pd.to_datetime(df['datetime'], format='%d.%m.%Y')
df.sort_values(by='datetime', inplace=True)
df['day_of_week'] = df['datetime'].dt.dayofweek.astype(int)
df['start_week'] = df['datetime'].dt.dayofweek.isin([0, 1]).astype(int)
df['hour'] = df['datetime'].dt.hour.astype(int)
df['minute'] = df['datetime'].dt.minute.astype(int)
df['start'] = df['datetime'].dt.day.isin([1, 2, 3]).astype(int)
df['end'] = df['datetime'].dt.is_month_end.astype(int)
df['day'] = df['datetime'].dt.day.astype(int)
df['month'] = df['datetime'].dt.month.astype(int)
df['holidays'] = df['datetime'].dt.date.isin(holidays_list).astype(int)

# Нормализация копии датасета
df_normalized = df.copy()
df_normalized.drop('datetime', axis=1, inplace=True)
df_normalized[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour', 'minute']] = df[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour', 'minute']] / df[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour', 'minute']].max()

# Контроль переобучения
early = EarlyStopping(monitor='loss', min_delta=0.0001, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model.h5', monitor='loss', verbose=2, save_best_only=False, mode='auto')
callbacks = [early, check]

# Создание модели
model = Sequential()
model.add(LSTM(16, activation='tanh', input_shape=(9, 1), return_sequences = True))
model.add(Dropout(0.1))
model.add(GRU(32, activation='relu'))
model.add(Dense(1))
model.compile(optimizer=Adam(learning_rate=0.006), loss='mse', metrics=['mae'])

# Обучение
X_train = df_normalized[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour', 'minute']].values.reshape((df_normalized.shape[0], 9, 1))
y_train = df_normalized['calls'].values.reshape((df_normalized.shape[0], 1))
model.fit(X_train, y_train, epochs=300, batch_size=744, verbose=1, callbacks=callbacks)

# Создаем таблицу с признакамия для прогноза
next_days = pd.date_range(start=(df['datetime'].max()+pd.Timedelta(minutes=30)), periods=62*48, freq='30T')
X_pred = pd.DataFrame({'datetime': next_days})
X_pred['hour'] = X_pred['datetime'].dt.hour.astype(int)
X_pred['minute'] = X_pred['datetime'].dt.minute.astype(int)
X_pred['day_of_week'] = X_pred['datetime'].dt.dayofweek.astype(int)
X_pred['start_week'] = X_pred['datetime'].dt.dayofweek.isin([0, 1]).astype(int)
X_pred['day'] = X_pred['datetime'].dt.day.astype(int)
X_pred['start'] = X_pred['datetime'].dt.day.isin([1, 2, 3]).astype(int)
X_pred['end'] = X_pred['datetime'].dt.is_month_end.astype(int)
X_pred['month'] = X_pred['datetime'].dt.month.astype(int)
X_pred['holidays'] = X_pred['datetime'].dt.date.isin(holidays_list).astype(int)
X_pred_formatted = (X_pred[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour', 'minute']] / 
                    df[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour', 'minute']].max()).values.reshape((X_pred.shape[0], 9, 1))

# Делаем прогноз
predictions_normalized = model.predict(X_pred_formatted)
predictions = predictions_normalized * df['calls'].max()
X_pred['predictions'] = abs(predictions)
X_pred['predictions'] = X_pred.apply(lambda row: row['predictions'] * 1.10 if row['day'] == 1 else row['predictions'], axis=1)
X_pred.to_excel('test.xlsx')
