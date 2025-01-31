import pandas as pd

# Читаем Excel-файл, выбирая нужные столбцы (AC-BC)
file_path = "your_file.xlsx"  # Укажите путь к вашему файлу
data = pd.read_excel(file_path, skiprows=1, usecols=range(29, 55))  # Столбцы AC-BC (29-54)

# Удаляем строки, где 14-й столбец (индекс 13) пустой
data = data[data.iloc[:, 13].notna()]

# Преобразуем все названия столбцов в строки, а потом в целые числа, если это возможно
new_columns = ['дата/часы'] + [str(i) for i in range(24)]  # Делаем первый столбец датой, остальные - часы
data.columns = new_columns

# Преобразуем значения внутри таблицы в целые числа (кроме даты)
data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: int(x) if pd.notnull(x) else 0)

# Преобразуем таблицу в длинный формат
rows = []
for _, row in data.iterrows():
    date = row['дата/часы']  # Дата из первого столбца
    for hour in range(24):
        time = f"{hour:02d}:00"
        interval = "01:00"
        value = row[str(hour)]  # Берем значение из соответствующего часа
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
    
    # Записываем данные вручную, чтобы избежать пустых строк
    for _, row in output_df.iterrows():
        line = "\t".join(str(value) for value in row)  # Преобразуем все значения в строку с табуляцией
        f.write(line + "\n")  # Пишем строку с новой строкой в конце

print(f"Данные успешно преобразованы и сохранены в {output_file}")
