import pyodbc

# Настройка подключения к базе данных Oracle
connection_string = (
    "Driver={Oracle in OraClient12Home1};"  # Замените на ваш Oracle Driver
    "Dbq=your_db_tns;"                      # TNS alias или IP/порт/служба
    "Uid=your_username;"                    # Имя пользователя
    "Pwd=your_password;"                    # Пароль
)
try:
    # Установка соединения
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Запуск процедуры
    procedure_name = "имя_вашей_процедуры"  # Замените на имя вашей процедуры
    cursor.execute(f"BEGIN {procedure_name}(); END;")

    # Подтверждение изменений (если необходимо)
    conn.commit()

    print("Процедура выполнена успешно.")

except pyodbc.Error as e:
    print("Ошибка при выполнении процедуры:", e)

finally:
    # Закрытие соединения
    cursor.close()
    conn.close()

