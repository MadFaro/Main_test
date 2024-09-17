# Добавляем вывод в txt формате с интервалом 30 минут
with open('predictions.txt', 'w') as f:
    # Пишем заголовок
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tОбъём\tСВО (Секунды)\n")
    
    for index, row in X_pred.iterrows():
        # Форматируем дату и время
        date_str = row['datetime'].strftime('%d.%m.%Y')
        time_str = row['datetime'].strftime('%H:%M')
        interval = '00:30'  # Изменен интервал на 30 минут
        queue_name = 'SG_Operator'
        volume = int(row['predictions'])  # Объем — это предсказанные значения модели
        svo = 300  # Фиксированное значение СВО
        
        # Записываем строку в файл
        f.write(f"{queue_name}\t{date_str}\t{time_str}\t{interval}\t{volume}\t{svo}\n")
