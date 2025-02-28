AD_SERVER = "ldap://your.domain.com"  # Адрес контроллера домена
AD_USER = "your_username@your.domain.com"  # Учетная запись с правами на чтение
AD_PASSWORD = "your_password"
SEARCH_BASE = "DC=your,DC=domain,DC=com"  # Корень поиска в AD

# Имя компьютера, который ищем
PC_NAME = "PC12345"  # Замените на нужный номер ПК

# Подключаемся к серверу AD
server = Server(AD_SERVER, get_info=ALL)
conn = Connection(server, AD_USER, AD_PASSWORD, auto_bind=True)
