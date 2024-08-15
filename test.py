copy_button_html = '''
<button onclick="copyTextToClipboard()" style="background-color: orange; color: white; border: none; padding: 10px 20px; font-size: 16px; cursor: pointer; text-align: center;">
    <div style="font-size: 24px;">☎️</div>
    Копировать
</button>
<script>
    function copyTextToClipboard() {
        var text = "Пример текста";
        navigator.clipboard.writeText(text).then(function() {
            alert("Текст скопирован: " + text);
        }, function(err) {
            alert("Ошибка копирования: " + err);
        });
    }
</script>
'''
