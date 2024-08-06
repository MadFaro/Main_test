put_row([
        None,
        put_button(f"Заказы {count}", onclick=lambda: chek_order('admin', tab, fio, id, img_logo), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'), 
        put_button(f"Вопросы {count1}", onclick=lambda: chek_question('admin', tab, fio, id, img_logo), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'),
        put_button(f"Предложения {count2}", onclick=lambda: chek_offer_box('admin', tab, fio, id, img_logo), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'), 
        put_button(f"Настроение {count3}", onclick=lambda: chek_mood_box('admin', tab, fio, id, img_logo), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'), 
        put_button("Магазин", onclick=lambda: noadmin(sdep, tab, fio, id), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'),
        put_button("Добавить товар", onclick=lambda: add_product(df_product, sdep, tab, fio, id), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'),
        put_button("Добавить пользователя", onclick=lambda: add_user(df_user, sdep, tab, fio, id), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'),
        put_button("Баланс", onclick=lambda: chek_balance_users(df_user, 'admin', tab, fio, id), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;'),
        ]).style("display:grid;grid-template-columns:1fr")
