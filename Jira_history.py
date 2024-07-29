async def my_rate(sdep, tab, fio, id):
    filename = 'Команда № 1 Братский круг.pptx'
    filepath = 'ppt/Команда № 1 Братский круг.pptx'
    popup('ЗАДАНИЯ', [
        put_collapse('Задание 1', [
            put_table([
                ['Команда', 'Презентация'],
                ['БРАТСКИЙ КРУГ', put_button("Скачать", onclick=lambda: download_action(filepath, filename))]
            ])
        ], open=True)
    ], size='large')

async def download_action(filepath, filename):
    """Асинхронная функция для скачивания файла"""
    with open(filepath, 'rb') as file:
        content = file.read()
    return put_file(filename, content)
