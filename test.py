import subprocess
import json

def get_running_tasks_from_root():
    # Команда PowerShell для получения выполняющихся задач из корневой папки
    cmd = [
        'powershell',
        '-Command', 
        'Get-ScheduledTask | Where-Object { $_.State -eq "Running" -and $_.TaskPath -eq "\\" } | Select-Object TaskName, TaskPath, State | ConvertTo-Json'
    ]
    
    # Запуск PowerShell с явной установкой кодировки UTF-8
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    if result.returncode == 0:
        # Возвращаем JSON-данные, которые нужно обработать
        return result.stdout
    else:
        # В случае ошибки возвращаем сообщение об ошибке
        return result.stderr

def format_tasks_for_email(tasks_output):
    try:
        # Парсим JSON результат
        tasks = json.loads(tasks_output)
        
        # Если только одна задача, она будет словарем, иначе это будет список словарей
        if isinstance(tasks, dict):
            tasks = [tasks]
        
        # Добавляем заголовки и форматируем задачи в таблицу
        formatted_output = "Список выполняющихся задач в корневой папке:\n\n"
        formatted_output += "{:<30} {:<20} {:<10}\n".format("Имя задачи", "Путь", "Статус")
        formatted_output += "="*60 + "\n"
        
        # Форматируем каждую задачу
        for task in tasks:
            formatted_output += "{:<30} {:<20} {:<10}\n".format(task['TaskName'], task['TaskPath'], task['State'])
        
        return formatted_output
    
    except json.JSONDecodeError:
        return "Ошибка при разборе данных задач"

# Получаем выполняющиеся задачи из корневой папки
running_tasks = get_running_tasks_from_root()

# Форматируем результат для вставки в письмо
formatted_tasks = format_tasks_for_email(running_tasks)

# Выводим отформатированные задачи (для вставки в письмо Outlook)
print(formatted_tasks)

