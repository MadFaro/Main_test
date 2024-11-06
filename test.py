conn = cx_Oracle.connect(user='', password='', dsn = '')
cursor = conn.cursor()
try:
    cursor.execute("drop table analytics.NP_application_tech_voronka")
except:
    pass

table_count = 0
count = 1
while table_count < 4:
    try:
        cursor.execute(f"create table analytics.NP_application_tech_voronka as Select /*+ PARALLEL(4) */ * from cmdm2.application")
        table_count = table_count + 11
    except:
        count = count + 1
        table_count = table_count + 1

try:
    cursor.execute("select /*+ PARALLEL(4) */ * from analytics.NP_application_tech_voronka")
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = 'Pop'
    mail.Subject = f'Обновление таблицы analytics.NP_application_tech_voronka {datetime.date.today().strftime("%d.%m.%Y")}'
    mail.HTMLBody = f"Привет!<BR>Таблица обновлена.<BR>Попыток было: {count}"
    mail.Send()
except Exception as errors:
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = 'Pop'
    mail.Subject = f'Ошибка при обновлении analytics.NP_application_tech_voronka {datetime.date.today().strftime("%d.%m.%Y")}'
    mail.HTMLBody = f'Ошибка - {str(errors)}<BR>Попыток было: {count}'
    mail.Send()        

# Принимаем изменения и закрываем коннект
cursor.close()
conn.commit()
conn.close()
