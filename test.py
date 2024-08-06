tpl = '''
<div class="product-inner">
  <div class="product-wrap">
    <img src="{{image_data_url}}" alt="Product Image">
    <div class="actions">
      {{& add_to_cart_button}}
    </div>
  </div>
  <div class="product-info">
    <h3 class="product-title"><a href="{{product_link}}">{{product_title}}</a></h3>
    <span class="price">{{price}}</span>
  </div>
</div>
'''
