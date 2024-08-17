tpl = '''
<div class="star-rating">
    {{#stars}}
    <input type="radio" id="{{id}}" name="rating" value="{{value}}" onchange="sendRating('{{value}}')">
    <label for="{{id}}">★</label>
    {{/stars}}
</div>

<script>
    function sendRating(value) {
        WebIO.pushData(value);  // Отправляем выбранное значение в Python
    }
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
