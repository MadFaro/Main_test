import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "your_smtp_ip_or_dns"
port = 23  # Указанный порт

sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
subject = "Test email"
body = "This is a test email sent via SMTP server without authentication."

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP(smtp_server, port) as server:
        # Без вызова server.login(), так как аутентификация не требуется
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")

