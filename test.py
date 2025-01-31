import pandas as pd

# Путь к файлу
file_path = r"V:\VOL2\Contact-center\Файлы\Аналитика\Численность ДДО\022025\3.Чаты\Профиль нагрузки_чаты_022025.xlsx"
data = pd.read_excel(file_path, skiprows=1)  # Загружаем все данные

# Смотрим на столбцы данных
print(data.columns)

# Дата в первом столбце и часовые значения с 0.1 до 23.1
data = data.dropna(subset=data.columns[1:])  # Убираем строки с пустыми значениями по часам

# Массив для хранения всех строк для вывода
rows = []

# Перебираем все строки
for i, row in data.iterrows():
    date = row['дата/часы.1'].strftime("%d.%m.%Y")  # Форматируем дату в нужный формат
    
    # Перебираем все часы с 0.1, 1.1, ..., 23.1
    for hour in range(24):
        # Название столбца для текущего часа
        hour_column = f"{hour}.1"
        
        # Значение для текущего часа
        value = row[hour_column]  # Берем значение для текущего часа
        
        # Формируем строку для записи
        time = f"{hour:02d}:00"  # Форматируем строку времени (например, 00:00, 01:00)
        rows.append(["WEBIM_Chat", date, time, "01:00", value])  # Добавляем строку в список

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
