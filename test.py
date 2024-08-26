def get_correct_word_form(points):
    last_digit = points % 10
    last_two_digits = points % 100

    if last_digit == 1 and last_two_digits != 11:
        return f"{points} балл"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return f"{points} балла"
    else:
        return f"{points} баллов"

# Примеры использования
print(get_correct_word_form(552))  # 552 балла
print(get_correct_word_form(650))  # 650 баллов
print(get_correct_word_form(1))    # 1 балл
print(get_correct_word_form(21))   # 21 балл

