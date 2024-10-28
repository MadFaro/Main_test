from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import smtplib
import sqlite3
import pandas as pd

# Данные для отправки уведомлений на почту
smtp_server = ""
port = ""
sender_email = ""
shop_url = ""

# Данные для начисления
operation_type = "Начисление"
json = None
value_operation = 100
status_operation = "Исполнен"
on_read = 1

# Коннект в БД
db_path = r'C:\Users\TologonovAB\Desktop\shop_app\Convert\db\shop.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Выгружаем тех, у кого сегодня ДР
query = """
SELECT login
FROM users
WHERE strftime('%m-%d', birth_date) = strftime('%m-%d', 'now')
"""
df = pd.read_sql_query(query, conn)

# Путь к баннеру
banner_path = r'C:\Users\TologonovAB\Desktop\shop_app\Convert\banner.jpg'

# Добавляем операцию для каждого пользователя и отправляем уведомление на почту
for login_customer in df['login']:
    
    # Проверяем наличие токена для текущего пользователя
    token_query = """
    SELECT user_token 
    FROM tokens
    WHERE user_login = ?
    """
    cursor.execute(token_query, (login_customer,))
    token_result = cursor.fetchone()
    
    # Добавляем токен к URL, если он есть
    if token_result:
        token = token_result[0]
        personalized_url = f"{shop_url}?token={token}"
    else:
        personalized_url = shop_url

    # Добавляем запись в таблицу операций
    insert_query = """
        INSERT INTO operations (operation_type, json, login_customer, value_operation, status_operation, on_read)
        VALUES (?, ?, ?, ?, ?, ?)
        """
    cursor.execute(insert_query, (operation_type, json, login_customer, value_operation, status_operation, on_read))
    conn.commit()

    # Формируем письмо
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = login_customer
    msg['Subject'] = 'С днем рождения!'
    
    # HTML-контент письма с динамическим URL
    email_content = f"""<html>
                        <body>
                            <p>Добрый день!<br><br>
                            Ваш баланс был успешно пополнен на сумму: {value_operation}.<br><br>
                            <a href="{personalized_url}" target="_blank">Перейти в интернет магазин</a>
                            </p>
                            <img src="cid:banner">
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

# Закрываем соединение с БД
conn.close()
