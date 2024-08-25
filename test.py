from ftplib import FTP

ftp = FTP('your_server_ip')
ftp.login(user='username', passwd='password')

# Загрузка файла
with open('local_file.txt', 'rb') as f:
    ftp.storbinary('STOR remote_file.txt', f)

ftp.quit()

