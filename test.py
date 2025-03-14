def job():
    """Основная задача для выполнения каждые 5 минут."""
    start_task = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_timestamp = (datetime.now() - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')

    #для chatthreadid
    last_load = get_max_dtm_from_chat()
    rows = fetch_data_from_mariadb(last_load)
    if upsert_data_to_oracle(rows):
        update_last_load_timestamp(new_timestamp)

    #для chatthreadidhistory
    history_rows = fetch_history_data_from_mariadb(last_load)
    insert_history_data_to_oracle(history_rows)

    #для chatthreadmessage
    message_rows = fetch_message_data_from_mariadb(last_load)
    insert_message_data_to_oracle(message_rows)

    #для chatsl
    upsert_data_to_oracle_sl(rows)

    fetch_online_from_mariadb()
    fetch_config_from_mariadb()
    fetch_config_def_from_mariadb()

# Настройка расписания на каждые 5 минут
schedule.every(1).minutes.do(job)

# Основной цикл для выполнения задачи по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
