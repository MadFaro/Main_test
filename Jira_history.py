df_select[date_columns] = df_select[date_columns].apply(pd.to_datetime, errors='coerce', dayfirst=True)
df_select[numeric_columns] = df_select[numeric_columns].apply(pd.to_numeric, errors='coerce')
