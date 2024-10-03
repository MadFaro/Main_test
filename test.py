df_dict = pd.read_sql('SELECT name_case, name_directory FROM directory', connect("Convert/db/shop.db"))
