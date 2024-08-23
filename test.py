/* Подсветка границы верхнего левого угла */
.card::before {
  content: '';
  position: absolute;
  top: -1px;
  left: -1px;
  width: 50px; /* ширина границы */
  height: 50px; /* высота границы */
  border-top: 3px solid transparent;
  border-left: 3px solid transparent;
  background: linear-gradient(to bottom right, #8a2be2, transparent);
}

/* Подсветка границы нижнего правого угла */
.card::after {
  content: '';
  position: absolute;
  bottom: -1px;
  right: -1px;
  width: 50px; /* ширина границы */
  height: 50px; /* высота границы */
  border-bottom: 3px solid transparent;
  border-right: 3px solid transparent;
  background: linear-gradient(to top left, #8a2be2, transparent);
}
