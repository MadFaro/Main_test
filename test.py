from pywebio import start_server
from pywebio.output import put_button, put_html

def main():
    # Используем JavaScript прямо в параметре onclick
    put_button("Открыть новое письмо", onclick=lambda: put_html('''
        <script>
            // Создаем ссылку mailto с предустановленными полями
            var mailtoLink = "mailto:recipient@example.com?subject=Привет&body=Это тестовое письмо";
            // Создаем временный элемент для клика
            var link = document.createElement("a");
            link.href = mailtoLink;
            link.style.display = "none"; // Скрыть элемент
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        </script>
    '''))

if __name__ == '__main__':
    start_server(main, port=8080)
