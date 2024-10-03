async def money_open(sdep, tab, product_id, fio, id, img_logo):
    try:
        close_popup()  # Закрываем возможное открытое popup окно
    except:
        pass
    
    img_ban = open('img/money_temp_img.png', 'rb').read()
    
    # Запрашиваем данные из базы данных
    df = pd.read_sql(sql.sql_operations_one_money.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))
    df_dict = pd.read_sql('SELECT name_case, name_directory FROM directory', connect("Convert/db/shop.db"))
    
    # Создаем словарь для удобного доступа
    case_dict = dict(zip(df_dict['name_case'], df_dict['name_directory']))
    
    table_data = []  # Инициализируем пустой список для данных таблицы
    case_columns = [f"case{i}" for i in range(1, 14)]

    # Заполняем данные из кейсов
    for case in case_columns:
        case_value = df[case].iloc[0]  # Получаем значение case
        if pd.notna(case_value):  # Проверяем, что значение не NaN
            case_description = case_dict.get(case, case)  # Получаем расшифровку
            table_data.append([case_value, case_description])  # Добавляем в список

    # Добавляем заголовки только если есть данные в таблице
    if table_data:  # Проверяем, есть ли данные в таблице
        table_data.insert(0, ['Начислено', 'Позиция'])  # Вставляем заголовки в начало
    else:
        print("Нет данных для отображения в таблице.")  # Отладочная информация

    # Проверка на случай, если table_data пустое
    if not table_data:
        # Обработка случая, когда нет данных
        table_output = put_html("<p>Нет данных для отображения.</p>")
    else:
        # Создаем таблицу и применяем стили
        table_output = put_table(table_data).style("border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;")

    # Отображаем popup с изображением и таблицей
    popup(f'Начисление {product_id}', 
          [put_image(img_ban, width='auto', height='auto').style('place-self: center;'), put_html("<BR>"), table_output], 
          size="large")
