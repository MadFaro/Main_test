import pandas as pd

# Предположим, что у вас есть DataFrame 'data' с колонками 'start_time', 'end_time' и 'session_id'

# Преобразование данных в формат datetime
data['start_time'] = pd.to_datetime(data['start_time'])
data['end_time'] = pd.to_datetime(data['end_time'])

# Создание списка временных меток
timestamps = []
for index, row in data.iterrows():
    timestamps.append((row['start_time'], 1))
    timestamps.append((row['end_time'], -1))

# Сортировка временных меток по времени
timestamps.sort()

# Подсчет количества одновременных сессий
current_sessions = 0
max_sessions = 0
total_time = 0
last_timestamp = None

for timestamp in timestamps:
    if last_timestamp is not None:
        total_time += (timestamp[0] - last_timestamp).total_seconds() * current_sessions
    current_sessions += timestamp[1]
    max_sessions = max(max_sessions, current_sessions)
    last_timestamp = timestamp[0]

# Расчет среднего количества одновременных сессий
average_sessions = total_time / (timestamps[-1][0] - timestamps[0][0]).total_seconds()

print("Среднее количество одновременных сессий за день:", average_sessions)
print("Максимальное количество одновременных сессий за день:", max_sessions)


