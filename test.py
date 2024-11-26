async def update_product_and_row(row_id, df, sdep, tab, fio, id):
    try:
        close_popup()
    except:
        pass

    popup(f"Товар {df[row_id]['id']}",
          [
                put_textarea("admin_update_product_name", label = "Название:", value = df[row_id]['name'], readonly=False, rows=1),
                put_input("admin_update_product_price", type=NUMBER, label="Цена:", value=df[row_id]['price']),
                put_textarea("admin_update_product_desc", label = "Описание:", value = df[row_id]['description'], readonly=False, rows=3),
                put_text("") if df[row_id]['size'] == "[]" else put_checkbox("admin_update_product_size", label = "Размер:", options=["S", "M", "L", "XL", "XXL", "XXXL"], inline=True, value=str(df[row_id]['size']).strip("[]").replace("'", "").split(", ")),
                put_text("") if df[row_id]['color'] == "[]" else put_checkbox("admin_update_product_color", label = "Цвет:", options=["Белый", "Серый", "Фиолетовый"], inline=True, value=str(df[row_id]['color']).strip("[]").replace("'", "").split(", ")),
                put_input("admin_update_product_prom", type=NUMBER, label="Укажите скидку до 100%", value=df[row_id]['prom']),
                put_button("Обновить товар", onclick=lambda: update_product_bd(sdep, tab, fio, id, df[row_id]['id']), color='info', outline=True)
                ]) 

async def update_product_bd(sdep, tab, fio, id, product_id):
    try:
        close_popup()
    except:
        pass
    name_up_pin = await pin['admin_update_product_name']
    price_up_pin = await pin['admin_update_product_price']
    desc_up_pin = await pin['admin_update_product_desc']
    size_up_pin = await pin['admin_update_product_size']
    color_up_pin = await pin['admin_update_product_color']
    prom_up_pin = await pin['admin_update_product_prom']

    print(name_up_pin)
    print(price_up_pin)
    print(desc_up_pin)
