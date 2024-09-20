from datetime import datetime, timedelta

# Путь к вашему файлу
input_file = 'data.txt'
output_file = 'data_ufa.txt'

# Часовая разница между МСК и Уфой
time_difference = timedelta(hours=2)

# Чтение данных из файла
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Открытие нового файла для записи
with open(output_file, 'w', encoding='utf-8') as new_file:
    for line in lines:
        # Если строка содержит данные, а не заголовок
        if line.startswith('SG_Operator'):
            parts = line.split('\t')
            date_str = parts[1]
            time_str = parts[2]

            # Объединение даты и времени для создания объекта datetime
            datetime_str = f"{date_str} {time_str}"
            current_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')

            # Добавляем 2 часа для Уфы
            new_datetime = current_datetime + time_difference

            # Разделяем новую дату и время
            new_date_str = new_datetime.strftime('%d.%m.%Y')
            new_time_str = new_datetime.strftime('%H:%M')

            # Собираем строку с обновленным временем
            new_line = f"{parts[0]}\t{new_date_str}\t{new_time_str}\t{parts[3]}\t{parts[4]}\t{parts[5]}"
            new_file.write(new_line)
        else:
            # Записываем строку без изменений (например, заголовки)
            new_file.write(line)

print("Время успешно изменено на Уфу и записано в новый файл.")
