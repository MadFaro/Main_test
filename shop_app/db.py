﻿import sqlite3


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

    def get_user_pass(self, ID):
        try:
            result = self.cursor.execute("SELECT `pass` FROM `users` WHERE `login` = ?", (ID,))
            return result.fetchone()[0]
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
        
    def get_user_last_operation(self, ID):
        try:
            result = self.cursor.execute("SELECT max(`datetime_insert`), `operation_type`, `value_operation` FROM `operations` WHERE `login_customer` = ?", (ID,))
            return result.fetchone()
        except sqlite3.Error:
            return None 
               
    def add_user(self, index, password, sdep, login, fio):
        try:
            self.cursor.execute('INSERT INTO `users` (`index`, `pass`, `sdep`, `login`, `fio`) VALUES (?,?,?,?,?)', (index, password, sdep, login, fio))
            self.cursor.execute('INSERT INTO `operations` (`operation_type`, `json`, `login_customer`, `value_operation`, `status_operation`) VALUES (?,?,?,?,?)', ('test', None, login, 0, 'test'))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
    
    def add_product(self, id, name, description, price, img):
        try:
            self.cursor.execute('INSERT INTO `product` (`id`, `name`, `description`, `price`, `img`) VALUES (?,?,?,?,?)', (id, name, description, price, img))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
    
    def delete_product(self, ID):
        try:
            self.cursor.execute("delete FROM `product` WHERE `id` = ?", (ID,))
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
    
    def delete_order(self, ID):
        try:
            self.cursor.execute("delete FROM `operations` WHERE `id` = ?", (ID,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False
        
    def delete_one_product_basket(self, ID, Login):
        try:
            self.cursor.execute("delete FROM `basket` WHERE `product_id` = ? and `login` = ?", (ID, Login))
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
             
    def add_operation(self, operation_type, json, login_customer, value_operation, status_operation):
        try:
            self.cursor.execute('INSERT INTO `operations` (`operation_type`, `json`, `login_customer`, `value_operation`, `status_operation`) VALUES (?,?,?,?,?)', (operation_type, json, login_customer, value_operation, status_operation))
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            return False          

    def add_basket(self, product_id, login_customer, value_operation, img, size, color):
        try:
            self.cursor.execute('INSERT INTO `basket` (`product_id`, `login`, `price`, `img`, `size`, `color`) VALUES (?,?,?,?,?,?)', (product_id, login_customer, value_operation, img, size, color))
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
   
    def update_order_status(self, status, id):
        try:
            self.cursor.execute("UPDATE `operations` SET `status_operation` = ? WHERE `id` = ?", (status, id))
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
          
    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error:
            pass