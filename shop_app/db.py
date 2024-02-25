import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, ID):
        try:
            result = self.cursor.execute("SELECT `login` FROM `users` WHERE `login` = ?", (ID,))
            return bool(len(result.fetchall()))
        except:
            return False

    def get_user_pass(self, ID):
        try:
            result = self.cursor.execute("SELECT `pass` FROM `users` WHERE `login` = ?", (ID,))
            return result.fetchone()[0]
        except:
            return None

    def get_user_mot(self, ID):
        try:
            result = self.cursor.execute("SELECT `index`, `fio`, `sdep` FROM `users` WHERE `login` = ?", (ID,))
            return result.fetchone()
        except:
            return None
        
    def get_user_balanse(self, ID):
        try:
            result = self.cursor.execute("SELECT sum(`value_operation`) FROM `operations` WHERE `login_customer` = ?", (ID,))
            return result.fetchone()
        except:
            return None
        
    def get_order_count(self, ID):
        try:
            result = self.cursor.execute("SELECT count(*) FROM `operations` WHERE `status_operation` = ?", (ID,))
            return result.fetchone()
        except:
            return None
        
    def get_user_last_operation(self, ID):
        try:
            result = self.cursor.execute("SELECT max(`datetime_insert`), `operation_type`, `value_operation` FROM `operations` WHERE `login_customer` = ?", (ID,))
            return result.fetchone()
        except:
            return None 
               
    def add_user(self, index, password, sdep, login, fio):
        self.cursor.execute('INSERT INTO `users` (`index`, `pass`, `sdep`, `login`, `fio`) VALUES (?,?,?,?,?)', (index, password, sdep, login, fio))
        self.cursor.execute('INSERT INTO `operations` (`operation_type`, `product_id`, `login_customer`, `value_operation`, `status_operation`) VALUES (?,?,?,?,?)', ('test', 0, login, 0, 'test'))
        return self.conn.commit()
    
    def add_product(self, id, name, description, price, img):
        self.cursor.execute('INSERT INTO `product` (`id`, `name`, `description`, `price`, `img`) VALUES (?,?,?,?,?)', (id, name, description, price, img))
        return self.conn.commit()
    
    def delete_product(self, ID):
        self.cursor.execute("delete FROM `product` WHERE `id` = ?", (ID,))
        return self.conn.commit()
    
    def delete_user(self, ID):
        self.cursor.execute("delete FROM `users` WHERE `index` = ?", (ID,))      
        return self.conn.commit()
    
    def delete_order(self, ID):
        self.cursor.execute("delete FROM `operations` WHERE `id` = ?", (ID,))      
        return self.conn.commit()
    
    def add_operation(self, operation_type, product_id, login_customer, value_operation, status_operation):
        self.cursor.execute('INSERT INTO `operations` (`operation_type`, `product_id`, `login_customer`, `value_operation`, `status_operation`) VALUES (?,?,?,?,?)', (operation_type, product_id, login_customer, value_operation, status_operation))
        return self.conn.commit()
              
    def update_user_password(self, login, new_password):
        self.cursor.execute("UPDATE `users` SET `pass` = ? WHERE `login` = ?", (new_password, login))
        self.conn.commit()
        return self.conn.commit()
    
    def update_order_status(self, login):
        self.cursor.execute("UPDATE `operations` SET `status_operation` = ? WHERE `id` = ?", ('executed', login))
        self.conn.commit()
        return self.conn.commit()   
      
    def close(self):
        self.connection.close()