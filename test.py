def create_login_chart(dates, login_counts):
    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis("Logins", login_counts, is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Logins Over Time"),
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
