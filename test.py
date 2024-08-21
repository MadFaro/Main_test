.centered-border::after {
    content: '';
    position: absolute;
    bottom: 0; /* Граница будет снизу */
    left: 50%; /* Начало границы в середине */
    transform: translateX(-50%); /* Смещаем начало границы влево на половину её длины, чтобы центрировать */
    width: 50%; /* Ширина границы — 50% от ширины элемента */
    border-bottom: 1px solid black; /* Собственно, сама граница */
}
