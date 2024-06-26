# Фильтрация строк, где дата больше максимальной даты из базы данных
filtered_df = df[df['DD'] > max_date]

print(f"Filtered data: {filtered_df}")
