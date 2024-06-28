import smtplib

def send_simple_email(smtp_server, smtp_port, username, password, from_addr, to_addr, subject, body):
    try:
        # Формируем сообщение
        message = f"Subject: {subject}\n\n{body}"
        
        # Настраиваем соединение с SMTP-сервером
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Начинаем TLS-сессию
            server.login(username, password)
            server.sendmail(from_addr, to_addr, message)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Параметры для отправки письма
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_password'
from_addr = 'your_email@example.com'
to_addr = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email.'

# Отправка письма
send_simple_email(smtp_server, smtp_port, username, password, from_addr, to_addr, subject, body)
