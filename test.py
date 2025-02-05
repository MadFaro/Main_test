    def __init__(self, db_params):
        # Подключаемся к PostgreSQL
        self.conn = psycopg2.connect(
            dbname=db_params['dbname'],
            user=db_params['user'],
            password=db_params['password'],
            host=db_params['host'],
            port=db_params['port']
        )
        self.cursor = self.conn.cursor()

db_params = {
    'dbname': 'your_db_name',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

BotDS = BotDB(db_params)
