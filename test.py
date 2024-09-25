put_html("""
    <div style="text-align: center; font-size: x-large;">
    Привет! Добро пожаловать на страницу Геймификации 2024.<br>
    Игра в стиле «Слово пацана» завершена и мы благодарим каждого, кто принял участие.<br>
    Увидимся в следующем году, друзья. А пока можете посмотреть результаты Гейма во вкладке 
    </div>
""")

put_row([
    span("", width='auto'),
    put_button("Итоги", onclick=lambda: ..., link_style=True),
    span(".", width='auto')
], size="auto").style("text-align: center; font-size: x-large;")
