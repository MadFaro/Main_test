def download_file():
    # Указываем путь и имя файла
    filename = 'README.md'
    filepath = 'path/to/your/files/README.md'

    # Создаем кнопку для скачивания файла
    put_button(f"Скачать {filename}", onclick=lambda: download_action(filepath, filename))

def download_action(filepath, filename):
    """Функция, которая вызывается при нажатии на кнопку скачивания."""
    try:
        # Читаем файл при нажатии на кнопку
        with open(filepath, 'rb') as file:
            content = file.read()
        
        # Отдаем файл для скачивания
        put_file(filename, content)
    except FileNotFoundError:
        put_text(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        put_text(f"Произошла ошибка: {e}")
