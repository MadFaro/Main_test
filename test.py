def create_shortcut(filename, url, icon_path=None):
    with open(filename, 'w') as shortcut:
        shortcut.write(f"[InternetShortcut]\nURL={url}\n")
        if icon_path:  # Если передан путь к иконке, добавляем его в ярлык
            shortcut.write(f"IconFile={icon_path}\n")

# Пример использования
token = "your_unique_token"
url = f"https://yourwebsite.com/login?token={token}"
icon_path = "C:\\path\\to\\your\\icon.ico"  # Заменить на реальный путь к иконке

create_shortcut("login_shortcut.url", url, icon_path)

