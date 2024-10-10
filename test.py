import subprocess

def get_running_tasks():
    # Запуск команды SCHTASKS для получения списка задач и фильтрации по статусу "Running"
    cmd = ['SCHTASKS', '/Query', '/FO', 'LIST', '/V']
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Фильтруем строки, содержащие статус "Running"
        running_tasks = [line for line in result.stdout.splitlines() if "Running" in line]
        return running_tasks
    else:
        # В случае ошибки возвращаем сообщение об ошибке
        return result.stderr

running_tasks = get_running_tasks()
for task in running_tasks:
    print(task)
