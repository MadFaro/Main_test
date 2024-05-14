df['holidays'] = df['datetime'].dt.date.isin(df_h.to_dict()).astype(int)
