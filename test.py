import os
import subprocess

# Папка для сохранения задач
export_folder = "C:\\backup\\tasks"

# Создаем папку для экспорта, если она не существует
os.makedirs(export_folder, exist_ok=True)

# Команда для получения задач из корня "Библиотеки планировщика заданий" без подпапок
get_tasks_command = '''
Get-ScheduledTask |
Where-Object { $_.TaskPath -eq "\\" } |
ForEach-Object { $_.TaskName }
'''

# Выполняем PowerShell команду для получения списка задач
tasks = subprocess.run(["powershell", "-Command", get_tasks_command], capture_output=True, text=True).stdout.splitlines()

# Экспортируем каждую задачу
for task in tasks:
    if task:  # Проверка на пустую строку
        export_command = f'Export-ScheduledTask -TaskName "{task}" -TaskPath "\\" -Path "{export_folder}\\{task}.xml"'
        subprocess.run(["powershell", "-Command", export_command], capture_output=True, text=True)

print(f"Задачи из корневой папки экспортированы в папку {export_folder}")
