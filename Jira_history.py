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
df['start'] = df['datetime'].dt.day.isin([1, 2, 3]).astype(int)
df['end'] = df['datetime'].dt.is_month_end.astype(int)
df['day'] = df['datetime'].dt.day.astype(int)
df['month'] = df['datetime'].dt.month.astype(int)
df['holidays'] = df['datetime'].dt.date.isin(holidays_list).astype(int)

# Нормализация копии датасета
df_normalized = df.copy()
df_normalized.drop('datetime', axis=1, inplace=True)
df_normalized[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour']] = df[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour']] / df[['calls', 'month', 'day_of_week', 'start_week', 'day', 'start' , 'end',
               'holidays', 'hour']].max()

# Контроль переобучения
early = EarlyStopping(monitor='loss', min_delta=0.0001, patience=5, verbose=2, mode='auto')
check = ModelCheckpoint('model.h5', monitor='loss', verbose=2, save_best_only=False, mode='auto')
callbacks = [early, check]

# Создание модели
model = Sequential()
model.add(LSTM(16, activation='tanh', input_shape=(8, 1), return_sequences = True))
model.add(Dropout(0.1))
model.add(GRU(32, activation='relu'))
model.add(Dense(1))
model.compile(optimizer=Adam(learning_rate=0.006), loss='mse', metrics=['mae'])

# Обучение
X_train = df_normalized[['month', 'day_of_week', 'start_week', 'day', 'start', 'end', 'holidays', 'hour']].values.reshape((df_normalized.shape[0], 8, 1))
y_train = df_normalized['calls'].values.reshape((df_normalized.shape[0], 1))
model.fit(X_train, y_train, epochs=300, batch_size=744, verbose=1, callbacks=callbacks)
