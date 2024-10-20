from datetime import timedelta

with open('predictions.txt', 'w', encoding='utf-8') as f:
    # Добавляем формат даты/времени в начало файла
    f.write("DATE_TIME_FORMAT\nDD.MM.YYYY HH:mm\n")
    
    # Пишем заголовок таблицы
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tОбъём\tСВО (Секунды)\n")
    
    for index, row in X_pred.iterrows():
        # Сдвигаем время на 2 часа вперед
        adjusted_datetime = row['datetime'] + timedelta(hours=2)
        
        # Форматируем дату и время с учетом сдвига
        date_str = adjusted_datetime.strftime('%d.%m.%Y')
        time_str = adjusted_datetime.strftime('%H:%M')
        interval = '00:30'  # Интервал 30 минут
        queue_name = 'SG_Operator'
        volume = int(row['predictions'])  # Округляем предсказанные значения модели до целого числа
        
        # Определяем SVO в зависимости от дня недели (0 = Понедельник, 6 = Воскресенье)
        day_of_week = row['day_of_week']
        if day_of_week < 5:  # Будние дни (Понедельник - Пятница)
            svo = SVO_BUD
        else:  # Выходные дни (Суббота - Воскресенье)
            svo = SVO_VIX
        
        # Записываем строку в файл
        f.write(f"{queue_name}\t{date_str}\t{time_str}\t{interval}\t{volume}\t{svo}\n")

