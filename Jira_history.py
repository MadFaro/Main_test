import pandas as pd

# Загрузка данных из файла или другого источника
# Пример входных данных:
# data = pd.read_csv("sessions.csv")

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
for timestamp in timestamps:
    current_sessions += timestamp[1]
    max_sessions = max(max_sessions, current_sessions)

# Расчет среднего количества одновременных сессий
average_sessions = sum(x[1] for x in timestamps) / len(timestamps)

print("Среднее количество одновременных сессий за день:", average_sessions)
print("Максимальное количество одновременных сессий за день:", max_sessions)

