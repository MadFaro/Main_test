import cx_Oracle
import win32com.client
import datetime

# Подключение к базе данных
conn = cx_Oracle.connect(user='', password='', dsn='')
cursor = conn.cursor()

# Попытка удаления таблицы
try:
    cursor.execute("drop table analytics.NP_application_tech_voronka")
except:
    pass  # Игнорируем ошибку, если таблица не существует

# Попытка создания таблицы, максимум 5 попыток
max_attempts = 5
success = False

for attempt in range(1, max_attempts + 1):
    try:
        cursor.execute(f"create table analytics.NP_application_tech_voronka as Select /*+ PARALLEL(4) */ * from cmdm2.application")
        success = True
        break  # Выход из цикла при успешном выполнении
    except Exception as e:
        last_error = e  # Сохраняем последнюю ошибку

# Создание и отправка письма через Outlook
outlook = win32com.client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)
mail.To = 'Pop'
current_date = datetime.date.today().strftime("%d.%m.%Y")

if success:
    mail.Subject = f'Обновление таблицы analytics.NP_application_tech_voronka {current_date}'
    mail.HTMLBody = f"Привет!<BR>Таблица обновлена.<BR>Попыток было: {attempt}"
else:
    mail.Subject = f'Ошибка при обновлении analytics.NP_application_tech_vоронка {current_date}'
    mail.HTMLBody = f'Ошибка - {str(last_error)}<BR>Попыток было: {max_attempts}'

mail.Send()

# Закрываем курсор и соединение
cursor.close()
conn.commit()
conn.close()
