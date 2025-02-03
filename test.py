df['day_of_week'] = df['datetime'].dt.weekday  # Понедельник = 0, Воскресенье = 6
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month
df['hour'] = df['datetime'].dt.hour
df['minute'] = df['datetime'].dt.minute
