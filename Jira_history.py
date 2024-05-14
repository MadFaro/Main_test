df_h['TRUNC(CLD_DAY_DT)'] = df_h['TRUNC(CLD_DAY_DT)'].apply(lambda x: x.date())
