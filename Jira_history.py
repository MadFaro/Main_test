
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

# Создайте DataFrame для каждого CSV-файла
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')
df4 = pd.read_csv('file4.csv')
df5 = pd.read_csv('file5.csv')
df6 = pd.read_csv('file6.csv')
df7 = pd.read_csv('file7.csv')
df8 = pd.read_csv('file8.csv')
df9 = pd.read_csv('file9.csv')
df10 = pd.read_csv('file10.csv')

# Список всех ваших DataFrame
dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]

# Объедините их в один DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Сохраните объединенные данные в новый CSV-файл
combined_df.to_csv('combined_data.csv', index=False)
