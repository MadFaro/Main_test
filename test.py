import pandas as pd

# Читаем Excel-файл, выбирая столбцы AC-BC (29-54) и пропуская первую строку
file_path = "your_file.xlsx"  # Укажите путь к вашему файлу
data = pd.read_excel(file_path, skiprows=1, usecols=range(29, 55))  # Столбцы AC-BC (29-54)

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
    date = row["дата/часы"]  # Убедитесь, что название этого столбца корректно
    for hour in range(24):
        time = f"{hour:02d}:00"
        interval = "01:00"
        value = row[str(hour)]  # Значение из соответствующего часа
        rows.append(["WEBIM_Chat", date, time, interval, value])

# Создаем DataFrame из собранных данных
output_df = pd.DataFrame(rows, columns=["Имя очереди", "Дата", "Время", "Интервал времени", "Требования ЭПЗ"])

# Добавляем заголовок в текстовый файл
output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    # Пишем фиксированный заголовок
    f.write("DATE_TIME_FORMAT\n")
    f.write("DD.MM.YYYY HH:mm\n")
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tТребования ЭПЗ\n")
    # Сохраняем данные в файл с разделителем табуляции
    output_df.to_csv(f, sep="\t", index=False, header=False)

print(f"Данные успешно преобразованы и сохранены в {output_file}")
