import subprocess

def get_running_tasks_from_root():
    cmd = [
        'powershell',
        'Get-ScheduledTask -TaskPath "\" | Where-Object { $_.State -eq "Running" }'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return "Нет запущенных задач"

running_tasks = get_running_tasks_from_root()
print(running_tasks)

