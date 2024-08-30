from pywebio import start_server
from pywebio.output import put_html, put_button
from pywebio.input import input

def main():
    put_html('<h2>Создание нового письма в Outlook</h2>')
    
    def open_mail():
        # Создайте ссылку mailto с предустановленными полями (тема, текст и т.д.)
        mailto_link = "mailto:recipient@example.com?subject=Привет&body=Это тестовое письмо"
        put_html(f'<a href="{mailto_link}" id="mail-link" style="display:none;">Open Mail</a>')
        put_html('''<script>
            document.getElementById('mail-link').click();
        </script>''')
    
    put_button("Открыть новое письмо", onclick=open_mail)

if __name__ == '__main__':
    start_server(main, port=8080)
