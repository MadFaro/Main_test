import subprocess

def get_running_tasks():
    # Запуск команды PowerShell для получения списка выполняющихся задач
    cmd = ['powershell', 'Get-ScheduledTask | Where-Object { $_.State -eq "Running" }']
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Возвращаем список выполняющихся задач
        return result.stdout
    else:
        # В случае ошибки возвращаем сообщение об ошибке
        return result.stderr

running_tasks = get_running_tasks()
print(running_tasks)
