if not df_chat_wait.empty:
    df_chat_wait = df_chat_wait.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, pd.Timestamp) else x)
else:
    df_chat_wait = pd.DataFrame([['Нет данных']], columns=['Сообщение'])
