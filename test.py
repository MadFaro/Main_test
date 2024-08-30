def json_to_html(json_obj):
    html = '<html><body>'
    html += '<h1>Ваш отчет по продуктам</h1>'
    html += '<table border="1" cellpadding="5" cellspacing="0">'
    html += '<tr>'
    html += '<th>ID продукта</th>'
    html += '<th>Название</th>'
    html += '<th>Количество</th>'
    html += '<th>Цена</th>'
    html += '<th>Изображение</th>'
    html += '<th>Размер</th>'
    html += '<th>Цвет</th>'
    html += '</tr>'
    
    for item in json_obj:
        html += '<tr>'
        html += f'<td>{item["product_id"]}</td>'
        html += f'<td>{item["name"]}</td>'
        html += f'<td>{item["count"]}</td>'
        html += f'<td>{item["subtotal_price"]}</td>'
        html += f'<td><img src="{item["img"]}" alt="{item["name"]}" style="width:100px;height:auto;"></td>'
        html += f'<td>{item["size"]}</td>'
        html += f'<td>{item["color"]}</td>'
        html += '</tr>'
    
    html += '</table>'
    html += '</body></html>'
    return html
