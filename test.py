    def get_user_aut(self, ID):
        try:
            result = self.cursor.execute("SELECT `dt`, `authen_key` FROM `authen` WHERE `login` = ?", (ID,))
            return result.fetchone()[0]
        except sqlite3.Error:
            return None
