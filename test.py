copy_button_html = '''
<button onclick="copyTextToClipboard()" style="background-color: transparent; color: orange; border: 2px solid orange; padding: 20px 20px 10px 20px; font-size: 16px; cursor: pointer; text-align: center; border-radius: 5px; position: relative; overflow: visible; transition: all 0.3s ease;">
    <div style="font-size: 24px; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); transition: all 0.3s ease;">
        ☎️
    </div>
    <span style="display: block;">9 999 999 99 99</span>
</button>
<script>
    function copyTextToClipboard() {
        var text = "9 999 999 99 99";
        navigator.clipboard.writeText(text).then(function() {
            alert("Текст скопирован: " + text);
        }, function(err) {
            alert("Ошибка копирования: " + err);
        });
    }

    // Добавление эффекта при наведении на кнопку
    const button = document.querySelector('button');
    button.addEventListener('mouseover', function() {
        this.querySelector('div').style.top = '-30px';  // Поднимаем иконку при наведении
        this.style.backgroundColor = 'rgba(255, 165, 0, 0.1)';  // Легкий фон при наведении
        this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';  // Тень при наведении
    });
    button.addEventListener('mouseout', function() {
        this.querySelector('div').style.top = '-20px';  // Возвращаем иконку в исходное положение
        this.style.backgroundColor = 'transparent';  // Убираем фон при наведении
        this.style.boxShadow = 'none';  // Убираем тень при наведении
    });
</script>
'''
