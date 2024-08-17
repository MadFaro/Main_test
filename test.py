popup(f"{name} - {price} баллов",
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
                            put_widget(tpl, data),
                            put_button("В корзину", onclick=lambda: basket_add(id, img, tab, price, sdep, fio, name), color='info', outline=True)
                        ], size='normal')
