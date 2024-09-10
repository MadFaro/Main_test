import socket
import json

def get_client_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

# Получение IP-адреса клиента (например, через PyWebIO)
client_ip = "192.168.1.1"  # это замените на вашу переменную с IP-адресом клиента

# Получение сетевого имени клиента
client_hostname = get_client_hostname(client_ip)

# Собираем всю информацию
session_info = {
    k: str(getattr(info, k))
    for k in ['user_agent', 'user_language', 'server_host',
              'origin', 'user_ip', 'backend', 'protocol', 'request']
}
session_info['client_hostname'] = client_hostname

# Преобразование в JSON
session_info_json = json.dumps(session_info, indent=4)

print(session_info_json)
