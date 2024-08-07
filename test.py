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
        )
    )
    return line

    dates = df['date'].tolist()
    login_counts = df['cnt'].tolist()
