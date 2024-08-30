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
