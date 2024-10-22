def validate_aut_key_reg(aut_key):
    # Получаем сгенерированный код и время его создания для данного email
    result = BotDS.get_user_aut(email)

    if result is None:
        return 'Ошибка при получении данных. Попробуйте снова.'

    dt, stored_code = result

    # Проверяем, совпадает ли введённый код с тем, что хранится в базе
    if aut_key != stored_code:
        return 'Неверный код. Проверьте почту и введите код повторно'

    # Если код совпадает, возвращаем None, что означает успешную валидацию
    return None
