# Главное меню
async def main_menu(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    img_ban = open('main_menu/img/ban.jpg', 'rb').read()
    img_logo = open('img/logo.png', 'rb').read()
    df = pd.read_sql(sql.sql_msg.replace('Замена', str(tab)), connect("Convert/db/shop.db"))

    product_cards = []
    product_cards.append(
        put_tabs([{'title': f"ТВОЙ МАГАЗИН МЕРЧА", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo1.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr'),
                    put_button("", onclick=lambda: noadmin(sdep, tab, fio, id), 
                            color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;border-bottom: 1px solid #e9ecef;')
    )
    product_cards.append(
        put_tabs([{'title': f"ГЕЙМИФИКАЦИЯ", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo2.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr'),
                    put_button("", onclick=lambda: game_noadmin(sdep, tab, fio, id), 
                            color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;border-bottom: 1px solid #e9ecef;')
    )
    product_cards.append(
        put_tabs([{'title': f"БОКС ОБРАТНОЙ СВЯЗИ", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo3.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr'),
                    put_button("", onclick=lambda: box_menu(sdep, tab, fio, id), 
                            color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;border-bottom: 1px solid #e9ecef;')
    )

    product_cards.append(
        put_tabs([{'title': f"СКИДКИ ДЛЯ ТЕБЯ", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo4.jpg', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr'),
                    put_button("", onclick=lambda: toast("Что то будет"), 
                            color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;border-bottom: 1px solid #e9ecef;')
    )

    rows = []
    for i in range(0, len(product_cards), 4):
        row_items = product_cards[i:i+4]
        rows.append(row_items)
    rows_grid = put_grid(rows, cell_width='auto', cell_height='auto').style('justify-content:center;gap:5vh;grid-template-columns: repeat(auto-fill, minmax(200px, calc(100% / 5)));')
    put_row([
    None if df.empty else put_widget(css.tpl.replace("Замена", str(df.shape[0])), data={"contents": put_button("", onclick=lambda: new_msg_cnt(sdep, tab, fio, id, img_logo, df), color='warning', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')}).style("margin: auto;"),
    put_image(img_logo, width='auto', height='auto').style('place-self: center;'),
    put_button("🡸\nВыйти", onclick=lambda: exit_shop(tab), color='dark', outline=True)
        ]).style('padding:0.3em;background:rgb(255 255 255);grid-template-columns:0.01fr 1fr 0.01fr;')
    put_image(img_ban, width='auto', height='auto').style('width:100%;display: block;margin-left: auto;margin-right: auto;')
    put_row([
    put_column([
        put_column(rows_grid).style("width:100%;height:50%;transform:translateY(-5px);border-color:white;justify-content:center;display:grid;margin-top: 1.25rem;")], size='auto')]
            ,).style('width:100%;height:50%;')
    
    put_html(f"""
        <footer class="footer">
        {fio}
        </footer>
       """).style("position:absolute;width:100%;bottom:0px")
