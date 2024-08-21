    border-bottom: 1px solid black;
    transition: width 0.3s ease-in-out, left 0.3s ease-in-out; /* Анимация изменения ширины и позиции */
}

.centered-border:hover::after {
    width: 100%;  /* Граница расширяется до полной ширины */
    left: 0; /* Начало границы смещается влево, чтобы занять всю ширину */
    transform: translateX(0); /* Убираем смещение */
}
