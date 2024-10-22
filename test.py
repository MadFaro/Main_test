async def main():
    try:
        clear()
    except:
        pass
    session_info = json.dumps({
        k: str(getattr(info, k))
        for k in ['user_agent', 'user_language', 'server_host',
                'origin', 'user_ip', 'backend', 'protocol', 'request']
    }, indent=4)
    user_login = BotDS.user_exists_ip(str(json.loads(session_info)['user_ip']))
    if user_login == None:

        invalid_password_attempts = 0
            
        def validate_password(password):
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[a-zA-Z0-9!@#$%^&*()_+]{8,}$", password):
                return 'Пароль должен содержать не менее 8 символов и включать как минимум одну заглавную, одну строчную букву и один специальный символ'
        
        try:
            while invalid_password_attempts < 5:
                id_select = await input_group("Вход",
                                            [
                                input('Логин', name='tab', type=TEXT),
                                input('Пароль', name='password', type=PASSWORD),
                                actions(name='action', buttons=[
                                          {'label': 'Войти', 'value': 'login', 'color':'dark'},
                                          {'label': 'Регистрация', 'value': 'register', 'color':'success'},
                                      ])
                                            ])
                if id_select['action'] == 'register':
                    await register()
                elif id_select['action'] == 'login':
                    tab = str(id_select['tab']).upper()
                    block = BotDS.get_user_block(tab)
                    if int(block) == 0:
                        toast('Учетная запись заблокирована', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                    else:
                        password = str(hashlib.sha256(str(id_select['password']).encode()).hexdigest())
                        rezult = BotDS.user_exists(ID=tab)
                        def_pass = str(BotDS.get_def_pass())

                        if rezult == False:
                            toast('Неверный логин', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

                        elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == def_pass and password == def_pass:
                            id_select_2 = await input_group("Введи новый пароль",
                                                            [
                                            input('Пароль', name='password', type=PASSWORD, validate=validate_password)
                                                            ])
                            password_up = hashlib.sha256(str(id_select_2['password']).encode()).hexdigest()
                            BotDS.update_user_password(tab, password_up)
                            toast('Пароль обновлен', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                            run_js('window.location.reload()')

                        elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == password:

                            user_info = BotDS.get_user_mot(ID=tab)

                            if user_info[2] == 'noadmin':
                                BotDS.add_user_ip(login=tab, ip=str(json.loads(session_info)['user_ip']))
                                BotDS.add_log(login=tab, type_log = 'Вход')
                                await main_menu(sdep='noadmin', tab=tab, fio=user_info[1], id = user_info[0])

                            elif user_info[2] == 'admin':
                                BotDS.add_user_ip(login=tab, ip=str(json.loads(session_info)['user_ip']))
                                pass
                                await admin(sdep='admin', tab=tab, fio=user_info[1], id = user_info[0])

                            else:
                                toast('Нет прав', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

                            break

                        else:
                            invalid_password_attempts += 1
                            if invalid_password_attempts >= 5:
                                BotDS.block_user(tab, 0)
                                toast('Учетная запись заблокирована', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                            else:
                                toast('Неверный пароль', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

        except:
            clear()
            toast('Нет прав', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
    else:
        user_info = BotDS.get_user_mot(ID=user_login[0])
        if user_info[2] == 'noadmin':
            await main_menu(sdep='noadmin', tab=user_login[0], fio=user_info[1], id = user_info[0])
        elif user_info[2] == 'admin':
            await admin(sdep='admin', tab=user_login[0], fio=user_info[1], id = user_info[0])
        else:
            toast('Нет прав', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

# Функция для регистрации
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
        
    id_select_reg = await input_group("Регистрация",[
                                input('ФИО', name='fio_reg', type=TEXT),
                                input('Рабочая почта', name='tab_reg', type=TEXT, validate=validate_mail_reg),
                                select(name='gender', label='Выбери пол:', options=['М', 'Ж']),
                                input('Пароль', name='password_reg', type=PASSWORD, validate=validate_password_reg),
                                actions(name='action', buttons=[
                                          {'label': 'Зарегистрироваться', 'value': 'reg', 'color':'success'},
                                      ])
                                            ])
    if id_select_reg['action'] == 'reg':
        email = str(id_select_reg['tab_reg']).upper().replace(' ', '')
        def validate_aut_key_reg(aut_key):
            result = BotDS.get_user_aut(email)
            dt, stored_code = result
            if result is None:
                BotDS.delete_aut(email)
                return 'Ошибка при получении данных. Попробуйте снова.'
            if aut_key != stored_code:
                return 'Неверный код. Проверьте почту и введите код повторно'
            if datetime.now() - datetime.timedelta(hours=3) > dt + datetime.timedelta(minutes=10):
                return 'Код истёк. Повторите регистрацию'

        code = ''.join(random.choice('0123456789', 6))
        BotDS.delete_aut(email)
        BotDS.add_aut(login = email, code = code)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = code
        msg.attach(MIMEText(f"Ваш код для подтверждения {code}", 'plain'))
        
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.sendmail(sender_email, email, msg.as_string())
            toast(f"На почту {email} отправлено уведомление, действует 10 минут")
        except Exception as e:
            toast(f"Failed to send email: {e}")

    id_select_aut = await input_group("Подтверждение почты",[
                                input('Код', name='aut_key', type=TEXT, validate=validate_aut_key_reg),
                                actions(name='action', buttons=[
                                          {'label': 'Подтвердить', 'value': 'aut', 'color':'success'},
                                      ])
                                            ])
    if id_select_aut['action'] == 'aut':
        BotDS.register_user(
                password = str(hashlib.sha256(str(id_select_reg['password_reg']).encode()).hexdigest()), 
                sdep='noadmin', 
                login=str(id_select_reg['tab_reg']).upper().replace(' ', ''), 
                fio=id_select_reg['fio_reg'],
                status = 1,
                gender=id_select_reg['gender']
                )
        toast('Регистрация прошла успешно', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
