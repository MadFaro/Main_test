    def user_exists_ip(self, ID):
        try:
            result = self.cursor.execute("SELECT `user_login` FROM `session` WHERE `user_ip` = ?", (ID,))
            if bool(len(result.fetchall())) == False:
                return None
            else:
                return result.fetchone()[0]
        except sqlite3.Error:
            return None
    def add_user_ip(self, login, ip):
        try:
            self.cursor.execute('INSERT INTO `session` (`user_ip`, `user_login`) VALUES (?,?)', (login, ip))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
async def main():

    session_info = json.dumps({
        k: str(getattr(info, k))
        for k in ['user_agent', 'user_language', 'server_host',
                'origin', 'user_ip', 'backend', 'protocol', 'request']
    }, indent=4)
    user_login = BotDS.user_exists_ip(json.loads(session_info)['user_ip'])
    if user_login == None:

        invalid_password_attempts = 0

        def validate_login(tab):
            if BotDS.user_exists(ID=tab) == False:
                return 'Логин не существует'
            
        def validate_password(password):
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[a-zA-Z0-9!@#$%^&*()_+]{8,}$", password):
                return 'Пароль должен содержать не менее 8 символов и включать как минимум одну заглавную, одну строчную букву и один специальный символ'
        
        try:
            while invalid_password_attempts < 5:
                id_select = await input_group("Вход",
                                            [
                                input('Логин', name='tab', type=TEXT, validate=validate_login),
                                input('Пароль', name='password', type=PASSWORD)
                                            ])
                tab = id_select['tab']
                block = BotDS.get_user_block(tab)
                if int(block) == 0:
                    toast('Учетная запись заблокирована', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                else:
                    password = str(hashlib.sha256(str(id_select['password']).encode()).hexdigest())
                    rezult = BotDS.user_exists(ID=tab)
                    def_pass = str(BotDS.get_def_pass())

                    if rezult == False:
                        toast('Неверный логин', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

                    elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == def_pass and password == def_pass:
                        id_select_2 = await input_group("Введи новый пароль",
                                                        [
                                        input('Пароль', name='password', type=PASSWORD, validate=validate_password)
                                                        ])
                        password_up = hashlib.sha256(str(id_select_2['password']).encode()).hexdigest()
                        BotDS.update_user_password(tab, password_up)
                        toast('Пароль обновлен', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                        run_js('window.location.reload()')

                    elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == password:

                        user_info = BotDS.get_user_mot(ID=tab)

                        if user_info[2] == 'noadmin':
                            BotDS.add_user_ip(login=tab, ip=json.loads(session_info)['user_ip'])
                            await noadmin(sdep='noadmin', tab=tab, fio=user_info[1], id = user_info[0])

                        elif user_info[2] == 'admin':
                            await admin(sdep='admin', tab=tab, fio=user_info[1], id = user_info[0])

                        else:
                            toast('Нет прав', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

                        break

                    else:
                        invalid_password_attempts += 1
                        if invalid_password_attempts >= 5:
                            BotDS.block_user(tab, 0)
                            toast('Учетная запись заблокирована', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                        else:
                            toast('Неверный пароль', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

        except:
            clear()
            toast('Нет прав', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
    else:
        user_info = BotDS.get_user_mot(ID=user_login)
        if user_info[2] == 'noadmin':
            await noadmin(sdep='noadmin', tab=tab, fio=user_info[1], id = user_info[0])
        elif user_info[2] == 'admin':
            await admin(sdep='admin', tab=tab, fio=user_info[1], id = user_info[0])
        else:
            toast('Нет прав', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
