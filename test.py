import base64
 with open(path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

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

/* Стили для контейнера изображения продукта */
.product-wrap {
   position: relative;
   overflow: hidden;
   margin-bottom: 15px;
}

.product-wrap img {
   display: block;
   width: 100%;
}

/* Стили для действий над продуктом */
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
   font-style: normal;
   font-weight: normal;
   text-decoration: inherit;
   margin-right: 5px;
}

/* Иконки FontAwesome для кнопок */
.add-to-cart:before {
   content: "\f07a"; /* Иконка корзины */
}

.quickview:before {
   content: "\f002"; /* Иконка поиска */
}

.wishlist:before {
   content: "\f08a"; /* Иконка списка желаний */
}

/* Стили для информации о продукте */
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
