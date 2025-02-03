import pandas as pd

# Загружаем данные
df = pd.read_excel("your_file.xlsx")  # замените на актуальное имя файла

# Группируем по часу
df_grouped = df.groupby(df['datetime'].dt.floor('H')).agg({
    'hour': 'first',
    'day_of_week': 'first',
    'minute': 'first',
    'day': 'first',
    'start': 'first',
    'end': 'first',
    'month': 'first',
    'holidays': 'first',
    'predictions': 'sum'
}).reset_index()

# Сохраняем результат
df_grouped.to_excel("grouped_file.xlsx", index=False)

print(df_grouped.head())
