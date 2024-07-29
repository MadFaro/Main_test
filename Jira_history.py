async def my_rate(sdep, tab, fio, id):
    filename = 'Команда № 1 Братский круг.pptx'
    filepath = 'ppt/Команда № 1 Братский круг.pptx'
    popup('ЗАДАНИЯ',[
        put_collapse('Задание 1', [
        put_table([
        ['Команда', 'Презентация'],
        ['БРАТСКИЙ КРУГ', put_button(f"Скачать", onclick=lambda: download_action(filepath, filename))]
                    ])
                                    ], open=True)                                 
        
        ], size='large')
async def download_action(filepath, filename):
    with open(filepath, 'rb') as file:
        content = file.read()
    print(content)
    return put_file(filename, content)
