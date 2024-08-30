

async def dashboard_user(df_user, sdep, tab, fio, id):
    try:
        clear()
    except:
        pass

    def create_login_chart(dates, login_counts):
        p = figure(x_range=dates, title="Входы", width=800, height=400,
                   toolbar_location=None, tools="hover", tooltips="@x: @y")
        p.line(x=dates, y=login_counts, line_width=2, legend_label="Кол-во", line_color="blue")
        p.circle(x=dates, y=login_counts, size=8, color="blue", fill_alpha=0.6)
        p.legend.location = "top_left"
        p.xaxis.axis_label = "Дата"
        p.yaxis.axis_label = "Количество"
        p.xaxis.major_label_orientation = 1.2
        return p

    def create_multi_chart(dates, shop, game, box):
        p = figure(x_range=dates, title="Сервисы", width=800, height=400,
                   toolbar_location=None, tools="hover", tooltips="@x: @y")
        p.line(x=dates, y=shop, line_width=2, legend_label="Зашел в магазин", line_color="green")
        p.line(x=dates, y=game, line_width=2, legend_label="Зашел в гейм", line_color="orange")
        p.line(x=dates, y=box, line_width=2, legend_label="Воспользовался боксом", line_color="red")
        p.legend.location = "top_left"
        p.xaxis.axis_label = "Дата"
        p.yaxis.axis_label = "Количество"
        p.xaxis.major_label_orientation = 1.2
        return p

    def create_box_chart(dates, quest, offer, mood):
        p = figure(x_range=dates, title="Бокс ОС", width=800, height=400,
                   toolbar_location=None, tools="hover", tooltips="@x: @y")
        p.line(x=dates, y=quest, line_width=2, legend_label="Задал вопрос", line_color="purple")
        p.line(x=dates, y=offer, line_width=2, legend_label="Предложил идею", line_color="brown")
        p.line(x=dates, y=mood, line_width=2, legend_label="Отправил настроение", line_color="pink")
        p.legend.location = "top_left"
        p.xaxis.axis_label = "Дата"
        p.yaxis.axis_label = "Количество"
        p.xaxis.major_label_orientation = 1.2
        return p

    def create_orders_cancellations_chart(dates, order_counts, cancellation_counts):
        p = figure(x_range=dates, title="Заказы", width=800, height=400,
                   toolbar_location=None, tools="hover", tooltips="@x: @y")
        p.line(x=dates, y=order_counts, line_width=2, legend_label="Сделал", line_color="blue")
        p.line(x=dates, y=cancellation_counts, line_width=2, legend_label="Отменил", line_color="red")
        p.legend.location = "top_left"
        p.xaxis.axis_label = "Дата"
        p.yaxis.axis_label = "Количество"
        p.xaxis.major_label_orientation = 1.2
        return p
    
    # Получение данных из базы данных
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
    cnt_orders = df['cnt_orders'].tolist()
    cnt_cancel = df['cnt_cancellations'].tolist()

    # Создание графиков
    chart = create_login_chart(dates, cnt_login)
    chart2 = create_multi_chart(dates, cnt_shop, cnt_game, cnt_box)
    chart3 = create_box_chart(dates, cnt_quest, cnt_offer, cnt_mood)
    chart4 = create_orders_cancellations_chart(dates, cnt_orders, cnt_cancel)

    # Получение HTML компонентов для вставки на страницу
    script1, div1 = components(chart)
    script2, div2 = components(chart2)
    script3, div3 = components(chart3)
    script4, div4 = components(chart4)

    # Отображение контента на странице
    put_column([

        put_row([
            None,
            put_text("Статистика").style("text-align: center; font-size: xx-large;"),
            put_button("     back      ", onclick=lambda: admin('admin', tab, fio, id), color='primary', outline=True).style('width:100%; height:100%; padding:0.5em;')
        ]).style('grid-template-columns: 0.1fr 1fr 0.1fr;'),

        None,

        put_row([
            put_html(div1).style('width:100%'),
            put_html(div2).style('width:100%'),
        ]).style('display: flex; flex-direction: row; gap: 1em;'),

        None,

        put_row([
            put_html(div3).style('width:100%'),
            put_html(div4).style('width:100%'),
        ]).style('display: flex; flex-direction: row; gap: 1em;'),

        put_text("Активные сессии").style("text-align: center; font-size: xx-large;"),

        put_row([
            put_datatable(
                df_online.to_dict(orient='records'),
                theme='material',
                instance_id='balance',
                height='40vh',
                cell_content_bar=False
            ).style('width:100%')
        ]).style('display: flex; justify-content: center;'),
    ])

    # Отображение скриптов для интерактивности графиков
    put_html(f"<script>{script1}</script>")
    put_html(f"<script>{script2}</script>")
    put_html(f"<script>{script3}</script>")
    put_html(f"<script>{script4}</script>")
