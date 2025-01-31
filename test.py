import pandas as pd

# Читаем Excel-файл
file_path = "your_file.xlsx"  # Укажите путь к вашему файлу
data = pd.read_excel(file_path, skiprows=1, usecols=range(28, 54))  # Столбцы AC-BC (28-53)

# Удаляем ненужные столбцы (второй и третий)
data = data.drop(columns=data.columns[[1, 2]])

# Преобразуем все числовые значения в таблице в целые числа
data = data.applymap(lambda x: int(x) if pd.notnull(x) else 0)

# Получаем даты из первого столбца (с датой и временем)
dates = pd.read_excel(file_path, usecols=[0], skiprows=1)  # Первый столбец — дата

# Создаем список строк для вывода
rows = []

# Перебираем все строки
for i, row in data.iterrows():
    # Извлекаем дату для текущей строки
    date = dates.iloc[i, 0].strftime("%d.%m.%Y")  # Форматируем дату в нужный формат (DD.MM.YYYY)
    
    # Перебираем данные по часам
    for hour in range(24):
        time = f"{hour:02d}:00"
        value = row.iloc[hour]  # Получаем значение для этого часа
        rows.append(["WEBIM_Chat", date, time, "01:00", value])

# Создаем DataFrame для результата
output_df = pd.DataFrame(rows, columns=["Имя очереди", "Дата", "Время", "Интервал времени", "Требования ЭПЗ"])

# Сохраняем в текстовый файл с нужным форматом
output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    # Пишем заголовок
    f.write("DATE_TIME_FORMAT\n")
    f.write("DD.MM.YYYY HH:mm\n")
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tТребования ЭПЗ\n")
    
    # Записываем данные построчно
    for _, row in output_df.iterrows():
        line = "\t".join(str(value) for value in row)  # Преобразуем все значения в строку с табуляцией
        f.write(line + "\n")  # Записываем строку с новой строкой в конце

print(f"Данные успешно преобразованы и сохранены в {output_file}")
