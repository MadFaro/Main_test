import pandas as pd

# Предположим, что у вас уже есть DataFrame df с колонкой 'datetime'
# Найдем максимальное значение в колонке 'datetime' и добавим 1 час
start_datetime = df['datetime'].max() + pd.Timedelta(hours=1)

# Создадим список для хранения новых значений дат и времени
date_list = []

# Цикл по каждому дню в течение 62 дней
for day in range(62):
    # Для каждого дня создадим временные метки от 04:00 до 22:00
    day_start = start_datetime + pd.Timedelta(days=day)
    times = pd.date_range(start=day_start.replace(hour=4, minute=0, second=0),
                          end=day_start.replace(hour=22, minute=0, second=0),
                          freq='1H')
    date_list.extend(times)

# Преобразуем список дат в DataFrame
new_df = pd.DataFrame(date_list, columns=['datetime'])

# Посмотрим на результат
print(new_df)
