<button onclick="copyTextToClipboard2()" 
    style="background-color: transparent; color: #ff8484; border: 2px solid #ff8484; font-family: system-ui; padding: 20px 20px 10px 20px; font-size: 16px; cursor: pointer; text-align: center; border-radius: 5px; position: relative; overflow: visible; transition: all 0.3s ease;">
    <div class="icon" 
        style="font-size: 24px; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); transition: all 0.3s ease;">
        ☎️
    </div>
    <span style="display: block;">         8 937 304 40 32         </span>
</button>

<script>
    function copyTextToClipboard2() {
        var text = "8 937 304 40 32";
        navigator.clipboard.writeText(text).then(function() {
            alert("Текст скопирован: " + text);
        }, function(err) {
            alert("Ошибка копирования: " + err);
        });
    };
</script>

<style>
    button:hover {
        background-color: #ff8484;
        color: white;
    }

    button:hover .icon {
        transform: translateX(-50%) scale(1.2);
    }

    button:active {
        background-color: #cc6b6b;
        border-color: #cc6b6b;
        color: white;
    }

    button:active .icon {
        transform: translateX(-50%) scale(1);
    }
</style>
