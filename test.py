# Функция для генерации уникального токена
def generate_unique_token(length=32):
    return secrets.token_hex(length)

# Функция для проверки уникальности токена
def is_token_unique(token, cursor):
    cursor.execute("SELECT COUNT(1) FROM users WHERE token = ?", (token,))
    return cursor.fetchone()[0] == 0

# Основная логика генерации токена
def create_token(cursor):
    token = generate_unique_token()
    while not is_token_unique(token, cursor):
        token = generate_unique_token()
    return token
