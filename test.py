def json_to_html(json_data):
    # Если json_data - это список словарей
    if isinstance(json_data, list):
        df = pd.DataFrame(json_data)
    else:
        raise ValueError("JSON data is not in the expected format")
    
    # Преобразование DataFrame в HTML
    return df.to_html(index=False, escape=False)
