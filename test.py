def create_top_5_products_pie_chart(products, sales):
    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # Выбор темы, можно заменить на ThemeType.DARK
        .add(
            series_name="Sales",
            data_pair=[(product, sale) for product, sale in zip(products, sales)],
            radius=["40%", "75%"],  # Размеры кругов
            label_opts=opts.LabelOpts(formatter="{b}: {d}%")  # Форматирование меток
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Top 5 Most Sold Products",
                title_textstyle_opts=opts.TextStyleOpts(color="#000000")  # Цвет заголовка
            ),
            legend_opts=opts.LegendOpts(is_show=True, textstyle_opts=opts.TextStyleOpts(color="#000000"))  # Цвет легенды
        )
    )
    return pie
