# Преобразуем каждый объект времени в количество секунд
df['time_as_seconds'] = df['time_column'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)

# Преобразуем каждый объект времени во float (количество секунд) для удобства использования
df['time_as_float'] = df['time_as_seconds'].astype(float)
