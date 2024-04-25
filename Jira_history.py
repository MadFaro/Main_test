import zipfile
import os

def unzip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Пример использования:
zip_file = 'example.zip'  # Путь к вашему архиву ZIP
extract_to = 'extracted_folder'  # Путь к папке, куда нужно извлечь файлы

# Убедитесь, что папка для извлечения существует, иначе создайте её
if not os.path.exists(extract_to):
    os.makedirs(extract_to)

# Разархивируем
unzip(zip_file, extract_to)

