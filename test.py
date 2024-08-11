import win32com.client
import pandas as pd

# Инициализация COM-объекта Планировщика задач
scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()

# Получение основной папки "Библиотека планировщика заданий"
folder = scheduler.GetFolder('\\')

# Функция для получения типа триггера
def get_trigger_type(trigger):
    trigger_type_map = {
        1: "Ежедневно",
        2: "Еженедельно",
        3: "Ежемесячно",
        4: "Однократно",
        5: "При входе в систему",
        6: "При регистрации пользователя",
        7: "По времени простоя",
        8: "При событии"
    }
    
    return trigger_type_map.get(trigger.Type, "Неизвестный тип")

# Функция для получения даты и времени запуска
def get_trigger_datetime(trigger):
    if trigger.Type in (1, 2, 3, 4):  # Если это дата-время триггер
        start_boundary = trigger.StartBoundary
        return start_boundary
    else:
        return "Не указано"

# Функция для получения информации о задаче
def get_task_info(task):
    task_name = task.Name
    is_enabled = "Включена" if task.Enabled else "Отключена"
    
    trigger_types = []
    trigger_datetimes = []
    
    for trigger in task.Definition.Triggers:
        trigger_types.append(get_trigger_type(trigger))
        trigger_datetimes.append(get_trigger_datetime(trigger))
    
    # Присоединяем списки в строки
    trigger_types = '; '.join(trigger_types) if trigger_types else 'Нет триггеров'
    trigger_datetimes = '; '.join(trigger_datetimes) if trigger_datetimes else 'Нет даты/времени'

    actions_info = []
    for action in task.Definition.Actions:
        actions_info.append(action.Path + ' ' + action.Arguments)
    actions_info = '; '.join(actions_info) if actions_info else 'Нет действий'
    
    return {
        "Название задачи": task_name,
        "Состояние": is_enabled,
        "Тип триггера": trigger_types,
        "Дата и время запуска": trigger_datetimes,
        "Действие(я)": actions_info
    }

# Извлекаем задачи из основной папки
tasks_info = []
tasks = folder.GetTasks(0)
for task in tasks:
    tasks_info.append(get_task_info(task))

# Создаем DataFrame для удобного представления данных
df = pd.DataFrame(tasks_info)

# Сохраняем данные в Excel-файл
df.to_excel('tasks_info.xlsx', index=False)

print("Данные успешно выгружены в файл tasks_info.xlsx")

