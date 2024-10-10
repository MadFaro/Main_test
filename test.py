import subprocess

def get_running_tasks_from_root():
    # Команда PowerShell для получения выполняющихся задач из корневой папки
    cmd = [
        'powershell',
        'Get-ScheduledTask | Where-Object { $_.State -eq "Running" -and $_.TaskPath -eq "\\" }'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Возвращаем список выполняющихся задач из корневой папки
        return result.stdout
    else:
        # В случае ошибки возвращаем сообщение об ошибке
        return result.stderr

running_tasks = get_running_tasks_from_root()
print(running_tasks)
