async def main_menu(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    img_ban = open('main_menu/img/ban.jpg', 'rb').read()
    img_logo = open('img/logo.png', 'rb').read()
    marquee_html = """
    <marquee behavior="scroll" direction="left" scrollamount="5" style="font-size: 25px; color: violet; margin-bottom: 20px;">
        Это пример бегущей строки! Здесь можно разместить любое сообщение.
    </marquee>
    """
    
    # Кнопки с анимацией
    def styled_button(content, onclick, color='dark', outline=True):
        return put_button(content, onclick=onclick, color=color, outline=outline).style(''' 
            position:absolute;
            top:0%;right:0%;
            filter:opacity(0.5);
            font-size:1vw;
            height: 100%;
            width: 100%;
            transition: transform 0.2s ease-in-out, background-color 0.2s ease-in-out;
            &:hover {
                transform: scale(1.05);
                background-color: rgba(255, 255, 255, 0.1);
            }
        ''')
    
    product_cards = []
    product_cards.append(
        put_tabs([{'title': f"ТВОЙ МАГАЗИН МЕРЧА", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo1.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 10px; overflow:hidden;'),
                    styled_button("", onclick=lambda: noadmin(sdep, tab, fio, id))
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;text-align:center;')
    )
    product_cards.append(
        put_tabs([{'title': f"ГЕЙМИФИКАЦИЯ", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo2.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 10px; overflow:hidden;'),
                    styled_button("", onclick=lambda: game_noadmin(sdep, tab, fio, id))
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;')
    )
    product_cards.append(
        put_tabs([{'title': f"БОКС ОБРАТНОЙ СВЯЗИ", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo3.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 10px; overflow:hidden;'),
                    styled_button("", onclick=lambda: box_menu(sdep, tab, fio, id))
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;')
    )
    
    rows_grid = put_grid(rows, cell_width='auto', cell_height='auto').style('''
        justify-content:center;
        gap:5vh;
        grid-template-columns: repeat(auto-fill, minmax(200px, calc(100% / 4)));
        padding: 2em;
        background: linear-gradient(45deg, #e0e0e0, #f0f0f0);
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    ''')
    
    put_row([
        None,
        put_image(img_logo, width='auto', height='auto').style('place-self: center; filter: drop-shadow(2px 4px 6px #000);'),
        put_button("ВЫХОД", onclick=lambda: exit_shop(tab), color='dark', outline=True).style('''
            padding: 0.8em 2em;
            background: linear-gradient(135deg, #ff4d4d, #ff0000);
            border: none;
            color: white;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 25px;
            transition: background-color 0.3s ease-in-out;
            &:hover {
                background-color: #ff1a1a;
            }
        ''')
    ]).style('padding:0.4em;background:rgb(255 255 255);grid-template-columns:0.01fr 1fr 0.01fr;')
    
    put_image(img_ban, width='auto', height='auto').style('width:100%;filter: drop-shadow(1px 2px 4px #181d1f); border-radius: 10px;')
    
    put_row([
        put_column([
            put_tabs([
            {'title':'', 'content':
            [put_column(rows_grid)]}
           ]).style("width:100%;height:50%;transform:translateY(-5px);border-color:white;justify-content:center;display:grid;"),
           None,
           put_html("""
            <footer class="footer" style="background: linear-gradient(45deg, #333, #555); color: white; padding: 1em;">
            <a href="" target="_blank" style="color: #ffcc00;">uralsib</a>
            </footer>
           """).style("width:100%;z-index:2147483647;")
        ], size='auto')]
        ,size='auto').style('position:absolute;width:100%;height:50%;background: linear-gradient(45deg, #e0e0e0, #f0f0f0);')
    
           ], size='auto')]
                ,size='auto').style('position:absolute;width:100%;height:50%;')
