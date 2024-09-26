import os
import shutil
from openpyxl import load_workbook

def move_folders_from_excel(excel_file, archive_path):
    # Открываем Excel-файл
    wb = load_workbook(excel_file)
    ws = wb.active

    # Проверяем, что папка для архива существует, если нет, создаем её
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)

    # Проходим по строкам Excel-файла, начиная со второй строки (первая — заголовки)
    for row in ws.iter_rows(min_row=2, max_col=1, values_only=True):
        folder_path = row[0]  # Путь к папке находится в первом столбце

        if folder_path and os.path.exists(folder_path):
            # Получаем имя папки для перемещения
            folder_name = os.path.basename(folder_path)

            # Путь к новой папке в архиве
            destination = os.path.join(archive_path, folder_name)

            try:
                # Перемещаем папку
                shutil.move(folder_path, destination)
                print(f"Папка {folder_path} перемещена в {destination}")
            except Exception as e:
                print(f"Ошибка при перемещении {folder_path}: {e}")
        else:
            print(f"Папка {folder_path} не найдена")

# Пример использования
if __name__ == "__main__":
    excel_file = "! Разбор папок.xlsx"  # Укажите имя вашего Excel файла
    archive_path = r"V:\VOL2\Contact-center\Файлы\Аналитика\Архив"  # Путь к папке, куда нужно переместить папки

    move_folders_from_excel(excel_file, archive_path)
