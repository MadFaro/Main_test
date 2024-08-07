def create_orders_cancellations_chart(dates, order_counts, cancellation_counts):
    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis("Orders", order_counts, is_smooth=True)
        .add_yaxis("Cancellations", cancellation_counts, is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Orders and Cancellations Over Time"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(type_="value"),
            datazoom_opts=[
                opts.DataZoomOpts(type_="slider"),  # Добавление элемента зума
                opts.DataZoomOpts(type_="inside")  # Внутренний зум для скролла
            ],
            legend_opts=opts.LegendOpts(is_show=True)  # Отображение легенды
        )
    )
    return line
dates = df['date'].tolist()
    order_counts = df['cnt_orders'].tolist()
    cancellation_counts = df['cnt_cancellations'].tolist()
    
    # Создание графика
    chart = create_orders_cancellations_chart(dates, order_counts, cancellation_counts)
    
