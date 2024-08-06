        put_tabs([{'title': f"БОКС ОБРАТНОЙ СВЯЗИ", 'content':[
                    put_column([
                    put_image(open('main_menu/img/logo3.png', 'rb').read(), width='100%', height="100%")
                    ]).style('grid-template-rows:1fr'),
                    put_button("", onclick=lambda: box_menu(sdep, tab, fio, id), 
                            color='dark', outline=True).style('position:absolute;top:0%;right:0%;filter:opacity(0.5);font-size:1vw;height: 100%;width: 100%;')
                ]}]).style('grid-column: span 1; grid-row: span 1;display: block;')
