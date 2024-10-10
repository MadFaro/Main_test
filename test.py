import subprocess

def get_running_tasks_from_root():
    # Запуск команды SCHTASKS для получения списка задач в подробном формате (/V)
    cmd = ['SCHTASKS', '/Query', '/FO', 'LIST', '/V']
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        # Разбиваем вывод на блоки задач
        tasks = result.stdout.split("\n\n")  # Разделяем на блоки по двойным переносам строк
        running_tasks = []

        for task in tasks:
            # Проверяем, находится ли задача в корневом каталоге (\) и имеет статус Running
            if "TaskName: \\" in task and "Status: Running" in task:
                running_tasks.append(task.strip())
        
        return running_tasks
    else:
        # В случае ошибки возвращаем сообщение об ошибке
        return result.stderr

running_tasks = get_running_tasks_from_root()

# Печать выполняющихся задач из корневой папки
for task in running_tasks:
    print(task)
    print("="*50)  # Разделитель для визуального удобства
