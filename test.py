cursor = conn.cursor()
cursor.execute("select VERSION from ANALYTICS.TOLOG_TEST1 where PLATFORM = 'ANDROID' and APP_ACT = 1")
# Переменная с текстом по умолчанию
last_app_android = cursor.fetchall()[0]
cursor.execute("select VERSION from ANALYTICS.TOLOG_TEST1 where PLATFORM = 'IOS' and APP_ACT = 1")
last_app_ios = cursor.fetchall()[0]
conn.close()
