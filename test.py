async def dashboard_user(df_user, sdep, tab, fio, id):
    try:
        clear()
    except:
        pass

    def create_login_chart(dates, login_counts):
        line = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(dates)
            .add_yaxis("Кол-во", login_counts, is_smooth=True)
            .set_series_opts(
                        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                        label_opts=opts.LabelOpts(is_show=False),)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Входы"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(type_="value"),
                datazoom_opts=[
                    opts.DataZoomOpts(type_="slider", range_start=80, range_end=100)
                ],
                legend_opts=opts.LegendOpts(is_show=True)  # Отображение легенды
            )
        )
        return line
    
    def create_multi_chart(dates, shop, game, box):
        line = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(dates)
            .add_yaxis("Зашел в магазин", shop, is_smooth=True)
            .add_yaxis("Зашел в гейм", game, is_smooth=True)
            .add_yaxis("Воспользовался боксом", box, is_smooth=True)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Сервисы"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(type_="value"),
                datazoom_opts=[
                    opts.DataZoomOpts(type_="slider", range_start=80, range_end=100)
                ],
                legend_opts=opts.LegendOpts(is_show=True)  # Отображение легенды
            )
        )
        return line

    def create_box_chart(dates, quest, offer, mood):
        line = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(dates)
            .add_yaxis("Задал вопрос", quest, is_smooth=True)
            .add_yaxis("Предложил идею", offer, is_smooth=True)
            .add_yaxis("Отправил настроение", mood, is_smooth=True)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Бокс ОС"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(type_="value"),
                datazoom_opts=[
                    opts.DataZoomOpts(type_="slider", range_start=80, range_end=100)
                ],
                legend_opts=opts.LegendOpts(is_show=True)  # Отображение легенды
            )
        )
        return line
    
    def create_orders_cancellations_chart(dates, order_counts, cancellation_counts):
        line = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(dates)
            .add_yaxis("Сделал", order_counts, is_smooth=True)
            .add_yaxis("Отменил", cancellation_counts, is_smooth=True)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Заказы"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(type_="value"),
                datazoom_opts=[
                    opts.DataZoomOpts(type_="slider", range_start=80, range_end=100)
                ],
                legend_opts=opts.LegendOpts(is_show=True)  # Отображение легенды
            )
        )
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
