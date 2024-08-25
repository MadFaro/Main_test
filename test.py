import pandas as pd
from io import BytesIO
import sqlite3

async def add_balans(df_user, sdep, tab, fio, id):
    try:
        clear()

        # Загрузка Excel файла
        excel_file = await file_upload("Выберите Excel файл:", accept=".xlsx")
        with BytesIO(excel_file['content']) as buffer:
            df = pd.read_excel(buffer)

        # Подключение к базе данных
        conn = sqlite3.connect("Convert/db/shop.db")

        # Получение максимального id из new_msg
        query = "SELECT MAX(id) FROM new_msg"
        max_id = pd.read_sql(query, conn).iloc[0, 0]

        # Если таблица new_msg пуста, начинаем с id = 1
        if pd.isnull(max_id):
            max_id = 0

        # Добавление данных в df
        df['operation_type'] = 'Начисление'
        df['status_operation'] = 'Исполнен'
        df['json'] = None
        df['id'] = range(max_id + 1, max_id + 1 + len(df))
        df['login'] = df['login_customer']
        df['state'] = df['operation_type']
        df['on_read'] = 1

        # Сохранение данных в базу данных
        df.to_sql('operations', conn, if_exists='append', index=False)
        df[['id', 'login', 'state', 'on_read']].to_sql('new_msg', conn, if_exists='append', index=False)

        # Закрытие соединения
        conn.close()

        # Уведомление об успешном завершении операции
        popup('Баланс начислен')
        await chek_balance_users(df_user, sdep, tab, fio, id)

    except Exception as e:
        # Логирование ошибки для отладки
        print(f"Error: {e}")
        toast('Error - что-то пошло не по плану :(', duration=0, position='center', color='error', onclick=lambda: run_js('window.location.reload()'))
