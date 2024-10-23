async def add_balans(df_user, sdep, tab, fio, id):
    try:
        clear()
        excel_file = await file_upload("Выберите Excel файл:", accept=".xlsx")
        with BytesIO(excel_file['content']) as buffer:
            df = pd.read_excel(buffer)
        df['operation_type'] = 'Начисление'
        df['status_operation'] = 'Исполнен'
        df['json'] = None
        df[['login_customer', 'value_operation', 'operation_type', 'status_operation', 'json',
            'case1','case2','case3','case4','case5','case6','case7','case8','case9','case10','case11','case12','case13',
            ]].dropna(subset=['value_operation']).to_sql('operations', connect("Convert/db/shop.db"), if_exists='append', index=False)
        popup('Баланс начислен')
        await chek_balance_users(df_user, sdep, tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))


        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = admin_email
        msg['Subject'] = 'Поделился настроением'
        msg.attach(MIMEText(f"ФИО:{fio}<br>Почта:{tab}<br>Настроение:{mood_text}", 'html'))
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.sendmail(sender_email, admin_email, msg.as_string())
        except Exception as e:
            pass
