    if datetime.now() + timedelta(hours=3) > dt + timedelta(minutes=15):
        return 'Код истёк. Запросите новый.'
