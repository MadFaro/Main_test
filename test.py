import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import os

def send_email_with_shortcut(to_email, subject, body, shortcut_file):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = to_email
    msg['Subject'] = subject

    # Добавление текста в письмо
    msg.attach(MIMEText(body, 'plain'))

    # Добавление вложения (ярлык)
    with open(shortcut_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(shortcut_file)}')
        msg.attach(part)

    # Отправка письма
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, to_email, msg.as_string())

# Пример использования
token = generate_unique_token()
url = f"https://yourwebsite.com/login?token={token}"

# Создаем ярлык
shortcut_filename = "login_shortcut.url"
create_shortcut(shortcut_filename, url)

# Отправляем почту с ярлыком
send_email_with_shortcut('recipient_email@gmail.com', 'Ваш ярлык для входа', 'Вот ваш ярлык для входа на сайт.', shortcut_filename)

