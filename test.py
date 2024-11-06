    conn = cx_Oracle.connect(user='', password='', dsn = '')
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute("select * from STAGE_UNC.EFS_STAFF@cvm.prod where TUB_NUM = :myField", {"myField":str(row['Логин']).upper()})
        select_true = cursor.fetchall()
        if pd.DataFrame(select_true).empty:
            count += 1
            cursor.execute("INSERT INTO STAGE_UNC.EFS_STAFF@cvm.prod (FULL_NAME, LOGIN, TUB_NUM, DATE_INSERT) VALUES (:1, :2, :3, :4)",
                            (str(row['Фамилия Имя Отчество']).upper(), str(row['Логин']).upper(), row['Табельный номер'], date)
                            )
            cursor.execute("INSERT INTO STAGE_UNC.DICT_NPS_OPERATOR@cvm.prod (STAFF_ID, OPERATOR_NAME, DATE_INSERT) VALUES (:1, :2, :3)",
                                (str(row['Логин']).upper(), str(row['CISCO']).upper(), date)
                                )
