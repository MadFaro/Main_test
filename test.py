chart = create_login_chart(dates, login_counts)
    
    # Отображение графика в веб-интерфейсе
    put_html(chart.render_notebook())
