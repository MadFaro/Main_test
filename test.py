        def validate_aut_key_reg(aut_key):
            result = BotDS.get_user_aut(email)
            if result is None:
                BotDS.delete_aut(email)
                return 'Ошибка при получении данных. Повторите регистрацию.'
            elif hashlib.sha256(str(aut_key).encode()).hexdigest() != result[0]:
                return 'Неверный код. Проверьте почту и введите код повторно.'
            elif datetime.strptime(result[1], "%Y-%m-%d %H:%M:%S") + timedelta(minutes=10) < datetime.now() - timedelta(hours=3):
                BotDS.delete_aut(email)
                return 'Истекло время. Повторите регистрацию.'
