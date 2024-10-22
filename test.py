import datetime
from datetime import timedelta

# ... Ваш код ...

async def register():
    try:
        clear()
    except:
        pass

    def validate_password_reg(password):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[a-zA-Z0-9!@#$%^&*()_+]{8,}$", password):
            return 'Пароль должен содержать не менее 8 символов и включать как минимум одну заглавную, одну строчную букву и один специальный символ'
    
    def validate_mail_reg(mail):
        if 'uralsib' not in mail:
            return 'Укажи рабочую почту'
        elif BotDS.user_exists(ID=str(mail).upper().replace(' ', '')):
            return 'Такая почта уже зарегистрирована'
    
    id_select_reg = await input_group("Регистрация", [
        input('ФИО', name='fio_reg', type=TEXT),
        input('Рабочая почта', name='tab_reg', type=TEXT, validate=validate_mail_reg),
        select(name='gender', label='Выбери пол:', options=['М', 'Ж']),
        input('Пароль', name='password_reg', type=PASSWORD, validate=validate_password_reg),
        actions(name='action', buttons=[
            {'label': 'Зарегистрироваться', 'value': 'reg', 'color': 'success'},
        ])
    ])
    
    if id_select_reg['action'] == 'reg':
        email = str(id_select_reg['tab_reg']).upper().replace(' ', '')
        
        def validate_aut_key_reg(aut_key):
            result = BotDS.get_user_aut(email)
            
            if result is None:
                BotDS.delete_aut(email)
                return 'Ошибка при получении данных. Попробуйте снова.'
            
            dt, stored_code = result
            
            if aut_key != stored_code:
                return 'Неверный код. Проверьте почту и введите код повторно'
            
            # Проверка на истечение времени с учетом часового пояса
            if datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))) > dt + timedelta(minutes=10):
                return 'Код истёк. Повторите регистрацию'

        code = ''.join(random.choice('0123456789') for _ in range(6))  # Генерация 6-значного кода
        BotDS.delete_aut(email)
        BotDS.add_aut(login=email, code=code)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Код подтверждения"
        msg.attach(MIMEText(f"Ваш код для подтверждения: {code}", 'plain'))
        
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.sendmail(sender_email, email, msg.as_string())
            toast(f"На почту {email} отправлено уведомление, действует 10 минут")
        except Exception as e:
            toast(f"Не удалось отправить email: {e}")

        id_select_aut = await input_group("Подтверждение почты", [
            input('Код', name='aut_key', type=TEXT, validate=validate_aut_key_reg),
            actions(name='action', buttons=[
                {'label': 'Подтвердить', 'value': 'aut', 'color': 'success'},
            ])
        ])
        
        if id_select_aut['action'] == 'aut':
            BotDS.register_user(
                password=str(hashlib.sha256(str(id_select_reg['password_reg']).encode()).hexdigest()), 
                sdep='noadmin', 
                login=str(id_select_reg['tab_reg']).upper().replace(' ', ''), 
                fio=id_select_reg['fio_reg'],
                status=1,
                gender=id_select_reg['gender']
            )
            toast('Регистрация прошла успешно', duration=10, position='center', color='error', onclick=lambda: run_js('window.location.reload()'))
