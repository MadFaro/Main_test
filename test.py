import msoffcrypto
import io

# Откройте защищенный файл
with open('защищенный_файл.xlsx', 'rb') as file:
    decrypted = io.BytesIO()
    office_file = msoffcrypto.OfficeFile(file)
    office_file.load_key(password="2011")  # Укажите пароль
    office_file.decrypt(decrypted)

    # Сохраните файл без пароля
    with open('файл_без_пароля.xlsx', 'wb') as output_file:
        output_file.write(decrypted.getvalue())

