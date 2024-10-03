async def money_open(sdep, tab, product_id, fio, id, img_logo):
    try:
        close_popup()  # Закрываем возможное открытое popup окно
    except:
        pass

    # Получаем данные из базы
    df = pd.read_sql(sql.sql_operations_one_money.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))

    items = []  # Список элементов для вывода в popup

    # Собираем все case столбцы (от case1 до case13)
    case_columns = [f"case{i}" for i in range(1, 14)]

    # Проходим по каждому case столбцу и выводим те, которые заполнены
    for case in case_columns:
        case_value = df[case].iloc[0]
        if pd.notna(case_value):  # Если значение не NaN
            case_text = put_text(f"{case} - {case_value}")
            items.append(case_text)  # Добавляем текст в список items

    # Добавляем итоговое значение value_operation в items
    total_text = put_column([put_text(f'Всего начислено: {df["value_operation"][0]}')])
    items.append(total_text)

    # Показываем popup с начислениями и case
    popup(f'Начисление {product_id}', items)
