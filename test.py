import pandas as pd

# Путь к файлу
file_path = r"V:\VOL2\Contact-center\Файлы\Аналитика\Численность ДДО\022025\3.Чаты\Профиль нагрузки_чаты_022025.xlsx"

# Чтение данных из Excel, столбцы с 28 по 53 (которые соответствуют часам 0-23)
data = pd.read_excel(file_path, skiprows=1, usecols=range(28, 54))  # Столбцы с AC по BC
data = data.drop(columns=data.columns[[1, 2]])  # Удаление 2-х первых ненужных столбцов (дата и день недели)
data = data[data.iloc[:, 13].notna()]  # Удаление строк, где в 14-ом столбце (индекс 13) пропущены значения

# Чтение даты
dates = pd.read_excel(file_path, usecols=[0], skiprows=1)  # Первый столбец — дата

# Список для строк
rows = []

# Перебираем строки данных
for i, row in data.iterrows():
    # Извлекаем дату
    date = dates.iloc[i, 0].strftime("%d.%m.%Y")  # Форматируем дату
    
    # Перебираем все часы, начиная с 0 до 23 (столбцы с 28 по 53, но с учетом сдвига на 1)
    for hour in range(24):
        time = f"{hour:02d}:00"
        
        # Здесь час столбца напрямую соответствует числу от 0 до 23
        value = row[hour]  # Доступ к данным через индекс часа
        
        # Формируем строку для вывода
        rows.append(["WEBIM_Chat", date, time, "01:00", value])  # Интервал времени всегда 01:00

# Создаем DataFrame для результата
output_df = pd.DataFrame(rows, columns=["Имя очереди", "Дата", "Время", "Интервал времени", "Требования ЭПЗ"])

# Сохраняем в текстовый файл
output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    # Пишем заголовок
    f.write("DATE_TIME_FORMAT\n")
    f.write("DD.MM.YYYY HH:mm\n")
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tТребования ЭПЗ\n")
    
    # Записываем данные
    for _, row in output_df.iterrows():
        line = "\t".join(str(value) for value in row)  # Преобразуем значения в строку с табуляцией
        f.write(line + "\n")  # Записываем строку с новой строкой

print(f"Данные успешно преобразованы и сохранены в {output_file}")
