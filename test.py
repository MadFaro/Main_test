import pandas as pd

# Читаем Excel-файл с пропуском первой строки и выбором первых 27 столбцов
file_path = "your_file.xlsx"  # Укажите имя файла
data = pd.read_excel(file_path, skiprows=1, usecols=range(27))  # Пропускаем первую строку, берем 27 столбцов

# Проверяем названия столбцов и преобразуем их в строки, если необходимо
data.columns = data.columns.astype(str)

# Удаляем строки, где 14-й столбец (индекс 13) пустой
if "13" in data.columns:
    data = data[data["13"].notna()]
else:
    raise ValueError("14-й столбец (индекс 13) отсутствует в данных!")

# Проверяем, что столбцы с часами (0–23) существуют
hour_columns = [str(i) for i in range(24)]
missing_columns = [col for col in hour_columns if col not in data.columns]
if missing_columns:
    raise ValueError(f"Отсутствуют столбцы с часами: {', '.join(missing_columns)}")

# Преобразуем таблицу в длинный формат
rows = []
for _, row in data.iterrows():
    date = row["дата/часы"]  # Убедитесь, что столбец с датой называется именно так
    for hour in range(24):
        time = f"{hour:02d}:00"  # Форматируем время в часах
        interval = "01:00"
        value = row[str(hour)]  # Получаем значение для текущего часа
        rows.append(["WEBIM_Chat", date, time, interval, value])

# Создаем DataFrame из собранных данных
output_df = pd.DataFrame(rows, columns=["Имя очереди", "Дата", "Время", "Интервал времени", "Требования ЭПЗ"])

# Сохраняем результат в txt-файл
output_file = "output.txt"  # Имя выходного файла
output_df.to_csv(output_file, sep="\t", index=False, header=False, encoding="utf-8")

print(f"Данные успешно преобразованы и сохранены в {output_file}")
