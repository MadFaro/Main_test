from pywebio.output import put_widget

# Определяем HTML шаблон
tpl = '''
<div class="product-inner">
  <div class="product-wrap">
    <img src="{{image_src}}">
    <div class="actions">
      <a href="{{add_to_cart_link}}" class="add-to-cart">Add to Cart</a>
      <a href="{{quickview_link}}" class="quickview">Quick View</a>
      <a href="{{wishlist_link}}" class="wishlist">Wishlist</a>
    </div>
  </div>
  <div class="product-info">
    <h3 class="product-title"><a href="{{product_link}}">{{product_title}}</a></h3>
    <span class="price">{{price}}</span>
  </div>
</div>
'''

# Передаем данные в шаблон
put_widget(tpl, {
    "image_src": "https://html5book.ru/wp-content/uploads/2015/10/black-dress.jpg",
    "add_to_cart_link": "#",  # Замените на реальную ссылку, если она доступна
    "quickview_link": "#",    # Замените на реальную ссылку, если она доступна
    "wishlist_link": "#",     # Замените на реальную ссылку, если она доступна
    "product_link": "#",      # Ссылка на продукт
    "product_title": "Маленькое черное платье",
    "price": "₽ 1999"
})


.product-inner {
   width: 300px;
   margin: 0 auto;
   background: white;
   text-align: center;
   border-bottom: 2px solid #ebebec;
   transition: .2s linear;
}
.product-inner:hover {
   border-color: #bca480;
}
.product-wrap {
   position: relative;
   overflow: hidden;
   margin-bottom: 15px;
}
.product-wrap img {
   display: block;
   width: 100%;
}
.actions {
   position: absolute;
   left: 0;
   bottom: -20%;
   width: 100%;
   background: rgba(59, 62, 67, 0.75);
   transition: .3s linear;
}
.product-inner:hover .actions {
   bottom: 0;
}
.actions a {
   text-decoration: none;
   float: left;
   width: 33.33333333333333%;
   color: white;
   padding: 15px 0;
   transition: .2s linear;
}
.actions a:hover {
   background: rgba(59, 62, 67, 0.85);
}
.actions a:before {
   font-family: "FontAwesome";
}
.add-to-cart:before {
   content: "\f07a";
}
.quickview:before {
   content: "\f002";
}
.wishlist:before {
   content: "\f08a";
}
.product-info {
   padding-bottom: 10px;
   font-family: 'Noto Sans', sans-serif;
}
.product-title {
   margin: 0 0 10px 0;
   font-family: 'Noto Sans', sans-serif;
}
.product-title a {
   text-decoration: none;
   color: #1e1e1e;
   font-weight: 400;
   font-size: 16px;
}
.price {
   font-weight: bold;
   color: #bca480;
}
