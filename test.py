from ldap3 import Server, Connection, ALL

# Параметры подключения к AD
AD_SERVER = "ldap://your.domain.com"  # Адрес контроллера домена
AD_USER = "your_username@your.domain.com"  # Учетная запись с правами на чтение
AD_PASSWORD = "your_password"
SEARCH_BASE = "DC=your,DC=domain,DC=com"  # Корень поиска в AD

# Имя компьютера, который ищем
PC_NAME = "PC12345"  # Замените на нужный номер ПК

# Подключаемся к серверу AD
server = Server(AD_SERVER, get_info=ALL)
conn = Connection(server, AD_USER, AD_PASSWORD, auto_bind=True)

# Выполняем поиск компьютера
search_filter = f"(cn={PC_NAME})"  # Или можно использовать (sAMAccountName={PC_NAME}$)
attributes = ["cn", "distinguishedName", "lastLogonTimestamp", "operatingSystem", "whenCreated"]

conn.search(SEARCH_BASE, search_filter, attributes=attributes)

# Выводим результат
if conn.entries:
    for entry in conn.entries:
        print(entry)
else:
    print(f"Компьютер {PC_NAME} не найден в AD.")

# Закрываем соединение
conn.unbind()

