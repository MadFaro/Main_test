# Добавляем вывод в txt формате с интервалом 30 минут и кодировкой UTF-8
with open('predictions.txt', 'w', encoding='utf-8') as f:
    # Добавляем формат даты/времени в начало файла
    f.write("DATE_TIME_FORMAT\nDD.MM.YYYY HH:mm\n")
    
    # Пишем заголовок таблицы
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tОбъём\tСВО (Секунды)\n")
    
    for index, row in X_pred.iterrows():
        # Форматируем дату и время
        date_str = row['datetime'].strftime('%d.%m.%Y')
        time_str = row['datetime'].strftime('%H:%M')
        interval = '00:30'  # Интервал 30 минут
        queue_name = 'SG_Operator'
        volume = int(row['predictions'])  # Округляем предсказанные значения модели до целого числа
        svo = 300  # Фиксированное значение СВО
        
        # Записываем строку в файл
        f.write(f"{queue_name}\t{date_str}\t{time_str}\t{interval}\t{volume}\t{svo}\n")

