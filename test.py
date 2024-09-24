import os
import subprocess

# Папка для сохранения задач
export_folder = "C:\\backup\\tasks"

# Создаем папку для экспорта, если она не существует
os.makedirs(export_folder, exist_ok=True)

# Получаем список задач с помощью PowerShell
get_tasks_command = "Get-ScheduledTask | ForEach-Object { $_.TaskName }"
tasks = subprocess.run(["powershell", "-Command", get_tasks_command], capture_output=True, text=True).stdout.splitlines()

# Экспортируем каждую задачу
for task in tasks:
    # Формируем команду экспорта
    export_command = f'Export-ScheduledTask -TaskName "{task}" -TaskPath "\\" -Path "{export_folder}\\{task}.xml"'
    
    # Выполняем команду через PowerShell
    subprocess.run(["powershell", "-Command", export_command], capture_output=True, text=True)
    
print(f"Все задачи экспортированы в папку {export_folder}")

