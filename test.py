put_column([
        # Внешняя обертка продукта
        put_column([
            # Блок с изображением продукта
            put_image(image_url).style("width: 100%; display: block;"),

            # Название продукта
            put_text(product_name).style(
                "color: #2e2e2e; font-weight: 600; margin: 15px 0 5px; padding-bottom: 7px; "
                "display: block; position: relative; text-transform: uppercase; font-family: Lora, serif;"
                "text-align: center; font-size: 14px;"
            ),
            
            # Цена продукта
            put_text(f"₽ {price}").style(
                "font-size: 20px; color: #c0a97a; font-weight: 700; text-align: center;"
            ),
            
            # Кнопка "В корзину"
            put_button(button_text, onclick=button_action).style(
                "text-decoration: none; color: #c0a97a; font-size: 12px; width: 140px; height: 40px; "
                "line-height: 40px; border: 2px solid #c0a97a; display: block; margin: 10px auto; "
                "background: transparent; text-align: center; transition: background .3s ease-in-out;"
            ).onclick(button_action)
        ]).style(
            "width: 300px; margin: 0 auto; background: white; padding: 0 0 20px; text-align: center;"
        )
    ])
