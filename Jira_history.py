# Функция для обработки заказа (Показывает карточку с описанием и добавлением в корзину)
async def order(id, name, img, price, description, color, size, sdep, tab, fio):
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
                            put_button("В корзину", onclick=lambda: basket_add(id, img, tab, price, sdep, fio, name), color='danger', outline=True)
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
                            put_button("В корзину", onclick=lambda: basket_add(id, img, tab, price, sdep, fio, name), color='danger', outline=True)
                        ], size='normal')
