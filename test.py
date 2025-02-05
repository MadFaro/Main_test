import sqlite3


class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, ID):
        try:
            result = self.cursor.execute("SELECT 1 FROM `users` WHERE `login` = ?", (ID,))
            return bool(len(result.fetchall()))
        except sqlite3.Error:
            return False
        
    def user_exists_ip(self, ID):
        try:
            result = self.cursor.execute("SELECT `user_login` FROM `session` WHERE `user_ip` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None
        
    def add_user_ip(self, login, ip):
        try:
            self.cursor.execute('INSERT INTO `session` (`user_login`, `user_ip`) VALUES (?,?)', (login, ip))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
                      
    def get_user_pass(self, ID):
        try:
            result = self.cursor.execute("SELECT `pass` FROM `users` WHERE `login` = ?", (ID,))
            return result.fetchone()[0]
        except sqlite3.Error:
            return None
        
    def get_user_aut(self, ID):
        try:
            result = self.cursor.execute("SELECT `authen_key`, `dt`  FROM `authen` WHERE `login` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None
                        
    def get_user_block(self, ID):
        try:
            result = self.cursor.execute("SELECT `status` FROM `users` WHERE `login` = ?", (ID,))
            return result.fetchone()[0]
        except sqlite3.Error:
            return None
        
    def get_user_mot(self, ID):
        try:
            result = self.cursor.execute("SELECT `index`, `fio`, `sdep` FROM `users` WHERE `login` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None
        
    def get_user_balanse(self, ID):
        try:
            result = self.cursor.execute("SELECT sum(`value_operation`) FROM `operations` WHERE `login_customer` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None
        
    def get_basket_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `basket` WHERE `login` = ?", (ID,))
            return result.fetchone()[0]
        except sqlite3.Error:
            return None
                
    def get_order_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `operations` WHERE `status_operation` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None

    def get_question_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `question` WHERE `state` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None
        
    def get_offer_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `offer_box` WHERE `state` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None
        
    def get_mood_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `mood_box` WHERE `state` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None 
        
    def get_advt_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `advt` WHERE `moderation` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None 
                               
    def get_user_last_operation(self, ID):
        try:
            result = self.cursor.execute("SELECT max(`datetime_insert`), `operation_type`, `value_operation` FROM `operations` WHERE `login_customer` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None 
        
    def get_user_gender(self, fio):
        try:
            result = self.cursor.execute("SELECT `gender` FROM `users` WHERE `fio` = ?", (fio,))
            return result.fetchone()
        except sqlite3.Error:
            return None  

    def add_discount(self, name, img):
        try:
            self.cursor.execute('INSERT INTO `discount` (`name`, `img`) VALUES (?,?)', (name, img))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False        

    def add_user(self, password, sdep, login, fio, status, gender, birth_date):
        try:
            self.cursor.execute('INSERT INTO `users` (`pass`, `sdep`, `login`, `fio`, `status`, `gender`, `birth_date`) VALUES (?,?,?,?,?,?,?)', (password, sdep, login, fio, status, gender, birth_date))
            self.cursor.execute('INSERT INTO `operations` (`operation_type`, `json`, `login_customer`, `value_operation`, `status_operation`, `on_read`) VALUES (?,?,?,?,?,?)', ('test', None, login, 0, 'test', 0))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False

    def register_user(self, password, sdep, login, fio, status, gender, birth_date):
        try:
            self.cursor.execute('INSERT INTO `users` (`pass`, `sdep`, `login`, `fio`, `status`, `gender`, `birth_date`) VALUES (?,?,?,?,?,?,?)', (password, sdep, login, fio, status, gender, birth_date))
            self.cursor.execute('INSERT INTO `operations` (`operation_type`, `json`, `login_customer`, `value_operation`, `status_operation`, `on_read`) VALUES (?,?,?,?,?,?)', ('test', None, login, 0, 'test', 0))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
                    
    def add_product(self, id, name, description, price, img, color, size, prom):
        try:
            self.cursor.execute('INSERT INTO `product` (`id`, `name`, `description`, `price`, `img`, `color`, `size`, `prom`) VALUES (?,?,?,?,?,?,?,?)', (id, name, description, price, img, color, size, prom))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False

    def add_aut(self, login, code):
        try:
            self.cursor.execute('INSERT INTO `authen` (`login`, `authen_key`) VALUES (?,?)', (login, code))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def add_log(self, login, type_log):
        try:
            self.cursor.execute('INSERT INTO `log` (`login`, `type_log`) VALUES (?,?)', (login, type_log))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def delete_product(self, ID):
        try:
            self.cursor.execute("delete FROM `product` WHERE `id` = ?", (ID,))
            self.cursor.execute("delete FROM `basket` WHERE `product_id` = ?", (ID,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
    
    def delete_user(self, ID):
        try:
            self.cursor.execute("delete FROM `users` WHERE `index` = ?", (ID,))
            self.conn.commit()
            return True 
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def delete_user_token(self, ID):
        try:
            self.cursor.execute("delete FROM `tokens` WHERE `user_login` = ?", (ID,))
            self.conn.commit()
            return True 
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def delete_aut(self, login):
        try:
            self.cursor.execute("delete FROM `authen` WHERE `login` = ?", (login,))
            self.conn.commit()
            return True 
        except sqlite3.Error:
            self.conn.rollback()
            return False
                
    def delete_session(self, ID):
        try:
            self.cursor.execute("delete FROM `session` WHERE `user_login` = ?", (ID,))
            self.conn.commit()
            return True 
        except sqlite3.Error:
            self.conn.rollback()
            return False
            
    def delete_order(self, ID):
        try:
            self.cursor.execute("delete FROM `operations` WHERE `id` = ?", (ID,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def delete_one_product_basket(self, ID, Login, size, color):
        try:
            self.cursor.execute("delete FROM `basket` WHERE `product_id` = ? and `login` = ? and `size` = ? and `color` = ?", (ID, Login, size, color))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
                
    def delete_all_product_basket(self, Login):
        try:
            self.cursor.execute("delete FROM `basket` WHERE `login` = ?", (Login,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False

    def delete_discount(self, ID):
        try:
            self.cursor.execute("delete FROM `discount` WHERE `id` = ?", (ID,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False 
                
    def add_operation(self, operation_type, json, login_customer, value_operation, status_operation, on_read):
        try:
            self.cursor.execute('INSERT INTO `operations` (`operation_type`, `json`, `login_customer`, `value_operation`, `status_operation`, `on_read`) VALUES (?,?,?,?,?,?)', (operation_type, json, login_customer, value_operation, status_operation, on_read))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False   
               
    def add_box_question(self, tab, fio, msg, state, category):
        try:
            self.cursor.execute('INSERT INTO `question` (`fio`, `msg`, `state`, `category`, `login`) VALUES (?,?,?,?,?)', (fio, msg, state, category, tab))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False    

    def add_box_offer(self, tab, fio, offer, state, fio_bd):
        try:
            self.cursor.execute('INSERT INTO `offer_box` (`fio`, `offer`, `state`, `fio_bd`, `login`) VALUES (?,?,?,?,?)', (fio, offer, state, fio_bd, tab))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False  

    def add_advt(self, fio, login, phone, category, city, name, text_ad, file_ad, moderation):
        try:
            self.cursor.execute('INSERT INTO `advt` (`fio`, `login`, `phone`, `category`, `city`, `name`, `text_ad`, `file_ad`, `moderation`) VALUES (?,?,?,?,?,?,?,?,?)', (fio, login, phone, category, city, name, text_ad, file_ad, moderation))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False  

    def update_advt(self, id):
        try:
            self.cursor.execute("UPDATE `advt` SET `date_ad` = datetime() WHERE `id` = ?", (id,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def update_advt_admin(self, id):
        try:
            self.cursor.execute("UPDATE `advt` SET `moderation` = 1 WHERE `id` = ?", (id,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
                
    def delete_advt(self, id):
        try:
            self.cursor.execute("delete from `advt` WHERE `id` = ?", (id,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False   
                     
    def add_box_mood(self, tab, fio, mood, state):
        try:
            self.cursor.execute('INSERT INTO `mood_box` (`fio`, `mood`, `state`, `login`) VALUES (?,?,?,?)', (fio, mood, state, tab))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False 
                        
    def add_basket(self, product_id, login_customer, value_operation, img, size, color, name):
        try:
            self.cursor.execute('INSERT INTO `basket` (`product_id`, `login`, `price`, `img`, `size`, `color`, `name`) VALUES (?,?,?,?,?,?,?)', (product_id, login_customer, value_operation, img, size, color, name))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
                      
    def update_user_password(self, login, new_password):
        try:
            self.cursor.execute("UPDATE `users` SET `pass` = ? WHERE `login` = ?", (new_password, login))
            self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `login` = ?", (1, login))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def block_user(self, login, status):
        try:
            self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `login` = ?", (status, login))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
   
    def update_order_status(self, status, state, id):
        try:
            self.cursor.execute("UPDATE `operations` SET `status_operation` = ?, `on_read` = ? WHERE `id` = ?", (status, state, id))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False  
         
    def update_order_cancel(self, status, price, cancel, on_read, id):
        try:
            self.cursor.execute("UPDATE `operations` SET `status_operation` = ?, `value_operation` = ?, `cancel` = ? , `on_read` = ? WHERE `id` = ?", (status, price, cancel, on_read, id))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False   
                 
    def update_question_status(self, status, answer, id):
        try:
            self.cursor.execute("UPDATE `question` SET `state` = ?, `answer` = ?  WHERE `id` = ?", (status, answer, id))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False  
        
    def update_offer_box_status(self, status, answer, id):
        try:
            self.cursor.execute("UPDATE `offer_box` SET `state` = ?, `answer` = ?  WHERE `id` = ?", (status, answer, id))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False 
         
    def update_mood_box_status(self, status, answer, id):
        try:
            self.cursor.execute("UPDATE `mood_box` SET `state` = ?, `answer` = ?  WHERE `id` = ?", (status, answer, id))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False  

    def update_product_bd(self, name, price, desc, size, color, prom, id):
        try:
            self.cursor.execute("UPDATE `product` SET `name` = ?, `price` = ?, `description` = ?, `size` = ?, `color` = ?, `prom` = ?  WHERE `id` = ?", (name, price, desc, size, color, prom, id))
            self.cursor.execute("delete FROM `basket` WHERE `product_id` = ?", (id,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False  
                                                                  
    def get_def_pass(self):
        try:
            result = self.cursor.execute("SELECT `pass` FROM `reset`")
            return result.fetchone()[0]
        except sqlite3.Error:
            return None
        
    def get_def_crypta(self):
        try:
            result = self.cursor.execute("SELECT `key` FROM `crypt_key`")
            return result.fetchone()[0]
        except sqlite3.Error:
            return None
        
    def update_order_msg(self, state, tab):
        try:
            self.cursor.execute("UPDATE `operations` SET `on_read` = ? WHERE `login_customer` = ?", (state, tab))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False   
                 
    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error:
            pass
