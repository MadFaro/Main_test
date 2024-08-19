put_column([
        # Вставляем изображение
        put_image(image_url, width='100%'),

        # Вставляем название продукта и цену
        put_column([
            put_text(product_name, inline=True),  # Название продукта
            put_text(f"₽ {price}", inline=True),  # Цена продукта
        ], size='auto'),

        # Кнопка "В корзину"
        put_button(button_text, onclick=button_action)
    ], size='auto')
