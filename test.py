from pywebio.output import put_html, put_row, put_button

# Основной текст
put_html("""
    <div style="text-align: center; font-size: x-large; white-space: pre-line;">
    Привет! Добро пожаловать на страницу Геймификации 2024.<br>
    Игра в стиле «Слово пацана» завершена и мы благодарим каждого, кто принял участие.<br>
    Увидимся в следующем году, друзья. А пока можете посмотреть результаты Гейма во вкладке 
    </div>
""")

# Встраиваемое слово "Итоги" как кликабельная кнопка в тексте
put_row([
    put_html('<div style="font-size: x-large; display: inline-block;">«</div>'),  # Открывающая кавычка
    put_button('Итоги', onclick=lambda: ..., link_style=True).style('font-size: x-large; display: inline-block;'),
    put_html('<div style="font-size: x-large; display: inline-block;">».</div>')  # Закрывающая кавычка и точка
], size="auto").style('text-align: center;')
