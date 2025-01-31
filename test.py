# Перебираем все строки
for i, row in data.iterrows():
    # Извлекаем дату для текущей строки
    date = dates.iloc[i, 0].strftime("%d.%m.%Y")  # Форматируем дату в нужный формат (DD.MM.YYYY)
    
    # Преобразуем все значения в строках (если они числа)
    values = row.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int).values  # Все значения в целые числа
    
    # Перебираем данные по часам, начиная с 7:00 (индекс 0 в данных = 7:00)
    for hour in range(7, 24):  # Начинаем с 7:00
        time = f"{hour:02d}:00"
        value = values[hour - 7]  # Получаем значение для текущего часа (сдвиг на 7)
        rows.append(["WEBIM_Chat", date, time, "01:00", value])  # Формируем строку для записи
