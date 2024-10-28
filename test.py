                token_result = BotDS.user_token_for_mail(login_customer)
                
                # Добавляем токен к URL, если он есть
                if token_result:
                    token = token_result[0]
                    personalized_url = f"{shop_url}?app={token}"
                else:
                    personalized_url = shop_url
    def user_token_for_mail(self, ID):
        try:
            result = self.cursor.execute("SELECT `user_token` FROM `tokens` WHERE `user_login` = ?", (ID,))
            return result.fetchall()
        except sqlite3.Error:
            return None
