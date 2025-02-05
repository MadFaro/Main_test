# Преобразуем столбцы с типами numpy.int32 или numpy.int64 в стандартный int
final_df['ID'] = final_df['ID'].apply(int)
final_df['product_id'] = final_df['product_id'].apply(int)
final_df['count'] = final_df['count'].apply(int)
final_df['subtotal_price'] = final_df['subtotal_price'].apply(float)
