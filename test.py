df = pd.read_sql("SELECT id, json FROM operations", conn)

# Функция для извлечения данных из JSON
def extract_products(json_str):
    try:
        products = json.loads(json_str)
        return [(prod.get("product_id"), prod.get("count")) for prod in products]
    except json.JSONDecodeError:
        return []

# Извлечение и обработка данных
product_data = df['json'].apply(extract_products)

# Преобразование списка продуктов в DataFrame
product_rows = []
for idx, products in enumerate(product_data):
    for product_id, count in products:
        product_rows.append((df.iloc[idx]['id'], product_id, count))

product_df = pd.DataFrame(product_rows, columns=['id', 'product_id', 'count'])

# Группировка данных и выбор топ 5 продуктов
top_products = product_df.groupby('product_id')['count'].sum().nlargest(5)
