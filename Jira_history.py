
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav



import pandas as pd
import cx_Oracle
import holidays
from sqlalchemy import create_engine
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Conv1D, MaxPooling1D, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import Adam


holidays_ru = holidays.Russia(years=2023)
# Конект к БД
connect = create_engine("oracle://", creator=connect_str)

sql = """
        select day as datetime, sum(CALLSOFFERED) as calls from (
        Select trunc(INTERVAL, 'HH24') as day, sum(CALLSOFFERED) as CALLSOFFERED
        from ANALYTICS.TOLOG_TEMP_ML1
        where INTERVAL < date'2023-06-01' and FULLNAME in 
        ('CCM_PG_1.SG_DDO_ActiveCredit',
        'CCM_PG_1.SG_DDO_DebetCard',
        'CCM_PG_1.SG_Operator')
        group by trunc(INTERVAL, 'HH24')
        union
        Select trunc(V0, 'HH24') as day, sum(v5) as CALLSOFFERED
        from ANALYTICS.TOLOG_TEMP_ML2
        where V0 < date'2023-06-01'
        group by trunc(V0, 'HH24')) a
        group by day
        order by day
        """

# Данные для обучения
df = pd.read_sql(sql, connect)
df['datetime'] = pd.to_datetime(df['datetime'], format='%d.%m.%Y')
df.sort_values(by='datetime', inplace=True)
df['day_of_week'] = df['datetime'].dt.dayofweek.astype(int)
df['start_week'] = df['datetime'].dt.dayofweek.isin([0]).astype(int)
df['hour'] = df['datetime'].dt.hour.astype(int)
df['start'] = df['datetime'].dt.day.isin([1, 2, 3]).astype(int)
df['end'] = df['datetime'].dt.is_month_end.astype(int)
df['day'] = df['datetime'].dt.day.astype(int)
df['month'] = df['datetime'].dt.month.astype(int)
df['holidays'] = df['datetime'].dt.date.isin(holidays_ru).astype(int)
df_normalized = df.copy()
df_normalized.drop('datetime', axis=1, inplace=True)
df_normalized[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour']] = df[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour']] / df[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour']].max()

# Контроль переобучения по эпохам
early = EarlyStopping(monitor='loss', min_delta=0.0001, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model.h5', monitor='loss', verbose=2, save_best_only=False, mode='auto')
callbacks = [early, check]

# Создание модели
model = Sequential()
model.add(LSTM(66, activation='tanh', input_shape=(8, 1), return_sequences = True))
model.add(LSTM(66, activation='relu'))
model.add(Dense(1))
model.compile(optimizer=Adam(learning_rate=0.006), loss='mse', metrics=['mae'])

# Обучение
X_train = df_normalized[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour']].values.reshape((df_normalized.shape[0], 8, 1))
y_train = df_normalized['calls'].values.reshape((df_normalized.shape[0], 1))
model.fit(X_train, y_train, epochs=300, batch_size=720, verbose=1, callbacks=callbacks)

# Таблица для прогноза
next_days = pd.date_range(start=(df['datetime'].max()+pd.Timedelta(hours=1)), periods=61*24, freq='1H')
X_pred = pd.DataFrame({'datetime': next_days})
X_pred['hour'] = X_pred['datetime'].dt.hour.astype(int)
X_pred['day_of_week'] = X_pred['datetime'].dt.dayofweek.astype(int)
X_pred['start_week'] = X_pred['datetime'].dt.dayofweek.isin([0]).astype(int)
X_pred['day'] = X_pred['datetime'].dt.day.astype(int)
X_pred['start'] = X_pred['datetime'].dt.day.isin([1, 2, 3]).astype(int)
X_pred['end'] = X_pred['datetime'].dt.is_month_end.astype(int)
X_pred['month'] = X_pred['datetime'].dt.month.astype(int)
X_pred['holidays'] = X_pred['datetime'].dt.date.isin(holidays_ru).astype(int)
X_pred_formatted = (X_pred[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour']] / df[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour']].max()).values.reshape((X_pred.shape[0], 8, 1))

# Прогноз
predictions_normalized = model.predict(X_pred_formatted)
predictions = predictions_normalized * df['calls'].max()
X_pred['predictions'] = predictions * 1.07
X_pred.to_excel('test.xlsx')
