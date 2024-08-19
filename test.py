put_column([
        # Внешняя обертка продукта
        put_column([
            # Блок с изображением продукта
            put_image(img_content).style("width: 100%; height: 200px; object-fit: cover; display: block;"),

            # Название продукта
            put_text(str(product['name'][0:20])).style(
                "color: #2e2e2e; font-weight: 600; margin: 15px 0 5px; padding-bottom: 7px; "
                "display: block; text-transform: uppercase; font-family: Lora, serif;"
                "text-align: center; font-size: 14px;"
            ),
            
            # Цена продукта
            put_text(f"₽ {product['price']}").style(
                "font-size: 20px; color: #c0a97a; font-weight: 700; text-align: center;"
            ),

            # Прозрачная кнопка, покрывающая всю карточку
            put_button("", 
                       onclick=lambda: order(str(product['id']), str(product['name']), product['img'], 
                                             product['price'], product['description'], product['color'], 
                                             product['size'], sdep, tab, fio), 
                       color='dark', outline=True).style(
                'position:absolute;top:0;left:0;width:100%;height:100%;opacity:0;'
                'transition: opacity 0.3s ease-in-out;'
            )
        ], style="position: relative; width: 300px; margin: 0 auto; background: white; padding-bottom: 20px; text-align: center;")
    ]).style(
        "position: relative; width: 300px; margin: 10px auto;"
    )
