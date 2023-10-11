
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


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Замените URL на адрес нужной веб-страницы
url = "https://example.com"

# Отправляем GET-запрос для получения HTML-кода страницы
response = requests.get(url)
html = response.text

# Разбираем HTML-код с помощью BeautifulSoup и находим все таблицы
soup = BeautifulSoup(html, "html.parser")
tables = soup.find_all("table")

# Преобразуем каждую таблицу в объект DataFrame и сохраняем их в список
dataframes = []

for table in tables:
    df = pd.read_html(str(table))
    dataframes.extend(df)

# Теперь dataframes - это список объектов DataFrame, представляющих таблицы на веб-странице
# Вы можете обрабатывать и анализировать эти таблицы по своему усмотрению

# Пример: Вывести первую таблицу (если она есть) в консоль
if dataframes:
    print(dataframes[0])

# Пример: Сохранить первую таблицу в CSV-файл
if dataframes:
    dataframes[0].to_csv("first_table.csv", index=False)


