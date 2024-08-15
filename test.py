copy_button_html = '''
<button onclick="copyTextToClipboard()" style="background-color: transparent; color: orange; border: 2px solid orange; padding: 20px 20px 10px 20px; font-size: 16px; cursor: pointer; text-align: center; border-radius: 5px; position: relative; overflow: visible;">
    <div style="font-size: 24px; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); transition: top 0.3s ease;">
        ☎️
    </div>
    9 999 999 99 99
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
    });
    button.addEventListener('mouseout', function() {
        this.querySelector('div').style.top = '-20px';  // Возвращаем иконку в исходное положение
    });
</script>
'''
