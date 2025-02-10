# Авторизация
@config(theme = 'minty', css_style = css.container_output, description='ПОРТАЛ КЦ', title='ПОРТАЛ КЦ')
async def main():
    try:
        clear()
    except:
        pass
    key = str(BotDS.get_def_crypta())
    cipher_suite = Fernet(key.encode())
    user_login_token = await get_cookie("CC_s_12316274ndfydsfy273rnwjsf7213")
    if user_login_token == None:
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
                                            {'label': 'Сброс пароля', 'value': 'reset_pass', 'color':'warning'},
                                        ])
                                                ])
                if id_select['action'] == 'register':
                    await register()
                elif id_select['action'] == 'reset_pass':
                    await reset_pass()
                elif id_select['action'] == 'login':
                    tab = str(id_select['tab']).upper().replace(' ', '')
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
                                set_cookie("CC_s_12316274ndfydsfy273rnwjsf7213", cipher_suite.encrypt(str(tab).encode()).decode(), days=30)
                                BotDS.add_log(login=tab, type_log = 'Вход')
                                await main_menu(sdep='noadmin', tab=tab, fio=user_info[1], id = user_info[0])

                            elif user_info[2] == 'admin':
                                set_cookie("CC_s_12316274ndfydsfy273rnwjsf7213", cipher_suite.encrypt(str(tab).encode()).decode(), days=30)
                                await admin(sdep='admin', tab=tab, fio=user_info[1], id = user_info[0])

                            else:
                                toast('Ошибка при входе', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
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
            toast('Ошибка при входе', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
    else:
        try:
            user_token = str(cipher_suite.decrypt(str(user_login_token).encode()).decode()).upper()
            user_info_token = BotDS.get_user_mot(ID=user_token)
            if user_info_token[2] == 'noadmin':
                BotDS.add_log(login=user_token, type_log = 'Вход')
                await main_menu(sdep='noadmin', tab=user_token, fio=user_info_token[1], id = user_info_token[0])
            elif user_info_token[2] == 'admin':
                await admin(sdep='admin', tab=user_token, fio=user_info_token[1], id = user_info_token[0])
            else:
                toast('Ошибка при входе', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
        except:
            toast('Ошибка при входе', duration=10, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
