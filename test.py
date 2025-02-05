from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import psycopg2
import pandas as pd

# Данные для отправки уведомлений на почту
smtp_server = ""
port = 25
sender_email = ""
shop_url = ""

# Данные для начисления
operation_type = "Начисление"
json = None
value_operation = 50
status_operation = "Исполнен"
on_read = 1

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="your_database_name", 
    user="your_username", 
    password="your_password", 
    host="localhost"
)
cursor = conn.cursor()

# Выгружаем тех, у кого сегодня ДР
query = """
SELECT login
FROM users
WHERE TO_CHAR(birth_date, 'MM-DD') = TO_CHAR(NOW(), 'MM-DD')
"""
df = pd.read_sql_query(query, conn)

# Путь к баннеру
banner_path = r'C:\Users\TologonovAB\Desktop\shop_app\sys_img\ban_birth.jpg'

# Добавляем операцию для каждого пользователя и отправляем уведомление на почту
for login_customer in df['login']:

    # Добавляем запись в таблицу операций
    insert_query = """
        INSERT INTO operations (operation_type, json, login_customer, value_operation, status_operation, on_read)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
    cursor.execute(insert_query, (operation_type, json, login_customer, value_operation, status_operation, on_read))
    conn.commit()

    try:
        # Формируем письмо
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = login_customer
        msg['Subject'] = 'С Днем Рождения!'

        # HTML-контент письма с динамическим URL
        email_content = f"""<html>
                            <body>
                                <img src="cid:banner"><br>
                                <a href="{shop_url}" target="_blank">Перейти в интернет магазин</a>
                            </body>
                            </html>
                        """
        msg.attach(MIMEText(email_content, 'html'))

        # Добавляем баннер в письмо
        with open(banner_path, 'rb') as banner_file:
            img = MIMEImage(banner_file.read())
            img.add_header('Content-ID', '<banner>')
            msg.attach(img)

        # Отправка письма
        with smtplib.SMTP(smtp_server, port) as server:
            server.sendmail(sender_email, login_customer, msg.as_string())
    except Exception as e:
        print(f"Ошибка при отправке письма пользователю {login_customer}: {e}")
        pass

# Закрываем соединение с БД
conn.close()
