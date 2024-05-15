from pywebio.platform.tornado_http import start_server
from pywebio import STATIC_PATH

# Путь к локальным статическим файлам PyWebIO
LOCAL_STATIC_PATH = '/путь/к/папке/с/статическими/ресурсами/PyWebIO'

# Запуск сервера PyWebIO с использованием локальных статических файлов
start_server(
    lambda: None, 
    static_dir=STATIC_PATH, 
    use_builtin_static=False, 
    local_static_dir=LOCAL_STATIC_PATH
)
