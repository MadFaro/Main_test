# Основная функция
async def noadmin(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    BotDS.add_log(login=tab, type_log = 'Открыл магазин')
    df_product = pd.read_sql(sql.sql_product, connect("Convert/db/shop.db"))
    img_ban = open('img/ban.jpg', 'rb').read()
    img_logo = open('img/logo.png', 'rb').read()
    product_cards = [await render_product_card(product, sdep, tab, fio) for _, product in df_product.iterrows()]
    balans = BotDS.get_user_balanse(tab)[0]

    rows = []
    for i in range(0, len(product_cards), 5):
        row_items = product_cards[i:i+5]
        rows.append(row_items)
    rows_grid = put_grid(rows, cell_width='auto', cell_height='auto').style('justify-content:center;gap:1vh;grid-template-columns: repeat(auto-fill, minmax(200px, calc(100% / 6)));')
    if sdep == 'admin':
        put_button("  Admin Panel   ", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position:absolute;left:0%;top:0.5%;z-index:2147483647')
    else:
        put_row([
            None,
            put_text(f'Добро пожаловать, {fio}').style('margin-top: 0.8em;filter: drop-shadow(0px 0px 1px #181d1f)'),
            None
        ]).style('background:black;grid-template-columns:0.009fr 1fr;color: white;font-size: max(0.5vw, 10px);')
        put_row([
        put_button("\U0001F4DD\r\nПравила", onclick=lambda: des_render(), color='dark', outline=True),
        put_button("\U0001F4DE\r\nКонтакты", onclick=lambda: contact_render(), color='dark', outline=True),
        put_button("\U0001F4C9\r\nИстория", onclick=lambda: my_order(sdep, tab, fio, id, img_logo), color='dark', outline=True),
        put_image(img_logo, width='auto', height='auto').style('place-self: center;'),
        put_button(f"{balans}\rБаланс", onclick=lambda: my_balance(tab, fio), color='dark', outline=True),
        put_button("\U0001F6D2\r\nКорзина", onclick=lambda: basket_render(tab), color='dark', outline=True),
        put_button("\U0001F51A\r\nГлавная", onclick=lambda: main_menu(sdep, tab, fio, id), color='dark', outline=True)
        ]).style('padding:0.4em;background:rgb(255 255 255);grid-template-columns:0.01fr 0.01fr 0.01fr 1fr 0.01fr 0.01fr 0.01fr;')
        put_image(img_ban, width='auto', height='auto').style('width:100%;filter: drop-shadow(1px 2px 4px #181d1f)')
    put_row([
    put_column([
        put_tabs([
        {'title':'МАГАЗИН ТВОИХ ДОСТИЖЕНИЙ', 'content':
        [put_column(rows_grid)]}
       ]).style("width:100%;height:100%;transform:translateY(-5px);border-color:white;justify-content:center;"),
       None,
       put_html(f"""
        <footer class="footer">
        Version <a href="" target="_blank">{ver_app}</a>
        </footer>
       """).style("width:100%;z-index:2147483647")
       ], size='auto')]
            ,size='auto').style('position:absolute;width:100%;height:100%')
# Функция для создания карточки товара
async def render_product_card(product, sdep, tab, fio):
    img_content = open(product['img'], 'rb').read()
    if product['prom'] == 1:
        return put_tabs([{'title': f"{str(product['name'])} - {product['price']} \U0001F525", 'content':[
            put_column([
            put_image(img_content, width='100%', height="100%")
            ]).style('grid-template-rows:1fr'),
            put_button("", onclick=lambda: order(str(product['id']), str(product['name']),product['img'], product['price'], product['description'], product['color'], product['size'], sdep, tab, fio), 
                       color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
        ]}]).style('grid-column: span 1; grid-row: span 1;display: block;border-bottom: 5px solid #ff0000;')
    else:
        return put_tabs([{'title': f"{str(product['name'])} - {product['price']} \U0001F6D2", 'content':[
            put_column([
            put_image(img_content, width='100%', height="100%")
            ]).style('grid-template-rows:1fr'),
            put_button("", onclick=lambda: order(str(product['id']), str(product['name']),product['img'], product['price'], product['description'], product['color'], product['size'], sdep, tab, fio), 
                       color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
        ]}]).style('grid-column: span 1; grid-row: span 1;display: block;')

# Функция для обработки заказа (Показывает карточку с описанием и добавлением в корзину)
async def order(id, name, img, price, description, color, size, sdep, tab, fio):
    data = {
        "stars": [
            {"id": "5-stars", "value": "5"},
            {"id": "4-stars", "value": "4"},
            {"id": "3-stars", "value": "3"},
            {"id": "2-stars", "value": "2"},
            {"id": "1-star", "value": "1"}
        ]
    }
    
    if sdep == 'admin':
        img_content = open(img, 'rb').read()
        color_list = json.loads(color.replace("'", '"'))
        size_list = json.loads(size.replace("'", '"'))
        if all(not lst for lst in [color_list, size_list]):
            return popup(f"{name} - {price} баллов",
                        [   put_row([
                            None,
                            put_image(img_content),
                            None
                            ]).style('grid-template-columns: 0.25fr 1fr 0.1fr;'),
                            put_text(f"Описание:\n{description}")
                        ])   
        else:
            return popup(f"{name} - {price} баллов.",
                        [   
                            put_row([
                            put_image(img_content),
                            put_column([
                                None if not size_list else put_select(name='size', label='Выберите размер:', options=size_list),
                                None if not color_list else put_select(name='color', label='Выберите цвет:', options=color_list),
                            None,
                            ]).style("" if not size_list or not color_list else "grid-template-rows: 0.5fr 1fr 1fr;")
                            ]).style('grid-template-columns: 1fr 0.4fr;'),
                            put_text(f"Описание:\n{description}")
                        ], size='normal')
    else:
        img_content = open(img, 'rb').read()
        color_list = json.loads(color.replace("'", '"'))
        size_list = json.loads(size.replace("'", '"'))
        if all(not lst for lst in [color_list, size_list]):
            return popup(f"{name} - {price} баллов",
                        [   put_row([
                            None,
                            put_image(img_content),
                            None
                            ]).style('grid-template-columns: 0.25fr 1fr 0.1fr;'),
                            put_text(f"Описание:\n{description}"),
                            put_button("В корзину", onclick=lambda: basket_add(id, img, tab, price, sdep, fio, name), color='info', outline=True)
                        ])      
        else:      
            return popup(f"{name} - {price} баллов",
                        [   
                            put_row([
                            put_image(img_content),
                            put_column([
                                None if not size_list else put_select(name='size', label='Выберите размер:', options=size_list),
                                None if not color_list else put_select(name='color', label='Выберите цвет:', options=color_list),
                            None,
                            ]).style("" if not size_list or not color_list else "grid-template-rows: 0.5fr 1fr 1fr;")
                            ]).style('grid-template-columns: 1fr 0.4fr;'),
                            put_text(f"Описание:\n{description}"),
                            put_widget(css.tpl, data),
                            put_button("В корзину", onclick=lambda: basket_add(id, img, tab, price, sdep, fio, name), color='info', outline=True)
                        ], size='normal')
