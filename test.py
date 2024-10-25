    def token_exists(self, ID):
        try:
            result = self.cursor.execute("SELECT 1 FROM `tokens` WHERE `user_token` = ?", (ID,))
            return bool(len(result.fetchall()))
        except sqlite3.Error:
            return False
