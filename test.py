import os
import csv

# Указываем путь к основной папке
root_folder = "путь_к_вашей_папке"

# Имя файла для сохранения результатов
output_csv = "file_paths.csv"

# Создаем список для хранения данных
data = []

# Обходим все файлы в папке и подпапках
for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        # Добавляем полный путь к файлу и его имя в список
        file_path = os.path.join(dirpath, filename)
        data.append([dirpath, filename])

# Записываем данные в CSV файл
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки столбцов
    writer.writerow(['Путь к папке', 'Имя файла'])
    # Записываем строки с данными
    writer.writerows(data)

print(f"Таблица успешно создана и сохранена в {output_csv}")

