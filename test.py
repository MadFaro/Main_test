put_tabs([
        {
            'title': f"{str(product['name'][0:20])} - {product['price']} \U0001F6D2",
            'content': put_column([
                # Контейнер для карточки товара
                put_column([
                    # Блок с изображением продукта
                    put_image(img_content, width='100%').style(
                        "object-fit: cover; display: block; height: 200px;"),

                    # Название продукта
                    put_text(str(product['name'][0:20])).style(
                        "color: #2e2e2e; font-weight: 600; margin: 15px 0 5px; padding-bottom: 7px; "
                        "text-transform: uppercase; font-family: Lora, serif; text-align: center; font-size: 14px;"
                    ),

                    # Цена продукта
                    put_text(f"₽ {product['price']}").style(
                        "font-size: 20px; color: #c0a97a; font-weight: 700; text-align: center;"
                    ),

                    # Прозрачная кнопка, покрывающая всю карточку
                    put_button("", 
                               onclick=lambda: order(
                                   str(product['id']), str(product['name']), product['img'],
                                   product['price'], product['description'], product['color'],
                                   product['size'], sdep, tab, fio
                               ),
                               color='dark', outline=True).style(
                        'position:absolute; top:0; left:0; width:100%; height:100%; opacity:0;'
                        'transition: opacity 0.3s ease-in-out;'
                    )
                ]).style(
                    "position: relative; width: 300px; margin: 0 auto; background: white; padding: 0; text-align: center;"
                )
            ])
        }
    ]).style(
        "display: block; width: 300px; margin: 0 auto; padding: 0; position: relative;"
    )
