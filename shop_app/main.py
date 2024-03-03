from sqlite3 import connect
from pywebio import start_server, config
from pywebio.output import *
from pywebio.pin import *
from pywebio.input import *
from pywebio.session import run_js
from html_css import css
from db import BotDB
from function import sql
import pandas as pd
import re
import hashlib
import json


# Конект к БД
BotDS = BotDB('Convert/db/shop.db')

# Авторизация
@config(theme = 'minty', css_style = css.container_output, description='shop', title='shop')
async def main():

    invalid_password_attempts = 0

    def validate_login(tab):
        if BotDS.user_exists(ID=tab) == False:
            return 'Логин не существует'
        
    def validate_password(password):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[a-zA-Z0-9!@#$%^&*()_+]{8,}$", password):
            return 'Пароль должен содержать не менее 8 символов и включать как минимум одну заглавную, одну строчную букву и один специальный символ'
    
    try:
        while invalid_password_attempts < 5:
            id_select = await input_group("Вход",
                                        [
                            input('Логин', name='tab', type=TEXT, validate=validate_login),
                            input('Пароль', name='password', type=PASSWORD)
                                        ])
            tab = id_select['tab']
            block = BotDS.get_user_block(tab)
            if int(block) == 0:
                toast('Учетная запись заблокирована', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
            else:
                password = str(hashlib.sha256(str(id_select['password']).encode()).hexdigest())
                rezult = BotDS.user_exists(ID=tab)
                def_pass = str(BotDS.get_def_pass())

                if rezult == False:
                    toast('Неверный логин', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

                elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == def_pass and password == def_pass:
                    id_select_2 = await input_group("Введи новый пароль",
                                                    [
                                    input('Пароль', name='password', type=PASSWORD, validate=validate_password)
                                                    ])
                    password_up = hashlib.sha256(str(id_select_2['password']).encode()).hexdigest()
                    BotDS.update_user_password(tab, password_up)
                    toast('Пароль обновлен', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                    run_js('window.location.reload()')

                elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == password:

                    user_info = BotDS.get_user_mot(ID=tab)

                    if user_info[2] == 'noadmin':
                        await noadmin(sdep='noadmin', tab=tab, fio=user_info[1], id = user_info[0])

                    elif user_info[2] == 'admin':
                        await admin(sdep='admin', tab=tab, fio=user_info[1], id = user_info[0])

                    else:
                        toast('Нет прав', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

                    break

                else:
                    invalid_password_attempts += 1
                    if invalid_password_attempts >= 5:
                        BotDS.block_user(tab, 0)
                        toast('Учетная запись заблокирована', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
                    else:
                        toast('Неверный пароль', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

    except:
        clear()
        toast('Нет прав', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

# Основная функция для отображения пользователям (без админ прав)
async def noadmin(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass

    df_product = pd.read_sql(sql.sql_product, connect("Convert/db/shop.db"))
    img_ban = open('img/ban.jpg', 'rb').read()
    img_logo = open('img/logo.png', 'rb').read()
    product_cards = [await render_product_card(product, sdep, tab, fio) for _, product in df_product.iterrows()]

    rows = []
    for i in range(0, len(product_cards), 5):
        row_items = product_cards[i:i+5]
        rows.append(row_items)

    rows_grid = put_grid(rows).style('justify-content:center;gap:15px;')
    if sdep == 'admin':
        put_button("    Admin panel", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position:fixed;left:0%;top:37%;z-index:2147483647')
    else:
        put_row([
            None,
            put_text('\U0001F69B Доставим в офис по всей стране').style('margin-top: 0.5em;'),
            None,
            put_button(" Проект ", onclick=lambda: toast('что-то будет'), color='light', link_style=True),
            put_button("Контакты", onclick=lambda: toast('что-то будет'), color='light', link_style=True)
        ]).style('background:black;grid-template-columns:0.01fr 0.5fr 1fr 0.05fr 0.1fr;color: white;font-size: smaller;')
        put_row([
        put_button("\U0001F3E0 Главная", onclick=lambda: noadmin(sdep, tab, fio, id), color='dark', outline=True),
        None,
        put_image(img_logo),
        put_button("\U0001F4B3 Кошелек", onclick=lambda: my_balance(tab, fio), color='dark', outline=True),
        put_button("\U0001F6D2 Корзина", onclick=lambda: basket_render(tab), color='dark', outline=True),
        put_button("\U0001F4CA Заказы ", onclick=lambda: my_order(sdep, tab, fio, id), color='dark', outline=True)]).style('padding:0.4em;background:rgb(255 255 255);grid-template-columns:0.1fr 1fr 1fr 0.1fr 0.1fr;')
        put_image(img_ban, width='auto', height='auto').style('width:100%')
    put_row([
    put_column([
        put_tabs([
        {'title':'Одежда', 'content':
        [put_column(rows_grid)]},
        {'title': 'Техника', 'content': 
        [put_column(rows_grid)]},
        {'title': 'Что-то еще', 'content': 
        [put_column(rows_grid)]}
       ]).style("width:100%;height:100%;transform:translateY(-5px);border-color:white;justify-content:center;")], size='auto')]
            ,size='auto').style('position:absolute;width:100%;height:100%')

# Функция для создания карточки товара
async def render_product_card(product, sdep, tab, fio):
    img_content = open(product['img'], 'rb').read()
    return put_tabs([{'title': f"{str(product['name'])}", 'content':[
        put_column([
        put_image(img_content, width='100%', height="100%"),
        put_text(f"{product['price']} руб").style('height:100%;width:100%;text-align: center;')
        ]).style('grid-template-rows:1fr 0.1fr'),
        put_button("", onclick=lambda: order(str(product['id']), str(product['name']),product['img'], product['price'], product['description'], sdep, tab, fio), 
                   color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
    ]}]).style('grid-column: span 1; grid-row: span 1;display: block;')

# Функция для обработки заказа (Показывает карточку с описанием и добавлением в корзину)
async def order(id, name, img, price, description, sdep, tab, fio):
    if sdep == 'admin':
        img_content = open(img, 'rb').read()
        size_options = ['S', 'M', 'L', 'XL', 'XXL']
        color_options = ['Черный', 'Белый', 'Красный']
        return popup(f"{name} - {price} руб.",
                    [
                        put_row([
                        put_image(img_content),
                        put_column([
                        put_select(name='size', label='Выберите размер:', options=size_options),
                        put_select(name='color', label='Выберите цвет:', options=color_options),
                        None,
                        ]).style("grid-template-rows: 0.5fr 1fr 1fr;")
                        ]).style('grid-template-columns: 1fr 0.4fr;'),
                        put_text(f"Описание:\n{description}"),
                    ], size='normal')
    else:
        img_content = open(img, 'rb').read()
        size_options = ['S', 'M', 'L', 'XL', 'XXL']
        color_options = ['Черный', 'Белый', 'Красный']
        return popup(f"{name} - {price} руб.",
                    [   
                        put_row([
                        put_image(img_content),
                        put_column([
                        put_select(name='size', label='Выберите размер:', options=size_options),
                        put_select(name='color', label='Выберите цвет:', options=color_options),
                        None,
                        ]).style("grid-template-rows: 0.5fr 1fr 1fr;")
                        ]).style('grid-template-columns: 1fr 0.4fr;'),
                        put_text(f"Описание:\n{description}"),
                        put_button("В корзину", onclick=lambda: basket_add(id, img, tab, price, sdep, fio), color='danger', outline=True)
                    ], size='normal')

# Функция формирования корзины
async def basket_render(tab):
    try:
        close_popup()
    except:
        pass
    df = pd.read_sql(sql.sql_basket.replace('Замена', tab), connect("Convert/db/shop.db"))
    if df.empty:
        toast('В корзине нет товаров')
    else:
        items = [] 
        total_price = 0
        basket_data = [] 
        
        for (product_id, size, color), group_df in df.groupby(['product_id', 'size', 'color']):
            count = len(group_df) 
            img_url = open(group_df.iloc[0]['img'], 'rb').read()
            subtotal_price = group_df['price'].sum()
            total_price += subtotal_price
            
            item_data = {
                'product_id': str(product_id),
                'count': str(count),
                'subtotal_price': str(subtotal_price),
                'img': str(group_df.iloc[0]['img']),
                'size': str(size),
                'color': str(color)
            }
            basket_data.append(item_data)
        
            item_image = put_image(img_url, width='75px', height='75px')
            item_text = put_text(f'{count}').style('text-align: center;width: 50px; height: 20px;')
            item_size = put_text(f'{size}').style('text-align: center;width: 50px; height: 20px;')
            item_color = put_text(f'{color}').style('text-align: center;width: 100px; height: 20px;')
            item_price = put_text(f'{subtotal_price}').style('text-align: center;width: 100px; height: 20px;')
            item_button = put_button("x", onclick=lambda: basket_delete_one(tab, product_id, group_df.iloc[0]['login']), color='danger', outline=True)

            items.append(put_row([None, item_text, None, item_image, None, item_size, None, item_color, None, item_price, None, item_button, None], size='1% 10% 1% 35% 1% 10% 1% 10% 1% 10% 1% 10% 1%').style('display: flex;justify-content: space-between;align-items: center;'))
        
        json_data = json.dumps(basket_data)
        
        total_text = put_column([None,None,None,None,None,None,None,None,None,None,None,None,
        put_text(f'К оплате: {total_price}')])
        items.append(total_text)
        buttons_column = put_row([put_button("Оплатить", onclick=lambda: basket_accept(json_data, tab, int(total_price)), color='danger', outline=True),None,
                                    put_button("Очистить", onclick=lambda: basket_delete_all(tab, product_id, group_df.iloc[0]['login']), color='danger', outline=True)], size='25% 2% 25%')
        items.append(buttons_column)
        
        popup('Корзина', items)

        
# функция удаления одного товара из корзины
async def basket_delete_one(tab, product_id, login):
    BotDS.delete_one_product_basket(int(product_id), login)
    await basket_render(tab)

# функция удаления всех товаров из корзины
async def basket_delete_all(tab, product_id, login):
    BotDS.delete_all_product_basket(login)
    await basket_render(tab)

# Функция добавлнения в корзину
async def basket_add(id, img, tab, price, sdep, fio):
    count = BotDS.get_basket_count(tab)
    if int(count) < 5:
        selectid_size = await pin['size']
        selectid_color = await pin['color']
        BotDS.add_basket(product_id=id, login_customer=tab, value_operation=price, img=img, size=selectid_size, color=selectid_color)
        toast('Товар добавлен в корзину')
    else:
        toast('Максимум товаров в корзине 5')

# функция принятия заказа
async def basket_accept(json_data, tab, total_price):
    balans = BotDS.get_user_balanse(tab)[0]
    if balans < total_price:
        toast('Недостаточно средств')
    else:
        BotDS.add_operation(operation_type='Покупка', json=json_data, login_customer=tab, value_operation=-total_price, status_operation='Принят')
        BotDS.delete_all_product_basket(tab)
        close_popup()
        toast('Заказ принят')

# Функция для проверки баланса
async def my_balance(tab, fio):
    img = open('img/1.png', 'rb').read()
    last_operation = BotDS.get_user_last_operation(tab)
    balans = BotDS.get_user_balanse(tab)[0]
    if balans < 0:
        balans = 0
    else:
        balans
    popup("Кошелек", [
        put_image(img),
        put_text(f"{fio}").style('display: flex;justify-content: center;'),
        put_text(f"Доступно к списанию : {balans}"),
        put_text(f"Дата последней операции : {last_operation[0]}"),
        put_text(f"Тип последней операции : {last_operation[1].replace('addition', 'Начисление').replace('subtract', 'Покупка')}"),
        put_text(f"Сумма операции : {last_operation[2]}")
    ])

# Функция для отображения заказов
async def my_order(sdep, tab, fio, id):
    # Очищаем 
    try:
        clear()
    except:
        pass
    df_operation = pd.read_sql(sql.sql_operations.replace('Замена', str(tab)), connect("Convert/db/shop.db"))
    df_operation_site = df_operation[['id',
                         'datetime_insert',
                         'operation_type',
                         'login_customer',
                         'value_operation',
                         'status_operation']]
    
    async def user_chek_order(row_id):
        product_id = df_operation.to_dict(orient='records')[row_id]['id']
        product_type = df_operation.to_dict(orient='records')[row_id]['operation_type']
        if product_type == 'Начисление':
            pass
        else:
            await order_open(sdep, tab, product_id, fio, id)
        
    if df_operation.empty:
        toast("У тебя нет операций")
    else:
        put_row([
        None,
        put_button("\U0001F3E0 Главная", onclick=lambda: noadmin(sdep, tab, fio, id), color='dark', outline=True).style('font-size: 2vh')]).style('padding:0.4em;background:rgb(255 255 255);grid-template-columns:1fr 0.1fr;')
                
        put_row([
            None,
            None,
        put_column([
            None,
            put_datatable(df_operation_site.to_dict('records'), theme='alpine-dark', onselect=user_chek_order)])]).style('width:99%;height:100%;')         

# Функциф просмотра заказа
async def order_open(sdep, tab, product_id, fio, id):
    try:
        close_popup()
    except:
        pass
    
    df = pd.read_sql(sql.sql_operations_one.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))
    # Загружаем данные о корзине из JSON
    json_data = json.loads(df['json'].iloc[0]) 
    
    items = [] 
    total_price = 0
        
    for item_data in json_data:
        count = int(item_data['count'])  # Преобразуем строковое значение в целое число
        img_url = open(item_data['img'], 'rb').read()
        subtotal_price = int(item_data['subtotal_price'])  # Преобразуем строковое значение в целое число
        total_price += subtotal_price
            
        item_image = put_image(img_url, width='75px', height='75px')
        item_text = put_text(f'{count}').style('text-align: center;50px; height: 20px;')
        item_size = put_text(f'{item_data["size"]}').style('text-align: center;50px; height: 20px;')
        item_color = put_text(f'{item_data["color"]}').style('text-align: center;100px; height: 20px;')
        item_price = put_text(f'{subtotal_price}').style('text-align: center;100px; height: 20px;')

        items.append(put_row([None, item_text, None, item_image, None, item_size, None, item_color, None, item_price, None], size='5% 10% 2% 35% 2% 10% 2% 10% 2% 10% 5%').style('display: flex;justify-content: space-between;align-items: center;'))
        
    total_text = put_column([None,None,None,None,None,None,None,None,None,None,None,None,
    put_text(f'Оплачено: {total_price}')])
    items.append(total_text)
        
    buttons_column = put_row([put_button("Отменить", onclick=lambda: delete_order(sdep, tab, product_id, fio, id), color='danger', outline=True)])
    items.append(buttons_column)
        
    popup(f'Заказ {product_id}', items)

# Функциф просмотра заказа
async def order_open_admin(sdep, tab, product_id, fio, id):
    try:
        close_popup()
    except:
        pass
    
    df = pd.read_sql(sql.sql_operations_one.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))
    # Загружаем данные о корзине из JSON
    json_data = json.loads(df['json'].iloc[0]) 
    
    items = [] 
    total_price = 0
        
    for item_data in json_data:
        count = int(item_data['count'])  # Преобразуем строковое значение в целое число
        img_url = open(item_data['img'], 'rb').read()
        subtotal_price = int(item_data['subtotal_price'])  # Преобразуем строковое значение в целое число
        total_price += subtotal_price
            
        item_image = put_image(img_url, width='75px', height='75px')
        item_text = put_text(f'{count}').style('text-align: center;50px; height: 20px;')
        item_size = put_text(f'{item_data["size"]}').style('text-align: center;50px; height: 20px;')
        item_color = put_text(f'{item_data["color"]}').style('text-align: center;100px; height: 20px;')
        item_price = put_text(f'{subtotal_price}').style('text-align: center;100px; height: 20px;')


        items.append(put_row([None, item_text, None, item_image, None, item_size, None, item_color, None, item_price, None], size='5% 10% 2% 35% 2% 10% 2% 10% 2% 10% 5%').style('display: flex;justify-content: space-between;align-items: center;'))
        
    total_text = put_column([None,None,None,None,None,None,None,None,None,None,None,None,
    put_text(f'Заказчик: {df["login_customer"].iloc[0]}'),
    put_text(f'Оплачено: {total_price}')])
    items.append(total_text)
    if df['status_operation'].iloc[0] == 'Исполнен':
        popup(f'Заказ {product_id}', items)
    else:  
        buttons_column = put_column([None,None,None,None,
        put_row([None, put_button("   В работу   ", onclick=lambda: update_order(sdep, tab, product_id, fio, id, 'В работе'), color='danger', outline=True),None,
                                put_button(" Выполнить", onclick=lambda: update_order(sdep, tab, product_id, fio, id, 'Исполнен'), color='danger', outline=True), None,
                                put_button(" Отменить ", onclick=lambda: delete_order(sdep, tab, product_id, fio, id), color='danger', outline=True),None], size='4% 30% 2% 30% 2% 30% 2%')])
        items.append(buttons_column)
            
        popup(f'Заказ {product_id}', items)

# Основная функция администратора (админ панель)
async def admin(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    img = open('img/1.png', 'rb').read()
    df_product = pd.read_sql(sql.sql_product, connect("Convert/db/shop.db"))
    df_user = pd.read_sql(sql.sql_user, connect("Convert/db/shop.db"))
    df_user_site = df_user[['fio', 'login', 'balance']]
    count = BotDS.get_order_count('Принят')[0]

    # функции обертки для обработки кликов в таблице
    async def delete_wrapper(row_id):
        await delete_product_and_row(row_id, df_product.to_dict(orient='records'), sdep, tab, fio, id)

    async def delete_wrapper_user(row_id):
        await delete_user_and_row(row_id, df_user.to_dict(orient='records'), sdep, tab, fio, id)

    async def reset_password(row_id):
        user_login = df_user.to_dict(orient='records')[row_id]['login']
        BotDS.update_user_password(user_login, str(BotDS.get_def_pass()))
        toast(f"Пароль для пользователя {user_login} сброшен на 123456")

    # Отображаем таблицу
    put_button("    Admin Panel                             ", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position:absolute;left:0%;top:0.5%;z-index:2147483647')
    put_row([
            #Сайд бар
            put_widget(css.tpl, {'contents':[
                put_row([
            put_image(img).style('background:#181d1f;border-radius:100px;position:absolute;width:50%;left:24%;top:20%;font-size:1vw;')])]
                                }).style('position:relative;background:#181d1f;z-index:1;filter: drop-shadow(1px 2px 3px #181d1f);'), None,
    put_column([
        None,
        put_row([
        put_button("user balance", onclick=lambda: chek_balance_users(df_user, 'admin', tab, fio, id), color='info').style('position:absolute;top:1%;right:5%;'),
        put_button("add product", onclick=lambda: add_product(df_product, sdep, tab, fio, id), color='info').style('position:absolute;top:1%;right:13%;'),
        put_button("   add user   ", onclick=lambda: add_user(df_user, sdep, tab, fio, id), color='info').style('position:absolute;top:1%;right:21%;'),
        put_button("   the store   ", onclick=lambda: noadmin(sdep, tab, fio, id), color='info').style('position:absolute;top:1%;right:29%;'),
        put_button(f"     order {count}    ", onclick=lambda: chek_order('admin', tab, fio, id), color='info').style("position:absolute;top:1%;right:37%;"), 
        ]),
        None,
    put_datatable(
        df_product.to_dict(orient='records'),
        actions=[
            ("delete product", delete_wrapper)
        ],
        theme='alpine-dark',
        instance_id='product',
        height='35vh'
    ).style('display:table'),
    None,
    put_row([
    put_datatable(
        df_user_site.to_dict(orient='records'),
        actions=[
            ("delete user", delete_wrapper_user),
            ("reset_password", reset_password)
        ],
        theme='alpine-dark',
        instance_id='user',
        height='35vh'
    ).style('display:table'),
    ])
    ], size='2% 3% 3% 40% 5% 40%')],
                    size='9% 5% 81%').style('position: absolute;width: 100%;height: 100%;')

# Основная функция администратора (работа с заказами)
async def chek_order(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    img = open('img/1.png', 'rb').read()
    df_order = pd.read_sql(sql.sql_order, connect("Convert/db/shop.db"))
    df_order_site = df_order[['id',
                         'datetime_insert',
                         'operation_type',
                         'login_customer',
                         'value_operation',
                         'status_operation']]
    # функции обертки для обработки кликов в таблице
    async def delete_wrapper_order(row_id):
        product_id = df_order.to_dict(orient='records')[row_id]['id']
        await order_open_admin(sdep, tab, product_id, fio, id)

    if df_order.empty:
        toast('Заказов больше нет')
        await admin(sdep, tab, fio, id)
    else:
        # Отображаем таблицу
        put_button("    Admin Panel                             ", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position:absolute;left:0%;top:0.5%;z-index:2147483647')
        put_row([
                #Сайд бар
                put_widget(css.tpl, {'contents':[
                    put_row([
                put_image(img).style('background:#181d1f;border-radius:100px;position:absolute;width:50%;left:24%;top:20%;font-size:1vw;')])]
                                    }).style('position:relative;background:#181d1f;z-index:1;filter: drop-shadow(1px 2px 3px #181d1f);'), None,
        put_column([
            None,
            put_row([
            put_button("   the store   ", onclick=lambda: noadmin(sdep, tab, fio, id), color='info').style('position:absolute;top:1%;right:5%;'),
            put_button("     back      ", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position:absolute;top:1%;right:13%;'),
            ]),
            None,
        put_datatable(
            df_order_site.to_dict(orient='records'),
            theme='alpine-dark',
            instance_id='product',
            height='80vh',
            onselect=delete_wrapper_order,
        ).style('display:table'),
        ], size='2% 3% 3% 85%')],
                        size='9% 5% 81%').style('position: absolute;width: 100%;height: 100%;')

# Основная функция администратора (работа с балансом)
async def chek_balance_users(df_user, sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    img = open('img/1.png', 'rb').read()
    df_balance = pd.read_sql(sql.sql_balance, connect("Convert/db/shop.db"))

        # Отображаем таблицу
    put_button("    Admin Panel                             ", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position:absolute;left:0%;top:0.5%;z-index:2147483647')
    put_row([
                #Сайд бар
            put_widget(css.tpl, {'contents':[
                put_row([
            put_image(img).style('background:#181d1f;border-radius:100px;position:absolute;width:50%;left:24%;top:20%;font-size:1vw;')])]
                                    }).style('position:relative;background:#181d1f;z-index:1;filter: drop-shadow(1px 2px 3px #181d1f);'), None,
    put_column([
        None,
        put_row([
        put_button("add balance", onclick=lambda: add_balans(df_user, sdep, tab, fio, id), color='info').style('position:absolute;top:1%;right:5%;'),
        put_button("     back      ", onclick=lambda: admin('admin', tab, fio, id), color='info').style('position:absolute;top:1%;right:13%;'),
            ]),
            None,
    put_datatable(
        df_balance.to_dict(orient='records'),
        theme='alpine-dark',
        instance_id='balance',
        height='80vh'
        ).style('display:table'),
        ], size='2% 3% 3% 85%')],
                        size='9% 5% 81%').style('position: absolute;width: 100%;height: 100%;')  


# Функция для удаления данных из таблица продуктов
async def delete_product_and_row(row_id, df, sdep, tab, fio, id):
        if len(df) == 1:
            toast("Нельзя полностью удалить все записи")
        else:
            row_bd = df[row_id]['id']
            BotDS.delete_product(row_bd)
            toast('Товар удален')
            await admin('admin', tab, fio, id)

# Функция для удаления данных из таблицы пользователь
async def delete_user_and_row(row_id, df, sdep, tab, fio, id):
        if len(df) == 1:
            toast("Нельзя полностью удалить все записи")
        else:
            row_bd = df[row_id]['index']
            BotDS.delete_user(row_bd)
            toast('Пользователь удален')
            await admin('admin', tab, fio, id)

# Функция для удаления заказа
async def delete_order(sdep, tab, product_id, fio, id):
        df = pd.read_sql(sql.sql_operations_one.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))
        if sdep == 'admin':
            BotDS.delete_order(product_id)
            close_popup()
            await chek_order(sdep, tab, fio, id)
            toast('Заказ удален')
        else:
            if df['status_operation'].iloc[0] == 'Принят':
                BotDS.delete_order(product_id)
                close_popup()
                await my_order(sdep, tab, fio, id)
                toast('Заказ удален')
            else:
                toast('Заказ в работе нельзя отменить')

# Функция для подтверждения заказа
async def update_order(sdep, tab, product_id, fio, id, status):
        if status == 'В работе':
            BotDS.update_order_status(status, product_id)
            popup('Заказ взят в работу')
            await chek_order(sdep, tab, fio, id)
        else:
            BotDS.update_order_status(status, product_id)
            popup('Заказ выполнен')
            await chek_order(sdep, tab, fio, id)

# Функция для добавления нового пользователя
async def add_user(df_user, sdep, tab, fio, id):
    def chek_user(login):
        if BotDS.user_exists(ID=login) == True:
            return 'Такой пользователь уже есть'
    try:
        clear()
        info = await input_group("Отредактируй\Заполни поля ниже",[
                    input(name = 'login', type=TEXT, label='Логин', value="", validate=chek_user),
                    input(name = 'fio', type=TEXT, label='ФИО', value=""),
                    ])
        
        BotDS.add_user(
            index=int(df_user['index'].max()) + 1,
            password=str(BotDS.get_def_pass()),
            sdep="noadmin",
            login=info['login'],
            fio=info['fio']
            )
        
        popup('Пользователь добавлен', put_text("Стандартный пароль для входа 123456, пользователь сможет его поменять при первом входе"))
        await admin('admin', tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

# Функция для добавления нового продукта
async def add_product(df_product, sdep, tab, fio, id):
    try:
        clear()
        info = await input_group("Отредактируй\Заполни поля ниже",[
                    input(name = 'name', type=TEXT, label='Название', value=""),
                    input(name = 'description', type=TEXT, label='Описание', value=""),
                    input(name = 'price', type=NUMBER, label='Цена', value=1000)
                    ])
        imgs = await file_upload("Select some pictures:", accept="image/*", multiple=False)
        with open(f"img/{imgs['filename']}", 'wb') as f:
            f.write(imgs['content'])
                
            
        BotDS.add_product(
            id=int(df_product['id'].max()) + 1,
            name=info['name'],
            description=info['description'],
            price=info['price'],
            img = f"img/{imgs['filename']}"
            )

        popup('Товар добавлен')
        await admin('admin', tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

# Функция для добавления баланса
async def add_balans(df_user, sdep, tab, fio, id):
    try:
        clear()
        login_options = df_user['login'].tolist()
        info = await input_group("Отредактируй\Заполни поля ниже",[
                    select(name='login', label='Выберите кому начисляем', options=login_options),
                    input(name = 'price', type=NUMBER, label='Сколько начислить', value=0)
                    ])
        
        BotDS.add_operation(operation_type='Начисление', json=None, login_customer=info['login'], value_operation=info['price'], status_operation='Исполнен')
        popup('Баланс начислен',[f"{str(info['login'])} {str(info['price'])}"])
        await chek_balance_users(df_user, sdep, tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))


# Вызов
if __name__ == '__main__':
    start_server(main, host = 'localhost', port = 8080, debug = True, cdn=True, secure=True)