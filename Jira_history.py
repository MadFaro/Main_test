
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)

import pandas as pd

# Пример данных
data = {'TimeColumn1': ['367:20:23', '10:15:30', '12:45:15'],
        'TimeColumn2': ['245:10:00', '11:00:00', '123:30:00']}

# Создайте DataFrame
df = pd.DataFrame(data)

# Функция для преобразования времени в десятичное число
def time_to_decimal(time_str):
    time_parts = time_str.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])
    decimal_time = hours + minutes / 60 + seconds / 3600
    return decimal_time

# Примените функцию к каждому столбцу с временем
for column in df.columns:
    df[column] = df[column].apply(time_to_decimal)

# Ваши столбцы с временем теперь содержат десятичные числа
print(df)
