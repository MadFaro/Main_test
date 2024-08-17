from pywebio.output import put_widget, put_markdown, put_table
from pywebio.session import run_js

# HTML шаблон для звездного рейтинга с использованием Mustache-синтаксиса
tpl = '''
<div class="star-rating">
    {{#stars}}
    <input type="radio" id="{{id}}" name="rating" value="{{value}}">
    <label for="{{id}}">★</label>
    {{/stars}}
</div>

<script>
    document.querySelectorAll('.star-rating input').forEach(function(input) {
        input.addEventListener('change', function() {
            WebIO.pushData(this.value);
        });
    });
</script>

<style>
    .star-rating {
        font-size: 0;
        direction: rtl;
        display: inline-block;
        position: relative;
        cursor: pointer;
    }
    .star-rating input[type="radio"] {
        display: none;
    }
    .star-rating label {
        font-size: 2rem;
        color: #ddd;
        padding: 0 0.1rem;
        transition: all 0.3s;
    }
    .star-rating input[type="radio"]:checked ~ label {
        color: orange;
    }
    .star-rating label:hover,
    .star-rating label:hover ~ label {
        color: orange;
    }
</style>
'''

# Данные для виджета
data = {
    "stars": [
        {"id": "5-stars", "value": "5"},
        {"id": "4-stars", "value": "4"},
        {"id": "3-stars", "value": "3"},
        {"id": "2-stars", "value": "2"},
        {"id": "1-star", "value": "1"}
    ]
}

# Отображение виджета
put_widget(tpl, data)

# Получение результата выбранного рейтинга
rating = run_js('await WebIO.waitForData()')

# Отображение результата
put_markdown(f'Вы выбрали рейтинг: **{rating}** звезд')

