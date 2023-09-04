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

SUBSTR('Лимит по карте *1234 увеличен до 60000', INSTR('Лимит по карте *1234 увеличен до 60000', 'до ') + LENGTH('до ')) AS TextAfterDо

import psycopg2
import pandas as pd
import datetime

# Подключение к базе данных
conn = psycopg2.connect(
host = 'rc1c-fhrb9f1e0l9g611h.mdb.yandexcloud.net',
port = 6432,
dbname = 'hr-analytics',
sslmode = 'require',
user = 'analytics',
password = 'HRanalytics'
)

# Создание курсора для выполнения запросов
cur = conn.cursor()

# Запрос на получение названий столбцов таблицы orders
cur.execute('''
with r as (
select user_id
,count (*)
from orders
group by user_id
having count(*) >= 3
),
x as (
select *
,lead (ord.shipped_at) over (partition by ord.store_id order by ord.shipped_at) as next_time
from orders as ord
join r on r.user_id = ord.user_id
),
q as (
select x.*
,date_part('hour', x.next_time - x.shipped_at ) as hour_diff
from x
),
a as (
select
store_id
,avg(hour_diff) as avg_hour
from q
group by store_id
)
select store_id, avg_hour
from a
where avg_hour = (select max(avg_hour) from a)
''')

col_names = [desc[0] for desc in cur.description]

# Получение результатов запроса
sql_query = cur.fetchall()
# Закрытие курсора и соединения с базой данных
cur.close()
conn.close()

# Вывод названий столбцов

#print(sql_query)

df = pd.DataFrame(sql_query, columns=col_names)
df.to_csv (r'G:\Test\2.csv', sep=';', encoding='utf-8-sig')
