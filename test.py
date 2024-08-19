tpl = '''
<div class="product-wrap">
    <div class="product-item">
        {{& pywebio_output_parse}}  <!-- Вставка изображения -->
    </div>
    <div class="product-buttons">
        {{& pywebio_output_parse}}  <!-- Вставка кнопки -->
    </div>
    <div class="product-title">
        {{& pywebio_output_parse}}  <!-- Вставка названия продукта -->
        {{& pywebio_output_parse}}  <!-- Вставка цены продукта -->
    </div>
</div>
'''
