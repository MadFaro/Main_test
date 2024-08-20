put_html("""
    <style>
        #scroll-button {
            display: none; /* Изначально кнопка скрыта */
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 100;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    
    <button id="scroll-button" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">Наверх</button>

    <script>
        window.onscroll = function() {
            var button = document.getElementById('scroll-button');
            if (document.documentElement.scrollTop > 100) {
                button.style.display = 'block'; // Показать кнопку, если прокручено более чем на 100px
            } else {
                button.style.display = 'none'; // Скрыть кнопку, если прокрутка меньше 100px
            }
        };
    </script>
    """)
