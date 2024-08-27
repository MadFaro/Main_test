cursor = conn.cursor()
cursor.execute("""
    SELECT 
        PLATFORM,
        VERSION
    FROM 
        ANALYTICS.TOLOG_TEST1 
    WHERE 
        PLATFORM IN ('ANDROID', 'IOS') 
        AND APP_ACT = 1
""")
result = cursor.fetchall()
conn.close()

# Обрабатываем результат
last_app_android = None
last_app_ios = None

for row in result:
    if row[0] == 'ANDROID':
        last_app_android = row[1]
    elif row[0] == 'IOS':
        last_app_ios = row[1]

print(f"Android version: {last_app_android}")
print(f"iOS version: {last_app_ios}")
