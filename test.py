import pandas as pd
from datetime import datetime, timedelta

# Читаем Excel-файл с пропуском первой строки и выбором первых 27 столбцов
data = pd.read_excel("your_file.xlsx", skiprows=1, usecols=range(27))  # Замените 'your_file.xlsx' на имя вашего файла

# Преобразуем таблицу в длинный формат
rows = []
for _, row in data.iterrows():
    date = row["дата/часы"]
    for hour in range(24):
        time = f"{hour:02d}:00"
        interval = "01:00"
        value = row[str(hour)]  # Значение из соответствующего часа
        rows.append(["WEBIM_Chat", date, time, interval, value])

# Создаем DataFrame из собранных данных
output_df = pd.DataFrame(rows, columns=["Имя очереди", "Дата", "Время", "Интервал времени", "Требования ЭПЗ"])

# Сохраняем результат в txt-файл
output_file = "output.txt"
output_df.to_csv(output_file, sep="\t", index=False, header=False)

print(f"Данные успешно преобразованы и сохранены в {output_file}")
