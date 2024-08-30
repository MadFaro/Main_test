from pywebio import start_server
from pywebio.output import put_html, put_button

def main():
    put_html('<h2>Создание нового письма в Outlook</h2>')
    
    def open_outlook_mail():
        # Создаем ссылку с URI-схемой outlook
        outlook_link = "outlook:newMessage?to=recipient@example.com&subject=Привет&body=Это тестовое письмо"
        put_html(f'<a href="{outlook_link}" id="outlook-link" style="display:none;">Open Outlook Mail</a>')
        put_html('''<script>
            document.getElementById('outlook-link').click();
        </script>''')
    
    put_button("Открыть новое письмо в Outlook", onclick=open_outlook_mail)

if __name__ == '__main__':
    start_server(main, port=8080)
