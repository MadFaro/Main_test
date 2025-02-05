import psycopg2

conn = psycopg2.connect(
    dbname="имя_вашей_базы_данных", 
    user="ваше_имя_пользователя", 
    password="ваш_пароль", 
    host="ip_сервера", 
    port="5432"
)
cursor = conn.cursor()
