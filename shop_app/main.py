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


# Конект к БД
BotDS = BotDB('Convert/db/shop.db')

# Авторизация
@config(theme = 'yeti', css_style = css.container_output, description='shop', title='shop')
async def main():
    def validate_login(tab):
        if not re.match("^[a-zA-Z]+$", tab):
            return 'Логин должен содержать только буквы английского алфавита (строчные и прописные).'
    try:
        id_select = await input_group("Вход",
                                        [
                            input('Логин', name='tab', type=TEXT, validate=validate_login),
                            input('Пароль', name='password', type=PASSWORD)
                                        ])
        tab = id_select['tab']
        password = str(hashlib.sha256(str(id_select['password']).encode()).hexdigest())
        rezult = BotDS.user_exists(ID=tab)
        def_pass = str(BotDS.get_def_pass())

        if rezult == False:
            toast('Неверный логин', duration=0, position='center', color='error')

        elif rezult == True and str(BotDS.get_user_pass(ID=tab)) == def_pass and password == def_pass:
            id_select_2 = await input_group("Введи новый пароль",
                                        [
                            input('Пароль', name='password', type=PASSWORD)
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

        else:
            toast('Неверный пароль', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

    except:
        clear()
        toast('Нет праыв', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

# Основная функция для отображения пользователям (без админ прав)
async def noadmin(sdep, tab, fio, id):
    # Очищаем 
    try:
        clear()
    except:
        pass

    df_product = pd.read_sql(sql.sql_product, connect("Convert/db/shop.db"))
    img_ban = open('img/ban.jpg', 'rb').read()
    product_cards = [await render_product_card(product, sdep, tab) for _, product in df_product.iterrows()]

    rows = []
    for i in range(0, len(product_cards), 3):
        row_items = product_cards[i:i+3]
        row_with_none = [put_column(card) if card else None for card in row_items]
        row_with_none.insert(1, None) 
        row_with_none.insert(3, None)
        row = put_row(row_with_none)
        rows.append(row)

    rows_grid = []
    for row in rows:
        rows_grid.append(row)

    if sdep == 'admin':
        put_button("    Admin panel", onclick=lambda: admin(sdep, tab, fio, id), color='info').style('position: fixed;left:0%;top:37%;z-index:2147483647')
    else:
        put_button("     The store    ", onclick=lambda: noadmin(sdep, tab, fio, id), color='info').style('position: fixed;left:0%;top:37%;z-index:2147483647')
        put_button("     My balance", onclick=lambda: my_balance(tab, fio), color='info').style('position: fixed;left:0%;top:44%;z-index:2147483647')
        put_button("     My orders  ", onclick=lambda: my_order(sdep, tab, fio, id), color='info').style('position: fixed;left:0%;top:51%;z-index:2147483647')
    put_row([
        None,
    put_column([
        put_image(img_ban).style('width: 100%;box-shadow: 0 0 20px rgba(138, 43, 226, 0.5);'),
        put_tabs([{'title':'Одежда', 'content':[
        put_column(
        rows_grid)]},
        {'title': 'Техника', 'content': 
         [put_column(
        rows_grid)]},
        {'title': 'Что-то еще', 'content': 
                [put_column(
                rows_grid)]}
        ]).style('width: 100%;height: 100%;font-size: 1.5vh;transform: translateY(-5px);box-shadow: 0 0px 0px rgba(0, 0, 0, 0);;transition: transform 0s ease, box-shadow 0s ease;transition: all 0s ease; border-radius: 0px;border-color: white;transition: none; ')], size='auto')],
                    size='13% 2% 80%').style('position: absolute;width: 100%;height: 100%') 

# Функция для создания карточки товара
async def render_product_card(product, sdep, tab):
    with open(product['img'], 'rb') as img_file:
        img_content = img_file.read()
    return [
        put_tabs([{'title': str(product['name']), 'content':[
        put_image(img_content, width='100%', height="90%"),
        put_text(f"Цена: {product['price']} руб."),
        put_button("Заказать", onclick=lambda: order(str(product['id']), str(product['name']),product['img'], product['price'], product['description'], sdep, tab), color='warning', link_style=True, outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);font-size:1vw')
        ]}]).style('grid-template-columns:1fr;')
    ]

# Функция для обработки заказа (Показывает карточку с описанием и просит подтвердить выбор)
async def order(id, name, img, price, description, sdep, tab):
    with open(img, 'rb') as img_file:
        img_content = img_file.read()
    size_options = ['S', 'M', 'L', 'XL', 'XXL']
    color_options = ['Черный', 'Белый', 'Красный']
    return popup(f"{name} - {price} руб.",
                 [
                     put_image(img_content, width='100%', height="30%"),
                     put_text(f"Описание:\n{description}"),
                     put_row([
                     put_select(name='size', label='Выберите размер:', options=size_options),None,
                     put_select(name='color', label='Выберите цвет:', options=color_options),], size = '49% 2% 29%'),
                    put_button("Подтвердить заказ", onclick=lambda: order_add(id, description, sdep, tab, price), color='warning', outline=True).style('z-index:2147483647')
                 ], size='normal')

# Аналогично только для админа
async def order_admin(row_id, df, sdep):
    img = df[row_id]['img']
    with open(img, 'rb') as img_file:
        img_content = img_file.read()
    return popup(f"{str(df[row_id]['name'])} - {df[row_id]['price']} руб.",[
            put_image(img_content, width='100%', height="90%"),
            put_text(f"Описание:\n{df[row_id]['description']}"),
            put_button("Подтвердить заказ", onclick=lambda: order_add_admin(row_id, df, sdep), color='warning', outline=True).style('z-index:2147483647')
        ])

# Функция обработки заказа
async def order_add(id, description, sdep, tab, price):
    if sdep == 'admin':
        pass
    else:
        balans = BotDS.get_user_balanse(tab)[0]
        if balans < price:
            close_popup()
            toast('Недостаточно средств')
        else:
            selected_size = await pin['size']
            selected_color = await pin['color']
            BotDS.add_operation(operation_type='subtract', product_id=id, login_customer=tab, value_operation=-price, status_operation='accept')
            close_popup()
            toast('Заказ принят')

# Аналогично для админа
async def order_add_admin(row_id, df, sdep):
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

    # Грузим из БД наши товары
    df_operation = pd.read_sql(sql.sql_operations.replace('Замена', str(tab)), connect("Convert/db/shop.db"))
    if df_operation.empty:
        toast("У тебя нет операций")
    else:
        put_button("     The store    ", onclick=lambda: noadmin(sdep, tab, fio, id), color='info').style('position: fixed;left:0%;top:37%;z-index:2147483647')
        put_button("     My balance", onclick=lambda: my_balance(tab, fio), color='info').style('position: fixed;left:0%;top:44%;z-index:2147483647')
        put_button("     My orders  ", onclick=lambda: my_order(sdep, tab, fio, id), color='info').style('position: fixed;left:0%;top:51%;z-index:2147483647')
        put_row([
            None,
        put_column([
            None,
            put_datatable(df_operation.to_dict('records'), theme='alpine-dark')], size='5% 95%')],
                        size='9% 88%').style('position: absolute;width: 100%;height: 100%;')         
    
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
    count = BotDS.get_order_count('accept')[0]

    # функции обертки для обработки кликов в таблице
    async def delete_wrapper(row_id):
        await delete_product_and_row(row_id, df_product.to_dict(orient='records'), sdep, tab, fio, id)

    async def delete_wrapper_user(row_id):
        await delete_user_and_row(row_id, df_user.to_dict(orient='records'), sdep, tab, fio, id)

    async def order_wrapper(row_id):
        await order_admin(row_id, df_product.to_dict(orient='records'), tab)

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
            ("delete product", delete_wrapper),
            ("product card", order_wrapper)
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
    df_product = pd.read_sql(sql.sql_product, connect("Convert/db/shop.db"))

    # функции обертки для обработки кликов в таблице
    async def delete_wrapper_order(row_id):
        await order_card_admin(row_id, df_order.to_dict(orient='records'), df_product, sdep, tab, fio, id)

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
            put_button("     back      ", onclick=lambda: admin('admin', tab, fio, id), color='info').style('position:absolute;top:1%;right:13%;'),
            ]),
            None,
        put_datatable(
            df_order.to_dict(orient='records'),
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
        
# Формирование карточки заказа
async def order_card_admin(row_id, df_order, df_product, sdep, tab, fio, id):
    if df_order[row_id]['status_operation'] == 'accept':
        id_product = df_order[row_id]['product_id']
        img = df_product.loc[df_product['id'] == id_product, 'img'].values[0]
        name = df_product.loc[df_product['id'] == id_product, 'name'].values[0]
        price = df_product.loc[df_product['id'] == id_product, 'price'].values[0]
        with open(img, 'rb') as img_file:
            img_content = img_file.read()
        return popup(f"Заказ {df_order[row_id]['id']}",[
                put_text(f"Товар:{name}"),
                put_image(img_content, width='100%', height="90%"),
                put_text(f"Заказчик:{df_order[row_id]['login_customer']}"),
                put_text(f"Цена:{price}"),
                put_row([
                put_button("Выполнить", onclick=lambda: update_order(row_id, df_order, sdep, tab, fio, id), color='warning', outline=True).style('z-index:2147483647'),
                put_button("Отменить ", onclick=lambda: delete_order(row_id, df_order, sdep, tab, fio, id), color='warning', outline=True).style('position:absolute;right:3%;z-index:2147483647')])
                
            ])
    else:
        id_product = df_order[row_id]['product_id']
        img = df_product.loc[df_product['id'] == id_product, 'img'].values[0]
        name = df_product.loc[df_product['id'] == id_product, 'name'].values[0]
        price = df_product.loc[df_product['id'] == id_product, 'price'].values[0]
        with open(img, 'rb') as img_file:
            img_content = img_file.read()
        return popup(f"Заказ {df_order[row_id]['id']}",[
                put_text(f"Товар:{name}"),
                put_image(img_content, width='100%', height="90%"),
                put_text(f"Заказчик:{df_order[row_id]['login_customer']}"),
                put_text(f"Цена:{price}")])    


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

# Функция для удаления данных из таблицы пользователь
async def delete_order(row_id, df, sdep, tab, fio, id):
        if len(df) == 1:
            toast("Нельзя полностью удалить все записи")
        else:
            row_bd = df[row_id]['id']
            BotDS.delete_order(row_bd)
            popup('Заказ удален')
            await chek_order('admin', tab, fio, id)

# Функция для подтверждения заказа
async def update_order(row_id, df, sdep, tab, fio, id):
        row_bd = df[row_id]['id']
        BotDS.update_order_status(row_bd)
        popup('Заказ подтвержден')
        await chek_order('admin', tab, fio, id)

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
        
        BotDS.add_operation(operation_type='addition', product_id=0, login_customer=info['login'], value_operation=info['price'], status_operation='executed')
        popup('Баланс начислен',[f"{str(info['login'])} {str(info['price'])}"])
        await chek_balance_users(df_user, sdep, tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))


# Вызов
if __name__ == '__main__':
    start_server(main, host = 'localhost', port = 8080, cdn=True, secure=True)