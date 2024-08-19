put_tabs([{'title': f"{str(product['name'][0:20])} - {product['price']} \U0001F6D2", 'content':[
            put_column([
            put_column([
            put_image(img_content, width='100%', height="100%").style("object-fit: cover; display: block;"),
            put_text(str(product['name'][0:20])).style(
                "color: #2e2e2e; font-weight: 600; margin: 15px 0 5px; padding-bottom: 7px; "
                "display: block; text-transform: uppercase; font-family: Lora, serif;"
                "text-align: center; font-size: 14px;"
            ),
            put_text(f"₽ {product['price']}").style(
                "font-size: 20px; color: #c0a97a; font-weight: 700; text-align: center;"
            ),
            put_button("", 
                       onclick=lambda: order(str(product['id']), str(product['name']), product['img'], 
                                             product['price'], product['description'], product['color'], 
                                             product['size'], sdep, tab, fio), 
                       color='dark', outline=True).style(
                'position:absolute;top:0;left:0;width:100%;height:100%;'
            )
        ]).style("grid-template-rows: 1fr 0.1fr 0.1fr 0.1fr;padding: 0rem;")
        ]).style("position: relative;")
        ]}]).style('grid-column: span 1; grid-row: span 1;display: block;')
        
    )
