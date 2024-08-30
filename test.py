df = pd.read_sql(sql.sql_operations_one.replace('Замена', str(product_id)), connect("Convert/db/shop.db"))
    # Загружаем данные о корзине из JSON
    json_data = json.loads(df['json'].iloc[0]) 
    
    items = [] 
    total_price = 0
    html_json = pd.read_json(json_data).to_html(index=False)
