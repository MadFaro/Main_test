import os
import win32com.client

def create_shortcut_lnk(filename, target_url, icon_path=None):
    # Создаем объект Shell для работы с COM-объектами
    shell = win32com.client.Dispatch("WScript.Shell")
    
    # Создаем ярлык (файл .lnk)
    shortcut = shell.CreateShortcut(filename)
    
    # Указываем URL в поле TargetPath (Windows откроет его как веб-ссылку)
    shortcut.TargetPath = target_url
    
    # Указываем путь к иконке, если он задан
    if icon_path:
        shortcut.IconLocation = icon_path
    
    # Сохраняем ярлык
    shortcut.save()

# Пример использования
token = "your_unique_token"
target_url = f"https://yourwebsite.com/login?token={token}"
shortcut_filename = os.path.join(os.getcwd(), "login_shortcut.lnk")
icon_path = "%ALLUSERSPROFILE%\\Uralsib\\your_icon.ico"  # Иконка на локальном ПК

create_shortcut_lnk(shortcut_filename, target_url, icon_path)

