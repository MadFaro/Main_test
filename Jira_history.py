next_days = pd.date_range(start=(df['datetime'].max()+pd.Timedelta(hours=1)), periods=62*24, freq='1H')
