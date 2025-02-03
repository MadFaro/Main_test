with open('predictions_chat.txt', 'w', encoding='utf-8') as f:
    f.write("DATE_TIME_FORMAT\nDD.MM.YYYY HH:mm\n")
    f.write("Имя очереди\tДата\tВремя\tИнтервал времени\tОбъём\tСВО (Секунды)\n")
    
    for index, row in X_pred.iterrows():
        adjusted_datetime = row['datetime'] + timedelta(hours=2)
        date_str = adjusted_datetime.strftime('%d.%m.%Y')
        time_str = adjusted_datetime.strftime('%H:%M')
        interval = '00:30'
        queue_name = 'чат банк'
        volume = int(row['predictions'])
        
        day_of_week = row['day_of_week']
        if day_of_week < 5:
            svo = SVO_BUD
        else:
            svo = SVO_VIX
        
        f.write(f"{queue_name}\t{date_str}\t{time_str}\t{interval}\t{volume}\t{svo}\n")
