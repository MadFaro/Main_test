import pandas as pd

# Указываем путь к файлу
file_path = r"V:\VOL2\Contact-center\Файлы\Аналитика\Численность ДДО\022025\3.Чаты\Профиль нагрузки_чаты_022025.xlsx"

# Загружаем только нужные данные (столбцы с 28 по 53)
data = pd.read_excel(file_path, skiprows=1, usecols=range(28, 54))  # Столбцы AC-BC (28-53)

# Убираем лишние столбцы
data = data.drop(columns=data.columns[[1, 2]])  # Убираем первые два столбца, которые не содержат нужных данных

# Оставляем строки, где есть данные в 14-ом столбце
data = data[data.iloc[:, 13].notna()]

# Загружаем даты из первого столбца
dates = pd.read_excel(file_path, usecols=[0], skiprows=1)  # Даты из первого столбца

# Список для хранения строк результата
rows = []

# Перебираем строки данных
for i, row in data.iterrows():
    # Извлекаем дату для текущей строки
    date = dates.iloc[i, 0].strftime("%d.%m.%Y")  # Форматируем дату в нужный формат
    
    # Преобразуем значения в числовой формат
    values = row.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int).values  # Заполняем пустые значения нулями
    
    # Перебираем все 24 часа для текущей строки
    for hour in range(24):
        time = f"{hour:02d}:00"  # Форматируем время для каждого часа
        value = values[hour]  # Получаем значение для текущего часа
        rows.append(["WEBIM_Chat", date, time, "01:00", value])  # Формируем строку для записи

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
