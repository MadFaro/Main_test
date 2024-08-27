    <button onclick="copyTextToClipboard()" style="background-color: transparent; color: #ff8484; border: 2px solid #ff8484; font-family: system-ui; padding: 20px 20px 10px 20px; font-size: 16px; cursor: pointer; text-align: center; border-radius: 5px; position: relative; overflow: visible; transition: all 0.3s ease;">
        <div style="font-size: 24px; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); transition: all 0.3s ease;">
            📧
        </div>
        <span style="display: block;">KalimullinAI@ufa.uralsib.ru</span>
    </button>
    <script>
        function copyTextToClipboard() {
            var text = "KalimullinAI@ufa.uralsib.ru";
            navigator.clipboard.writeText(text).then(function() {
                alert("Текст скопирован: " + text);
            }, function(err) {
                alert("Ошибка копирования: " + err);
            });
        }
    </script>
