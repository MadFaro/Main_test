import subprocess

def get_running_tasks_from_root():
    # Команда PowerShell для получения выполняющихся задач из корневой папки с кодировкой UTF-8
    cmd = [
        'powershell',
        '-Command', 
        'Get-ScheduledTask | Where-Object { $_.State -eq "Running" -and $_.TaskPath -eq "\\" } | Format-Table TaskName,TaskPath,State'
    ]
    
    # Запуск PowerShell с явной установкой кодировки UTF-8
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    if result.returncode == 0:
        # Возвращаем вывод в виде текста
        return result.stdout
    else:
        # Возвращаем сообщение об ошибке в случае проблемы
        return result.stderr

def format_tasks_for_email(tasks_output):
    # Разбиваем задачи на строки
    lines = tasks_output.strip().splitlines()
    
    # Добавляем заголовки для письма и форматируем задачи в таблицу
    formatted_output = "Список выполняющихся задач в корневой папке:\n\n"
    formatted_output += "{:<30} {:<20} {:<10}\n".format("Имя задачи", "Путь", "Статус")
    formatted_output += "="*60 + "\n"
    
    for line in lines[3:]:  # Пропускаем первые строки с метаданными таблицы
        formatted_output += line + "\n"
    
    return formatted_output

# Получаем выполняющиеся задачи из корневой папки
running_tasks = get_running_tasks_from_root()

# Форматируем результат для вставки в письмо
formatted_tasks = format_tasks_for_email(running_tasks)

# Выводим отформатированные задачи (для вставки в письмо Outlook)
print(formatted_tasks)

