put_column([
        # Внешняя обертка продукта
        put_column([
            # Блок с изображением продукта
            put_image(img_content, width='100%', height="100%").style("width: 100%; display: block;"),

            # Название продукта
            put_text(str(product['name'][0:20])).style(
                "color: #2e2e2e; font-weight: 600; margin: 15px 0 5px; padding-bottom: 7px; "
                "display: block; position: relative; text-transform: uppercase; font-family: Lora, serif;"
                "text-align: center; font-size: 14px;"
            ),
            
            # Цена продукта
            put_text(f"₽ {product['price']}").style(
                "font-size: 20px; color: #c0a97a; font-weight: 700; text-align: center;"
            ),
            
            # Кнопка "В корзину"
            put_button("", onclick=lambda: order(str(product['id']), str(product['name']),product['img'], product['price'], product['description'], product['color'], product['size'], sdep, tab, fio), 
                       color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
        ]).style(
            "width: 300px; margin: 0 auto; background: white; padding: 0 0 20px; text-align: center;"
        )
    ])
