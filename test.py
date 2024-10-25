def create_shortcut(filename, url, icon_path=None):
    with open(filename, 'w') as shortcut:
        shortcut.write(f"[InternetShortcut]\nURL={url}\n")
        if icon_path:
            # Добавляем переменную окружения без её разрешения на сервере
            shortcut.write(f"IconFile={icon_path}\n")

# Пример использования
token = "your_unique_token"
url = f"https://yourwebsite.com/login?token={token}"
# Указываем путь с системной переменной, который разрешится на локальном ПК
icon_path = "%ALLUSERSPROFILE%\\Uralsib\\your_icon.ico"

create_shortcut("login_shortcut.url", url, icon_path)

