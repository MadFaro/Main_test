import os
import datetime

def get_max_file_date(dir_path):
    max_file_date = None
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_mod_time = os.path.getmtime(file_path)
            file_mod_date = datetime.datetime.fromtimestamp(file_mod_time)
            if max_file_date is None or file_mod_date > max_file_date:
                max_file_date = file_mod_date
    return max_file_date

def process_directory(disk_path):
    results = []
    
    # Проходим по всем папкам и подпапкам
    for root, dirs, files in os.walk(disk_path):
        # Получаем дату изменения текущей папки
        folder_mod_time = os.path.getmtime(root)
        folder_mod_date = datetime.datetime.fromtimestamp(folder_mod_time)
        
        # Находим максимальную дату изменения файлов в текущей папке
        max_file_date = get_max_file_date(root)

        # Добавляем данные в список результатов
        results.append({
            'folder': root,
            'folder_mod_date': folder_mod_date,
            'max_file_date': max_file_date
        })

    return results

def save_results_to_file(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Folder,Folder Last Modified Date,Max File Last Modified Date\n")
        for result in results:
            folder = result['folder']
            folder_mod_date = result['folder_mod_date'].strftime('%Y-%m-%d %H:%M:%S')
            max_file_date = result['max_file_date'].strftime('%Y-%m-%d %H:%M:%S') if result['max_file_date'] else "No files"
            f.write(f"{folder},{folder_mod_date},{max_file_date}\n")

# Пример использования
if __name__ == "__main__":
    disk_path = "C:\\Your\\Path"  # Укажите путь к диску или директории
    output_file = "directory_report.csv"  # Имя файла для записи результатов
    
    results = process_directory(disk_path)
    save_results_to_file(results, output_file)

    print(f"Результаты сохранены в файл: {output_file}")

