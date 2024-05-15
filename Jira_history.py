from pywebio import start_server, config
from pywebio.output import *
from pywebio.pin import *
from pywebio.input import *
from pywebio.session import run_js
import logging


# Авторизация
@config(description='shop', title='shop')
async def main():
    put_text("Привет")
    print("Привет")


# Вызов
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_server(main, host = 'localhost')
