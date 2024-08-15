copy_button_html = '''
<button onclick="copyTextToClipboard()">Копировать</button>
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
