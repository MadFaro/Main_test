put_html("""
    <div style="text-align: center; font-size: x-large; white-space: pre-line;">
    Привет! Добро пожаловать на страницу Геймификации 2024.<br>
    Игра в стиле «Слово пацана» завершена и мы благодарим каждого, кто принял участие.<br>
    Увидимся в следующем году, друзья. А пока можете посмотреть результаты Гейма во вкладке «
    </div>
""")

# Кнопка "Итоги" встроенная в текст
put_button('Итоги', onclick=lambda: ..., link_style=True).style('font-size: x-large; display: inline;')

# Завершающий текст с закрывающей кавычкой
put_html("""
    <div style="text-align: center; font-size: x-large; display: inline;">».</div>
""")
