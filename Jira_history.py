    buffer = BytesIO()
    df = pd.read_sql("SELECT login as login_customer, '' as value_operation FROM users where login <> 'admin'", connect("Convert/db/shop.db"))
    df.to_excel(buffer, index=False)
put_button(' Template ', lambda: download('example.xlsx', buffer.getvalue()), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'),
from io import BytesIO
# Функция для добавления баланса
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
        popup('Баланс начислен')
        await chek_balance_users(df_user, sdep, tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
