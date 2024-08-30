from pyg2plot import Line
from pyg2plot import options as opts

def create_login_chart(dates, login_counts):
    line = Line(init_opts=opts.InitOpts(theme='walden', width='100%', height='400px'))
    line.add_xaxis(dates)
    line.add_yaxis('Кол-во', login_counts, is_smooth=True)
    line.set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    line.set_global_opts(
        title_opts=opts.TitleOpts(title='Входы', pos_left='center'),
        tooltip_opts=opts.TooltipOpts(trigger='axis'),
        xaxis_opts=opts.AxisOpts(type_='category'),
        yaxis_opts=opts.AxisOpts(type_='value'),
        datazoom_opts=[
            opts.DataZoomOpts(type_='slider', range_start=80, range_end=100)
        ],
        legend_opts=opts.LegendOpts(is_show=True)
    )
    return line

def create_multi_chart(dates, shop, game, box):
    line = Line(init_opts=opts.InitOpts(theme='walden', width='100%', height='400px'))
    line.add_xaxis(dates)
    line.add_yaxis('Зашел в магазин', shop, is_smooth=True)
    line.add_yaxis('Зашел в гейм', game, is_smooth=True)
    line.add_yaxis('Воспользовался боксом', box, is_smooth=True)
    line.set_global_opts(
        title_opts=opts.TitleOpts(title='Сервисы', pos_left='center'),
        tooltip_opts=opts.TooltipOpts(trigger='axis'),
        xaxis_opts=opts.AxisOpts(type_='category'),
        yaxis_opts=opts.AxisOpts(type_='value'),
        datazoom_opts=[
            opts.DataZoomOpts(type_='slider', range_start=80, range_end=100)
        ],
        legend_opts=opts.LegendOpts(is_show=True)
    )
    return line

def create_box_chart(dates, quest, offer, mood):
    line = Line(init_opts=opts.InitOpts(theme='walden', width='100%', height='400px'))
    line.add_xaxis(dates)
    line.add_yaxis('Задал вопрос', quest, is_smooth=True)
    line.add_yaxis('Предложил идею', offer, is_smooth=True)
    line.add_yaxis('Отправил настроение', mood, is_smooth=True)
    line.set_global_opts(
        title_opts=opts.TitleOpts(title='Бокс ОС', pos_left='center'),
        tooltip_opts=opts.TooltipOpts(trigger='axis'),
        xaxis_opts=opts.AxisOpts(type_='category'),
        yaxis_opts=opts.AxisOpts(type_='value'),
        datazoom_opts=[
            opts.DataZoomOpts(type_='slider', range_start=80, range_end=100)
        ],
        legend_opts=opts.LegendOpts(is_show=True)
    )
    return line

def create_orders_cancellations_chart(dates, order_counts, cancellation_counts):
    line = Line(init_opts=opts.InitOpts(theme='walden', width='100%', height='400px'))
    line.add_xaxis(dates)
    line.add_yaxis('Сделал', order_counts, is_smooth=True)
    line.add_yaxis('Отменил', cancellation_counts, is_smooth=True)
    line.set_global_opts(
        title_opts=opts.TitleOpts(title='Заказы', pos_left='center'),
        tooltip_opts=opts.TooltipOpts(trigger='axis'),
        xaxis_opts=opts.AxisOpts(type_='category'),
        yaxis_opts=opts.AxisOpts(type_='value'),
        datazoom_opts=[
            opts.DataZoomOpts(type_='slider', range_start=80, range_end=100)
        ],
        legend_opts=opts.LegendOpts(is_show=True)
    )
    return line
