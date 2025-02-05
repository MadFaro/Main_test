import pandas as pd
from sqlalchemy import create_engine

# Создание строки подключения для PostgreSQL
db_params = {
    'dbname': 'your_db_name',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

# Формирование строки подключения для SQLAlchemy
connection_string = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"

# Создание engine SQLAlchemy
engine = create_engine(connection_string)
