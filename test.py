async def money_open(sdep, tab, product_id, fio, id, img_logo):
    try:
        close_popup()
    except:
        pass
    
    img_ban = open('img/money_temp_img.png', 'rb').read()
    df = pd.read_sql(sql.sql_operations_one_money.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))
    df_dict = pd.read_sql('SELECT name_case, name_directory FROM directory', connect("Convert/db/shop.db"))
    case_dict = dict(zip(df_dict['name_case'], df_dict['name_directory']))
    
    table_data = []
    case_columns = [f"case{i}" for i in range(1, 14)]

    for case in case_columns:
        case_value = df[case].iloc[0]
        if pd.notna(case_value):
            case_description = case_dict.get(case, case) 
            table_data.append([case_value, case_description])

    # Добавляем заголовки только если есть данные в таблице
    if table_data:  # Проверяем, есть ли данные в таблице
        table_data.insert(0, ['Начислено', 'Позиция'])  # Вставляем заголовки в начало

    # Создаем таблицу и применяем стили
    table_output = put_table(table_data).style("border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;")

    # Отображаем popup с изображением и таблицей
    popup(f'Начисление {product_id}', [put_image(img_ban, width='auto', height='auto').style('place-self: center;'), put_html("<BR>"), table_output], size="large")
