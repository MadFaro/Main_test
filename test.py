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
        
        for (product_id, size, color, name), group_df in df.groupby(['product_id', 'size', 'color', 'name']):
            count = len(group_df) 
            img_url = open(group_df.iloc[0]['img'], 'rb').read()
            subtotal_price = group_df['price'].sum()
            total_price += subtotal_price
            
            item_data = {
                'product_id': str(product_id),
                'name': str(name),
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
            item_button = put_button("x", onclick=lambda: basket_delete_one(tab, product_id, size, color), color='info', outline=True)

            items.append(put_row([None, item_text, None, item_image, None, item_size, None, item_color, None, item_price, None, item_button, None], size='1% 10% 1% 35% 1% 10% 1% 10% 1% 10% 1% 10% 1%').style('display: flex;justify-content: space-between;align-items: center;'))
        
        json_data = json.dumps(basket_data)
        
        total_text = put_column([None,None,None,None,None,None,None,None,None,None,None,None,
        put_text(f'К оплате: {total_price}')])
        items.append(total_text)
        buttons_column = put_row([put_button("Оплатить", onclick=lambda: basket_accept(json_data, tab, int(total_price)), color='info', outline=True),None,
                                    put_button("Очистить", onclick=lambda: basket_delete_all(tab), color='info', outline=True)], size='25% 2% 25%')
        items.append(buttons_column)
        popup('Корзина', items)

