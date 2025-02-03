import pandas as pd
from datetime import timedelta

# Загружаем данные
df = pd.read_excel("your_file.xlsx")

# Фильтруем month > 2
df = df[df['month'] > 2]

# Добавляем 2 часа к datetime
df['datetime'] = df['datetime'] + timedelta(hours=2)

# Пересчитываем день недели, день и месяц
df['day_of_week'] = df['datetime'].dt.weekday
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month

# Запись в файл
with open('predictions_chat.txt', 'w', encoding='utf-8') as f:
    f.write("DATE_TIME_FORMAT\nDD.MM.YYYY HH:mm\n")
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tОбъём\tСВО (Секунды)\n")

    for index, row in df.iterrows():
        date_str = row['datetime'].strftime('%d.%m.%Y')
        time_str = row['datetime'].strftime('%H:%M')
        interval = '00:30'
        queue_name = 'чат банк'
        volume = int(row['predictions'])  # Теперь значение не изменится
        
        # Определяем СВО по дню недели
        day_of_week = row['day_of_week']
        svo = SVO_BUD if day_of_week < 5 else SVO_VIX
        
        f.write(f"{queue_name}\t{date_str}\t{time_str}\t{interval}\t{volume}\t{svo}\n")
