def fetch_online_from_mariadb():
    """Извлекаем данные из MariaDB с учётом метки времени."""
    try:
        data_type = {
            'OPERATORID': Integer
        }
        mariadb_conn = mysql.connector.connect(**mariadb_config)
        query = """
        select distinct OPERATORID from webim_hosted_meta.operatordevice
        where devicestatus = 'online' and (dtmcreated>= date(now()) or dtmmodified>= date(now()));
        """
        df = pd.read_sql(query, mariadb_conn)
        oracle_conn = cx_Oracle.connect(user='Reports_msk', password='Reports!', dsn = 'msk-as03math.fc.uralsibbank.ru/space.prod.msk.usb')
        cursor = oracle_conn.cursor()
        cursor.execute("truncate table ANALYTICS.TOLOG_BI_OPERONLINE")
        oracle_conn.commit()
        oracle_conn.close()
        connect_str = lambda: cx_Oracle.connect(user='Reports_msk', password='Reports!', dsn = 'msk-as03math.fc.uralsibbank.ru/space.prod.msk.usb')
        connect = create_engine("oracle://", creator=connect_str)
        df.to_sql('TOLOG_BI_OPERONLINE', connect, if_exists='append', schema='analytics', index=False, dtype=data_type)
    except:
        pass
