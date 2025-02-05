# Объединяем все отдельные DataFrame в один
final_df = pd.concat(expanded_rows, ignore_index=True)

# Переупорядочиваем столбцы
final_df = final_df[['id', 'date', 'type', 'login', 'product_id', 'name', 'count', 'subtotal_price', 'size', 'color']]

# Преобразуем все числовые столбцы в типы Python
final_df['id'] = final_df['id'].astype(int)
final_df['product_id'] = final_df['product_id'].astype(int)
final_df['count'] = final_df['count'].astype(int)
final_df['subtotal_price'] = final_df['subtotal_price'].astype(float)
