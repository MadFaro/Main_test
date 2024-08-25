async def add_balans(df_user, sdep, tab, fio, id):
    try:
        clear()
        excel_file = await file_upload("Выберите Excel файл:", accept=".xlsx")
        with BytesIO(excel_file['content']) as buffer:
            df = pd.read_excel(buffer)
        df['operation_type'] = 'Начисление'
        df['status_operation'] = 'Исполнен'
        df['json'] = None
        df.to_sql('operations', connect("Convert/db/shop.db"), if_exists='append', index=False)
        df['id'] = None
        df['login'] = df['login_customer']
        df['state'] = df['operation_type']
        df['on_read'] = 1
        df[['id', 'login', 'state', 'on_read']].to_sql('new_msg', connect("Convert/db/shop.db"), if_exists='append', index=False)
        popup('Баланс начислен')
        await chek_balance_users(df_user, sdep, tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
