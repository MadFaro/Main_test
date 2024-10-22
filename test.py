def get_user_aut(self, ID):
    try:
        # Выполняем запрос и получаем одну строку
        result = self.cursor.execute("SELECT `dt`, `authen_key` FROM `authen` WHERE `login` = ?", (ID,))
        row = result.fetchone()
        
        if row:
            # Возвращаем дату (row[0]) и код (row[1])
            return row[0], row[1]
        
        return None
    except sqlite3.Error:
        return None
