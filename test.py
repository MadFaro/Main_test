import pandas as pd
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

async def add_balans(df_user, sdep, tab, fio, id):
    try:
        clear()
        excel_file = await file_upload("Выберите Excel файл:", accept=".xlsx")
        with BytesIO(excel_file['content']) as buffer:
            df = pd.read_excel(buffer)
        
        # Добавляем нужные данные в DataFrame
        df['operation_type'] = 'Начисление'
        df['status_operation'] = 'Исполнен'
        df['json'] = None

        # Записываем данные в базу
        df[['login_customer', 'value_operation', 'operation_type', 'status_operation', 'json',
            'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9', 'case10', 'case11', 'case12', 'case13',
           ]].dropna(subset=['value_operation']).to_sql('operations', connect("Convert/db/shop.db"), if_exists='append', index=False)

        # Уведомляем об успешном начислении баланса
        popup('Баланс начислен')
        
        # Отправляем уведомления по email каждому пользователю
        smtp_server = 'your_smtp_server'
        sender_email = 'your_email'
        port = 587  # Порт для SMTP
        shop_url = "https://your-online-shop.com"  # Ссылка на интернет-магазин

        for index, row in df.iterrows():
            try:
                # Подготавливаем сообщение для каждого пользователя
                login_customer = row['login_customer']
                value_operation = row['value_operation']

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = login_customer
                msg['Subject'] = 'Ваш баланс пополнен'

                # Содержимое письма
                email_content = f"""
                Уважаемый клиент,<br><br>
                Ваш баланс был успешно пополнен на сумму: {value_operation}.<br>
                Спасибо за использование наших услуг!<br><br>
                <a href="{shop_url}" target="_blank">Перейти в интернет магазин</a><br><br>
                С уважением,<br>Ваша команда поддержки.
                """
                msg.attach(MIMEText(email_content, 'html'))

                # Отправка письма
                with smtplib.SMTP(smtp_server, port) as server:
                    server.sendmail(sender_email, login_customer, msg.as_string())

            except Exception as e:
                # Если произошла ошибка при отправке письма конкретному пользователю
                print(f"Ошибка отправки письма пользователю {login_customer}: {str(e)}")
        
        # Проверяем баланс пользователей
        await chek_balance_users(df_user, sdep, tab, fio, id)

    except Exception as e:
        toast(f'Error - что-то пошло не по плану: {str(e)}', duration=0, position='center', color='error', onclick=lambda: run_js('window.location.reload()'))
