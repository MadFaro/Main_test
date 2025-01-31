import pandas as pd

# Путь к файлу
file_path = r"V:\VOL2\Contact-center\Файлы\Аналитика\Численность ДДО\022025\3.Чаты\Профиль нагрузки_чаты_022025.xlsx"

# Чтение данных из Excel
data = pd.read_excel(file_path, skiprows=1, usecols=range(3, 29))  # Столбцы с 0 по 23 (28 столбцов)
dates = pd.read_excel(file_path, usecols=[0], skiprows=1)  # Даты

# Создаем список для итоговых строк
rows = []

# Перебираем строки данных
for i, row in data.iterrows():
    # Извлекаем дату
    date = dates.iloc[i, 0].strftime("%d.%m.%Y")
    
    # Перебираем значения по часам
    for hour in range(24):
        # Получаем значение для текущего часа
        value = row[hour]  # Значение по этому часу
        
        # Формируем строку
        time = f"{hour:02d}:00"
        rows.append(["WEBIM_Chat", date, time, "01:00", value])  # Интервал времени всегда 01:00
    
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
