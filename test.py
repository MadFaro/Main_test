/* Подсветка верхнего левого угла */
.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 50px; /* ширина подсветки */
  height: 50px; /* высота подсветки */
  background: linear-gradient(to bottom right, rgba(255, 255, 0, 0.5), transparent);
}

/* Подсветка нижнего правого угла */
.card::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50px; /* ширина подсветки */
  height: 50px; /* высота подсветки */
  background: linear-gradient(to top left, rgba(255, 255, 0, 0.5), transparent);
}
