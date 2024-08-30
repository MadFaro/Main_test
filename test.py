async def add_balans(df_user, sdep, tab, fio, id):
    try:
        clear()
        excel_file = await file_upload("Выберите Excel файл:", accept=".xlsx")
        with BytesIO(excel_file['content']) as buffer:
            df = pd.read_excel(buffer)
        df['operation_type'] = 'Начисление'
        df['status_operation'] = 'Исполнен'
        df['json'] = None
        df[['login_customer', 'value_operation', 'operation_type', 'status_operation', 'json']].dropna(subset=['value_operation']).to_sql('operations', connect("Convert/db/shop.db"), if_exists='append', index=False)
        popup('Баланс начислен')
        await chek_balance_users(df_user, sdep, tab, fio, id)
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))

# Дашборды

async def dashboard_user(df_user, sdep, tab, fio, id):
    try:
        clear()
    except:
        pass

    def create_login_chart(dates, login_counts):
        data = [{"date": date, "login_counts": count} for date, count in zip(dates, login_counts)]
        line = Plot("Line")
        line.set_options({
            "appendPadding": 32,
            "data": data,
            "xField": "date",
            "yField": "login_counts",
            "smooth": True,
            "lineStyle": {
                "lineWidth": 3,
            },
            "point": {
                "size": 5,
                "shape": 'diamond',
                "style": {
                    "fill": "white",
                    "stroke": "#5B8FF9",
                    "lineWidth": 2,
                }
            },
            "xAxis": {
                "title": "Дата"
            },
            "yAxis": {
                "title": "Кол-во"
            },
            "tooltip": {
                "showMarkers": False
            },
            "legend": {
                "position": "top"
            }
        })
        return line

    def create_multi_chart(dates, shop, game, box):
        data = [{"date": date, "shop": s, "game": g, "box": b} for date, s, g, b in zip(dates, shop, game, box)]
        line = Plot("Line")
        line.set_options({
            "appendPadding": 32,
            "data": data,
            "xField": "date",
            "yField": ["shop", "game", "box"],
            "seriesField": "type",
            "smooth": True,
            "lineStyle": {
                "lineWidth": 3,
            },
            "point": {
                "size": 5,
                "shape": 'diamond',
                "style": {
                    "fill": "white",
                    "stroke": "#5B8FF9",
                    "lineWidth": 2,
                }
            },
            "xAxis": {
                "title": "Дата"
            },
            "yAxis": {
                "title": "Количество"
            },
            "tooltip": {
                "showMarkers": False
            },
            "legend": {
                "position": "top"
            }
        })
        return line

    def create_box_chart(dates, quest, offer, mood):
        data = [{"date": date, "quest": q, "offer": o, "mood": m} for date, q, o, m in zip(dates, quest, offer, mood)]
        line = Plot("Line")
        line.set_options({
            "appendPadding": 32,
            "data": data,
            "xField": "date",
            "yField": ["quest", "offer", "mood"],
            "seriesField": "type",
            "smooth": True,
            "lineStyle": {
                "lineWidth": 3,
            },
            "point": {
                "size": 5,
                "shape": 'diamond',
                "style": {
                    "fill": "white",
                    "stroke": "#5B8FF9",
                    "lineWidth": 2,
                }
            },
            "xAxis": {
                "title": "Дата"
            },
            "yAxis": {
                "title": "Количество"
            },
            "tooltip": {
                "showMarkers": False
            },
            "legend": {
                "position": "top"
            }
        })
        return line

    def create_orders_cancellations_chart(dates, order_counts, cancellation_counts):
        data = [{"date": date, "order_counts": o, "cancellation_counts": c} for date, o, c in zip(dates, order_counts, cancellation_counts)]
        line = Plot("Line")
        line.set_options({
            "appendPadding": 32,
            "data": data,
            "xField": "date",
            "yField": ["order_counts", "cancellation_counts"],
            "seriesField": "type",
            "smooth": True,
            "lineStyle": {
                "lineWidth": 3,
            },
            "point": {
                "size": 5,
                "shape": 'diamond',
                "style": {
                    "fill": "white",
                    "stroke": "#5B8FF9",
                    "lineWidth": 2,
                }
            },
            "xAxis": {
                "title": "Дата"
            },
            "yAxis": {
                "title": "Количество"
            },
            "tooltip": {
                "showMarkers": False
            },
            "legend": {
                "position": "top"
            }
        })
        return line

    img = open('img/1.png', 'rb').read()
    # Кол-во входов
    df = pd.read_sql(sql.sql_dash_one, connect("Convert/db/shop.db"))
    df_online = pd.read_sql(sql.sql_online, connect("Convert/db/shop.db"))

    dates = df['date'].tolist()
    cnt_login = df['cnt_up'].tolist()
    cnt_shop = df['cnt_shop'].tolist()
    cnt_game = df['cnt_game'].tolist()
    cnt_box = df['cnt_box'].tolist()
    cnt_quest = df['cnt_quest'].tolist()
    cnt_offer = df['cnt_offer'].tolist()
    cnt_mood = df['cnt_mood'].tolist()
    cnt_orders= df['cnt_orders'].tolist()
    cnt_cancel= df['cnt_cancellations'].tolist()

    chart = create_login_chart(dates, cnt_login)
    chart2 = create_multi_chart(dates, cnt_shop, cnt_game, cnt_box)
    chart3 = create_box_chart(dates, cnt_quest, cnt_offer, cnt_mood)
    chart4 = create_orders_cancellations_chart(dates, cnt_orders, cnt_cancel)

    put_column([

    put_row([
    None,
    put_text("Статистика").style("text-align: center;font-size: xx-large;"),
    put_button("     back      ", onclick=lambda: admin('admin', tab, fio, id), color='primary', outline=True).style('width:100%;height:100%;padding:0.5em;')]).style('grid-template-columns: 0.1fr 1fr 0.1fr;'),

    None,

    put_row([
    None,
    put_html(chart.render_notebook()),
    put_html(chart2.render_notebook()),
    None
    ]).style('grid-template-columns: 0.5fr 1fr 1fr 0.1fr;'),
    None,
    put_row([
    None,
    put_html(chart3.render_notebook()),
    put_html(chart4.render_notebook()),
    ]).style('grid-template-columns: 0.5fr 1fr 1fr 0.1fr;'),
    put_text("Активные сессии").style("text-align: center;font-size: xx-large;"),
    put_row([None,
    put_datatable(
        df_online.to_dict(orient='records'),
        theme='material',
        instance_id='balance',
        height='40vh',
        cell_content_bar=False
        ).style('display:table;'),
    None]).style('grid-template-columns: 0.05fr 1fr 0.05fr;')
    
    ]).style('grid-template-rows: 0.1fr 0.01fr 1fr 0.01fr 1fr')
