conn = cx_Oracle.connect(user='', password='', dsn='')
cursor = conn.cursor()

for index, row in df.iterrows():
    login = str(row['Логин']).upper()
    tub_num_df = row['Табельный номер']
    
    # Выполнение запроса для проверки существования записи по логину
    cursor.execute("SELECT LOGIN, TUB_NUM FROM STAGE_UNC.EFS_STAFF@cvm.prod WHERE login = :myField", {"myField": login})
    select_result = cursor.fetchall()
    
    if not select_result:
        # Если запись отсутствует, выполняем вставку
        count += 1
        cursor.execute("INSERT INTO STAGE_UNC.EFS_STAFF@cvm.prod (FULL_NAME, LOGIN, TUB_NUM, DATE_INSERT) VALUES (:1, :2, :3, :4)",
                       (str(row['Фамилия Имя Отчество']).upper(), login, tub_num_df, date))
        cursor.execute("INSERT INTO STAGE_UNC.DICT_NPS_OPERATOR@cvm.prod (STAFF_ID, OPERATOR_NAME, DATE_INSERT) VALUES (:1, :2, :3)",
                       (login, str(row['CISCO']).upper(), date))
    else:
        # Если запись существует, проверяем табельный номер
        existing_tub_num = select_result[0][1]
        
        if existing_tub_num != tub_num_df:
            # Если табельный номер не соответствует, удаляем записи и добавляем их заново
            cursor.execute("DELETE FROM STAGE_UNC.EFS_STAFF@cvm.prod WHERE login = :myField", {"myField": login})
            cursor.execute("DELETE FROM STAGE_UNC.DICT_NPS_OPERATOR@cvm.prod WHERE STAFF_ID = :myField", {"myField": login})
            
            count += 1
            cursor.execute("INSERT INTO STAGE_UNC.EFS_STAFF@cvm.prod (FULL_NAME, LOGIN, TUB_NUM, DATE_INSERT) VALUES (:1, :2, :3, :4)",
                           (str(row['Фамилия Имя Отчество']).upper(), login, tub_num_df, date))
            cursor.execute("INSERT INTO STAGE_UNC.DICT_NPS_OPERATOR@cvm.prod (STAFF_ID, OPERATOR_NAME, DATE_INSERT) VALUES (:1, :2, :3)",
                           (login, str(row['CISCO']).upper(), date))

# Закрытие курсора и соединения
cursor.close()
conn.commit()
conn.close()
