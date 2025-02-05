import psycopg2
from psycopg2 import sql

class BotDB:

    def __init__(self, db_config):
        # Connect to PostgreSQL database
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()

    def user_exists(self, ID):
        try:
            self.cursor.execute("SELECT 1 FROM users WHERE login = %s", (ID,))
            return bool(len(self.cursor.fetchall()))
        except psycopg2.Error:
            return False
        
    def user_exists_ip(self, ID):
        try:
            self.cursor.execute("SELECT user_login FROM session WHERE user_ip = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None
        
    def add_user_ip(self, login, ip):
        try:
            self.cursor.execute('INSERT INTO session (user_login, user_ip) VALUES (%s, %s)', (login, ip))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
                       
    def get_user_pass(self, ID):
        try:
            self.cursor.execute("SELECT pass FROM users WHERE login = %s", (ID,))
            return self.cursor.fetchone()[0]
        except psycopg2.Error:
            return None
        
    def get_user_aut(self, ID):
        try:
            self.cursor.execute("SELECT authen_key, dt FROM authen WHERE login = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None
                        
    def get_user_block(self, ID):
        try:
            self.cursor.execute("SELECT status FROM users WHERE login = %s", (ID,))
            return self.cursor.fetchone()[0]
        except psycopg2.Error:
            return None
        
    def get_user_mot(self, ID):
        try:
            self.cursor.execute("SELECT index, fio, sdep FROM users WHERE login = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None
        
    def get_user_balanse(self, ID):
        try:
            self.cursor.execute("SELECT sum(value_operation) FROM operations WHERE login_customer = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None
        
    def get_basket_count(self, ID):
        try:
            self.cursor.execute("SELECT count(*) FROM basket WHERE login = %s", (ID,))
            return self.cursor.fetchone()[0]
        except psycopg2.Error:
            return None
               
    def get_order_count(self, ID):
        try:
            self.cursor.execute("SELECT count(*) FROM operations WHERE status_operation = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None

    def get_question_count(self, ID):
        try:
            self.cursor.execute("SELECT count(*) FROM question WHERE state = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None
        
    def get_offer_count(self, ID):
        try:
            self.cursor.execute("SELECT count(*) FROM offer_box WHERE state = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None
        
    def get_mood_count(self, ID):
        try:
            self.cursor.execute("SELECT count(*) FROM mood_box WHERE state = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None 
        
    def get_advt_count(self, ID):
        try:
            self.cursor.execute("SELECT count(*) FROM advt WHERE moderation = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None 
                               
    def get_user_last_operation(self, ID):
        try:
            self.cursor.execute("SELECT max(datetime_insert), operation_type, value_operation FROM operations WHERE login_customer = %s", (ID,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None 
        
    def get_user_gender(self, fio):
        try:
            self.cursor.execute("SELECT gender FROM users WHERE fio = %s", (fio,))
            return self.cursor.fetchone()
        except psycopg2.Error:
            return None  

    def add_discount(self, name, img):
        try:
            self.cursor.execute('INSERT INTO discount (name, img) VALUES (%s, %s)', (name, img))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False        

    def add_user(self, password, sdep, login, fio, status, gender, birth_date):
        try:
            self.cursor.execute('INSERT INTO users (pass, sdep, login, fio, status, gender, birth_date) VALUES (%s, %s, %s, %s, %s, %s, %s)', 
                                (password, sdep, login, fio, status, gender, birth_date))
            self.cursor.execute('INSERT INTO operations (operation_type, json, login_customer, value_operation, status_operation, on_read) VALUES (%s, %s, %s, %s, %s, %s)', 
                                ('test', None, login, 0, 'test', 0))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False

    def register_user(self, password, sdep, login, fio, status, gender, birth_date):
        return self.add_user(password, sdep, login, fio, status, gender, birth_date)

    def add_product(self, id, name, description, price, img, color, size, prom):
        try:
            self.cursor.execute('INSERT INTO product (id, name, description, price, img, color, size, prom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
                                (id, name, description, price, img, color, size, prom))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False

    def add_aut(self, login, code):
        try:
            self.cursor.execute('INSERT INTO authen (login, authen_key) VALUES (%s, %s)', (login, code))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def add_log(self, login, type_log):
        try:
            self.cursor.execute('INSERT INTO log (login, type_log) VALUES (%s, %s)', (login, type_log))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def delete_product(self, ID):
        try:
            self.cursor.execute("DELETE FROM product WHERE id = %s", (ID,))
            self.cursor.execute("DELETE FROM basket WHERE product_id = %s", (ID,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
    
    def delete_user(self, ID):
        try:
            self.cursor.execute("DELETE FROM users WHERE index = %s", (ID,))
            self.conn.commit()
            return True 
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def delete_user_token(self, ID):
        try:
            self.cursor.execute("DELETE FROM tokens WHERE user_login = %s", (ID,))
            self.conn.commit()
            return True 
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def delete_aut(self, login):
        try:
            self.cursor.execute("DELETE FROM authen WHERE login = %s", (login,))
            self.conn.commit()
            return True 
        except psycopg2.Error:
            self.conn.rollback()
            return False
