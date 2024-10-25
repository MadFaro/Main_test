def create_shortcut(filename, url):
    with open(filename, 'w') as shortcut:
        shortcut.write(f"[InternetShortcut]\nURL={url}\n")
