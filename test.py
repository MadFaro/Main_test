import psycopg2
from psycopg2 import sql


class BotDB:

    def __init__(self, db_params):
        try:
            self.conn = psycopg2.connect(**db_params)
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"Error: Unable to connect to the database. {e}")

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
            self.cursor.execute("INSERT INTO session (user_login, user_ip) VALUES (%s, %s)", (login, ip))
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
            self.cursor.execute("INSERT INTO discount (name, img) VALUES (%s, %s)", (name, img))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False        

    def add_user(self, password, sdep, login, fio, status, gender, birth_date):
        try:
            self.cursor.execute("INSERT INTO users (pass, sdep, login, fio, status, gender, birth_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                (password, sdep, login, fio, status, gender, birth_date))
            self.cursor.execute("INSERT INTO operations (operation_type, json, login_customer, value_operation, status_operation, on_read) VALUES (%s, %s, %s, %s, %s, %s)", 
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
            self.cursor.execute("INSERT INTO product (id, name, description, price, img, color, size, prom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                                (id, name, description, price, img, color, size, prom))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False

    def add_aut(self, login, code):
        try:
            self.cursor.execute("INSERT INTO authen (login, authen_key) VALUES (%s, %s)", (login, code))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def add_log(self, login, type_log):
        try:
            self.cursor.execute("INSERT INTO log (login, type_log) VALUES (%s, %s)", (login, type_log))
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
                 
    def delete_session(self, ID):
        try:
            self.cursor.execute("DELETE FROM session WHERE user_login = %s", (ID,))
            self.conn.commit()
            return True 
        except psycopg2.Error:
            self.conn.rollback()
            return False
            
    def delete_order(self, ID):
        try:
            self.cursor.execute("DELETE FROM operations WHERE id = %s", (ID,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def delete_one_product_basket(self, ID, Login, size, color):
        try:
            self.cursor.execute("DELETE FROM basket WHERE product_id = %s AND login = %s AND size = %s AND color = %s", 
                                (ID, Login, size, color))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
                
    def delete_all_product_basket(self, Login):
        try:
            self.cursor.execute("DELETE FROM basket WHERE login = %s", (Login,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False

    def delete_discount(self, ID):
        try:
            self.cursor.execute("DELETE FROM discount WHERE id = %s", (ID,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False 
                
    def add_operation(self, operation_type, json, login_customer, value_operation, status_operation, on_read):
        try:
            self.cursor.execute("INSERT INTO operations (operation_type, json, login_customer, value_operation, status_operation, on_read) VALUES (%s, %s, %s, %s, %s, %s)", 
                                (operation_type, json, login_customer, value_operation, status_operation, on_read))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False   
               
    def add_box_question(self, tab, fio, msg, state, category):
        try:
            self.cursor.execute("INSERT INTO question (fio, msg, state, category, login) VALUES (%s, %s, %s, %s, %s)", 
                                (fio, msg, state, category, tab))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False    

    def add_box_offer(self, tab, fio, offer, state, fio_bd):
        try:
            self.cursor.execute("INSERT INTO offer_box (fio, offer, state, fio_bd, login) VALUES (%s, %s, %s, %s, %s)", 
                                (fio, offer, state, fio_bd, tab))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False  

    def add_advt(self, fio, login, phone, category, city, name, text_ad, file_ad, moderation):
        try:
            self.cursor.execute("INSERT INTO advt (fio, login, phone, category, city, name, text_ad, file_ad, moderation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                (fio, login, phone, category, city, name, text_ad, file_ad, moderation))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False  

    def update_advt(self, id):
        try:
            self.cursor.execute("UPDATE advt SET date_ad = NOW() WHERE id = %s", (id,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def update_advt_admin(self, id):
        try:
            self.cursor.execute("UPDATE advt SET moderation = 1 WHERE id = %s", (id,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
                 
    def delete_advt(self, id):
        try:
            self.cursor.execute("DELETE FROM advt WHERE id = %s", (id,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False   
                     
    def add_box_mood(self, tab, fio, mood, state):
        try:
            self.cursor.execute("INSERT INTO mood_box (fio, mood, state, login) VALUES (%s, %s, %s, %s)", 
                                (fio, mood, state, tab))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False 
                        
    def add_basket(self, product_id, login_customer, value_operation, img, size, color, name):
        try:
            self.cursor.execute("INSERT INTO basket (product_id, login, price, img, size, color, name) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                (product_id, login_customer, value_operation, img, size, color, name))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
                       
    def update_user_password(self, login, new_password):
        try:
            self.cursor.execute("UPDATE users SET pass = %s WHERE login = %s", (new_password, login))
            self.cursor.execute("UPDATE users SET status = %s WHERE login = %s", (1, login))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
     
    def close(self):
        self.cursor.close()
        self.conn.close()
