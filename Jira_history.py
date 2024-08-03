    df_product = pd.read_sql(sql.sql_product, connect("Convert/db/shop.db"))
    img_ban = open('img/ban.jpg', 'rb').read()
    img_logo = open('img/logo.png', 'rb').read()
    product_cards = [await render_product_card(product, sdep, tab, fio) for _, product in df_product.iterrows()]

    sql_product =   """
               SELECT 
                    id,
                    name,
                    price,
                    description,
                    img,
                    color,
                    size,
                    prom
               FROM product
               ORDER BY prom desc, price asc
