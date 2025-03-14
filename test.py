import time
import schedule
from datetime import datetime, timedelta

def job():
    """Основная задача для выполнения каждые 5 минут с повтором в случае ошибки."""
    while True:  # Бесконечный цикл для повторов при ошибке
        try:
            start_task = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_timestamp = (datetime.now() - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')

            # Для chatthreadid
            last_load = get_max_dtm_from_chat()
            rows = fetch_data_from_mariadb(last_load)
            if upsert_data_to_oracle(rows):
                update_last_load_timestamp(new_timestamp)

            # Для chatthreadidhistory
            history_rows = fetch_history_data_from_mariadb(last_load)
            insert_history_data_to_oracle(history_rows)

            # Для chatthreadmessage
            message_rows = fetch_message_data_from_mariadb(last_load)
            insert_message_data_to_oracle(message_rows)

            # Для chatsl
            upsert_data_to_oracle_sl(rows)

            fetch_online_from_mariadb()
            fetch_config_from_mariadb()
            fetch_config_def_from_mariadb()

            break  # Если всё прошло успешно, выходим из цикла
        except Exception as e:
            print(f"Ошибка: {e}. Повтор через 10 секунд...")
            time.sleep(10)  # Ждём перед повторной попыткой

# Настройка расписания на каждые 5 минут
schedule.every(5).minutes.do(job)  # Здесь было 1 минута, но, судя по названию, нужно 5

# Основной цикл для выполнения задачи по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
