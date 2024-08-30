import plotly.graph_objects as go
import pandas as pd
from pywebio.output import put_column, put_row, put_html, put_text, put_button, put_datatable, clear

async def dashboard_user(df_user, sdep, tab, fio, id):
    try:
        clear()
    except:
        pass

    def create_login_chart(dates, login_counts):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=login_counts, mode='lines+markers', name='Кол-во'))
        fig.update_layout(
            title='Входы',
            xaxis_title='Дата',
            yaxis_title='Количество',
            template='plotly_white',
            margin=dict(l=20, r=20, t=40, b=20),
            width=800,  # можно настроить ширину
            height=400,  # и высоту графика
            xaxis=dict(tickmode='linear'),
            yaxis=dict(tickmode='linear')
        )
        return fig

    def create_multi_chart(dates, shop, game, box):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=shop, mode='lines+markers', name='Зашел в магазин'))
        fig.add_trace(go.Scatter(x=dates, y=game, mode='lines+markers', name='Зашел в гейм'))
        fig.add_trace(go.Scatter(x=dates, y=box, mode='lines+markers', name='Воспользовался боксом'))
        fig.update_layout(
            title='Сервисы',
            xaxis_title='Дата',
            yaxis_title='Количество',
            template='plotly_white',
            margin=dict(l=20, r=20, t=40, b=20),
            width=800,
            height=400,
            xaxis=dict(tickmode='linear'),
            yaxis=dict(tickmode='linear')
        )
        return fig

    def create_box_chart(dates, quest, offer, mood):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=quest, mode='lines+markers', name='Задал вопрос'))
        fig.add_trace(go.Scatter(x=dates, y=offer, mode='lines+markers', name='Предложил идею'))
        fig.add_trace(go.Scatter(x=dates, y=mood, mode='lines+markers', name='Отправил настроение'))
        fig.update_layout(
            title='Бокс ОС',
            xaxis_title='Дата',
            yaxis_title='Количество',
            template='plotly_white',
            margin=dict(l=20, r=20, t=40, b=20),
            width=800,
            height=400,
            xaxis=dict(tickmode='linear'),
            yaxis=dict(tickmode='linear')
        )
        return fig

    def create_orders_cancellations_chart(dates, order_counts, cancellation_counts):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=order_counts, mode='lines+markers', name='Сделал'))
        fig.add_trace(go.Scatter(x=dates, y=cancellation_counts, mode='lines+markers', name='Отменил'))
        fig.update_layout(
            title='Заказы',
            xaxis_title='Дата',
            yaxis_title='Количество',
            template='plotly_white',
            margin=dict(l=20, r=20, t=40, b=20),
            width=800,
            height=400,
            xaxis=dict(tickmode='linear'),
            yaxis=dict(tickmode='linear')
        )
        return fig

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

    # Отображение контента на странице
    put_column([
        put_row([
            None,
            put_text("Статистика").style("text-align: center; font-size: xx-large;"),
            put_button("     back      ", onclick=lambda: admin('admin', tab, fio, id), color='primary', outline=True).style('width:100%; height:100%; padding:0.5em;')
        ]).style('grid-template-columns: 0.1fr 1fr 0.1fr;'),

        None,

        put_row([
            put_html(chart.to_html(full_html=False)).style('width:100%'),
            put_html(chart2.to_html(full_html=False)).style('width:100%'),
        ]).style('display: flex; flex-direction: row; gap: 1em;'),

        None,

        put_row([
            put_html(chart3.to_html(full_html=False)).style('width:100%'),
            put_html(chart4.to_html(full_html=False)).style('width:100%'),
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
