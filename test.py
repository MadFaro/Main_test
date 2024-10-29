from cryptography.fernet import Fernet

# Генерация ключа для шифрования (сохрани его для использования в будущем)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_user_id(user_id: str) -> str:
    """Шифрует user_id."""
    return cipher_suite.encrypt(user_id.encode()).decode()

def decrypt_user_id(encrypted_user_id: str) -> str:
    """Дешифрует user_id."""
    return cipher_suite.decrypt(encrypted_user_id.encode()).decode()
