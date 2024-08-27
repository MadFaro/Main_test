import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle

# Функция для получения последних версий из базы данных
def fetch_latest_versions():
    conn = ""  # Укажите ваши параметры подключения к базе данных
    cursor = conn.cursor()
    cursor.execute("SELECT PLATFORM,VERSION FROM ANALYTICS.TOLOG_TEST1 WHERE PLATFORM IN ('ANDROID', 'IOS') AND APP_ACT = 1")
    result = cursor.fetchall()
    conn.close()

    last_app_android = "N/A"
    last_app_ios = "N/A"

    for row in result:
        if row[0] == 'ANDROID':
            last_app_android = row[1]
        elif row[0] == 'IOS':
            last_app_ios = row[1]

    return last_app_android, last_app_ios

# Функция для обновления метки с последними версиями
def update_version_label():
    last_app_android, last_app_ios = fetch_latest_versions()
    version_label.config(text=f"Latest Versions:\nANDROID: {last_app_android}\nIOS: {last_app_ios}")

# Функция для обновления поля "Enter Text" в зависимости от выбора платформы
def update_entry_text(combo_box, entry):
    platform = combo_box.get()
    last_app_android, last_app_ios = fetch_latest_versions()
    if platform == "ANDROID":
        entry.delete(0, tk.END)
        entry.insert(0, last_app_android)
    elif platform == "IOS":
        entry.delete(0, tk.END)
        entry.insert(0, last_app_ios)

# Функция для удаления старой версии
def on_remove_button_click():
    conn = ""  # Укажите ваши параметры подключения к базе данных
    cursor = conn.cursor()
    platform = remove_combo_box.get()
    user_input = remove_entry.get()
    cursor.execute(f"UPDATE ANALYTICS.TOLOG_TEST1 SET APP_ACT = 0 WHERE PLATFORM = '{platform}' AND VERSION = '{user_input}'")
    conn.commit()
    conn.close()
    messagebox.showinfo("Remove Version", f"Version removed - Platform: {platform}, Text: {user_input}")
    update_version_label()  # Обновляем метку с версиями после удаления

# Функция для добавления новой версии
def on_add_button_click():
    conn = ""  # Укажите ваши параметры подключения к базе данных
    cursor = conn.cursor()
    platform = add_combo_box.get()
    user_input = add_entry.get()
    cursor.execute(f"INSERT INTO ANALYTICS.TOLOG_TEST1 (PLATFORM, VERSION, APP_ACT) VALUES ('{platform}', '{user_input}', 1)")
    conn.commit()
    conn.close()
    messagebox.showinfo("Add Version", f"Version added - Platform: {platform}, Text: {user_input}")
    update_version_label()  # Обновляем метку с версиями после добавления

# Создаем основное окно приложения
root = tk.Tk()
root.title("Version Management App")

# Устанавливаем фиксированный размер окна
root.geometry("400x630")
root.resizable(False, False)

# Инициализируем метку с последними версиями
last_app_android, last_app_ios = fetch_latest_versions()
version_label = tk.Label(root, text=f"Latest Versions:\nANDROID: {last_app_android}\nIOS: {last_app_ios}", font=("Arial", 10, "bold"))
version_label.pack(pady=10)

# Разделитель после информации о версии
separator_label = tk.Label(root, text="---------------------------", font=("Arial", 10, "bold"))
separator_label.pack(pady=10)

# Секция для удаления старой версии
remove_label = tk.Label(root, text="Remove Old Version", font=("Arial", 10, "bold"))
remove_label.pack(pady=10)

remove_platform_label = tk.Label(root, text="Choose Platform:")
remove_platform_label.pack(pady=5)

remove_platforms = ["ANDROID", "IOS"]
remove_combo_box = ttk.Combobox(root, values=remove_platforms)
remove_combo_box.set(remove_platforms[0])
remove_combo_box.pack(pady=5)

remove_entry_label = tk.Label(root, text="Enter Text:")
remove_entry_label.pack(pady=5)

remove_entry = tk.Entry(root, width=40)
update_entry_text(remove_combo_box, remove_entry)
remove_entry.pack(pady=10)

remove_button = tk.Button(root, text="Remove Version", command=on_remove_button_click)
remove_button.pack(pady=10)

remove_combo_box.bind("<<ComboboxSelected>>", lambda event: update_entry_text(remove_combo_box, remove_entry))

# Разделитель между секциями
separator = tk.Label(root, text="---------------------------")
separator.pack(pady=10)

# Секция для добавления новой версии
add_label = tk.Label(root, text="Add New Version", font=("Arial", 10, "bold"))
add_label.pack(pady=10)

add_platform_label = tk.Label(root, text="Choose Platform:")
add_platform_label.pack(pady=5)

add_platforms = ["ANDROID", "IOS"]
add_combo_box = ttk.Combobox(root, values=add_platforms)
add_combo_box.set(add_platforms[0])
add_combo_box.pack(pady=5)

add_entry_label = tk.Label(root, text="Enter Text:")
add_entry_label.pack(pady=5)

add_entry = tk.Entry(root, width=40)
update_entry_text(add_combo_box, add_entry)
add_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Version", command=on_add_button_click)
add_button.pack(pady=10)

add_combo_box.bind("<<ComboboxSelected>>", lambda event: update_entry_text(add_combo_box, add_entry))

# Запускаем главное событие-цикл приложения
root.mainloop()

