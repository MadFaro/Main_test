from pywebio.output import put_link, put_text
from pywebio import start_server

def app():
    # UNC путь к сетевой папке
    network_path = r"\\192.168.0.1\shared_folder"
    
    # Создание ссылки в PyWebIO
    put_text("Чтобы открыть папку, скопируйте путь:")
    put_text(network_path)
    put_link("Кликните, чтобы открыть папку в проводнике", url=f"file:///{network_path}")

start_server(app, port=8080)

