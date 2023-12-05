
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

# Создайте DataFrame с вашими данными
data = {'created': ['2023-11-01 00:05:34'],
        'closed': ['2023-11-01 00:10:20'],
        'operatorname': ['Янгирова Карина'],
        'chatid': [78564]}

df = pd.DataFrame(data)

# Преобразуйте столбцы 'created' и 'closed' в формат datetime
df['created'] = pd.to_datetime(df['created'])
df['closed'] = pd.to_datetime(df['closed'])

# Сортировка данных по времени создания чата
df = df.sort_values(by='created')

# Создание столбца для отслеживания активных чатов
df['active_chats'] = 0

# Список для отслеживания числа активных чатов в каждый момент времени
active_chats_list = []

# Цикл по данным для отслеживания активных чатов
for index, row in df.iterrows():
    # Увеличение счетчика при начале чата
    df.loc[index:, 'active_chats'] += 1
    # Уменьшение счетчика при завершении чата
    end_time = row['closed']
    df.loc[df['created'] > end_time, 'active_chats'] -= 1
    # Запись числа активных чатов в список
    active_chats_list.append(df['active_chats'].max())

# Добавление списка в DataFrame
df['active_chats_max'] = active_chats_list

# Вывод среднего значения активных чатов
average_active_chats = df['active_chats_max'].mean()

print(f'Среднее количество чатов в работе у операторов: {average_active_chats}')

