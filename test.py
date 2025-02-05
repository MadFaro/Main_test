    def update_user_password(self, login, new_password):
        try:
            self.cursor.execute("UPDATE users SET pass = %s WHERE login = %s", (new_password, login))
            self.cursor.execute("UPDATE users SET status = %s WHERE login = %s", (1, login))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        
    def block_user(self, login, status):
        try:
            self.cursor.execute("UPDATE users SET status = %s WHERE login = %s", (status, login))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
   
    def update_order_status(self, status, state, id):
        try:
            self.cursor.execute("UPDATE operations SET status_operation = %s, on_read = %s WHERE id = %s", (status, state, id))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False  
         
    def update_order_cancel(self, status, price, cancel, on_read, id):
        try:
            self.cursor.execute("UPDATE operations SET status_operation = %s, value_operation = %s, cancel = %s, on_read = %s WHERE id = %s", 
                                (status, price, cancel, on_read, id))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False   
                 
    def update_question_status(self, status, answer, id):
        try:
            self.cursor.execute("UPDATE question SET state = %s, answer = %s WHERE id = %s", (status, answer, id))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False  
        
    def update_offer_box_status(self, status, answer, id):
        try:
            self.cursor.execute("UPDATE offer_box SET state = %s, answer = %s WHERE id = %s", (status, answer, id))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False 
         
    def update_mood_box_status(self, status, answer, id):
        try:
            self.cursor.execute("UPDATE mood_box SET state = %s, answer = %s WHERE id = %s", (status, answer, id))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False  

    def update_product_bd(self, name, price, desc, size, color, prom, id):
        try:
            self.cursor.execute("UPDATE product SET name = %s, price = %s, description = %s, size = %s, color = %s, prom = %s WHERE id = %s", 
                                (name, price, desc, size, color, prom, id))
            self.cursor.execute("DELETE FROM basket WHERE product_id = %s", (id,))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False  
                                                                  
    def get_def_pass(self):
        try:
            self.cursor.execute("SELECT pass FROM reset")
            return self.cursor.fetchone()[0]
        except psycopg2.Error:
            return None
        
    def get_def_crypta(self):
        try:
            self.cursor.execute("SELECT key FROM crypt_key")
            return self.cursor.fetchone()[0]
        except psycopg2.Error:
            return None
        
    def update_order_msg(self, state, tab):
        try:
            self.cursor.execute("UPDATE operations SET on_read = %s WHERE login_customer = %s", (state, tab))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False   
                 
    def close(self):
        try:
            self.conn.close()
        except psycopg2.Error:
            pass
