import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle, datetime, win32com.client

conn = ""
cursor = conn.cursor()
cursor.execute("SELECT PLATFORM,VERSION FROM ANALYTICS.TOLOG_TEST1 WHERE PLATFORM IN ('ANDROID', 'IOS') AND APP_ACT = 1")
result = cursor.fetchall()
conn.close()

# Обрабатываем результат
last_app_android = 0.0
last_app_ios = 0.0

for row in result:
    if row[0] == 'ANDROID':
        last_app_android = row[1]
    elif row[0] == 'IOS':
        last_app_ios = row[1]

# Функция для обновления поля "Enter Text" в зависимости от выбора платформы
def update_entry_text(combo_box, entry):
    platform = combo_box.get()
    if platform == "ANDROID":
        entry.delete(0, tk.END)  # Очистка текущего текста
        entry.insert(0, last_app_android)  # Установка текста для ANDROID
    elif platform == "IOS":
        entry.delete(0, tk.END)  # Очистка текущего текста
        entry.insert(0, last_app_ios)  # Установка текста для IOS

# Функция для удаления старой версии
def on_remove_button_click():
    conn = ""
    cursor = conn.cursor()
    platform = remove_combo_box.get()  # Получаем выбранную платформу для удаления
    user_input = remove_entry.get()  # Получаем текст для удаления
    cursor.execute(f"update ANALYTICS.TOLOG_TEST1 set APP_ACT = 0 where platform = '{platform}' and version = '{user_input}'")
    conn.commit()
    conn.close()
    messagebox.showinfo("Remove Version", f"Version removed - Platform: {platform}, Text: {user_input}")

# Функция для добавления новой версии
def on_add_button_click():
    conn = ""
    cursor = conn.cursor()
    platform = add_combo_box.get()  # Получаем выбранную платформу для добавления
    user_input = add_entry.get()  # Получаем текст для добавления
    cursor.execute(f"insert into ANALYTICS.TOLOG_TEST1 (platform, version, app_act) values ('{platform}', '{user_input}', 1)")
    conn.commit()
    conn.close()
    messagebox.showinfo("Add Version", f"Version added - Platform: {platform}, Text: {user_input}")

# Создаем основное окно приложения
root = tk.Tk()
root.title("Version Management App")

# Устанавливаем фиксированный размер окна
root.geometry("400x630")
root.resizable(False, False)  # Отключаем возможность изменения размера окна

# Секция для отображения актуальной версии приложения
version_label = tk.Label(root, text=f"Latest Versions:\nANDROID: {last_app_android}\nIOS: {last_app_ios}", font=("Arial", 10, "bold"))
version_label.pack(pady=10)

# Разделитель после информации о версии
separator_label = tk.Label(root, text="---------------------------", font=("Arial", 10, "bold"))
separator_label.pack(pady=10)

# Секция для удаления старой версии
remove_label = tk.Label(root, text="Remove Old Version",  font=("Arial", 10, "bold"))
remove_label.pack(pady=10)

remove_platform_label = tk.Label(root, text="Choose Platform:")
remove_platform_label.pack(pady=5)

remove_platforms = ["ANDROID", "IOS"]
remove_combo_box = ttk.Combobox(root, values=remove_platforms)
remove_combo_box.set(remove_platforms[0])  # Устанавливаем значение по умолчанию
remove_combo_box.pack(pady=5)

remove_entry_label = tk.Label(root, text="Enter Text:")
remove_entry_label.pack(pady=5)

remove_entry = tk.Entry(root, width=40)
update_entry_text(remove_combo_box, remove_entry)  # Устанавливаем текст в зависимости от платформы
remove_entry.pack(pady=10)

remove_button = tk.Button(root, text="Remove Version", command=on_remove_button_click)
remove_button.pack(pady=10)

# Обновление текста в поле ввода при смене выбора в ComboBox
remove_combo_box.bind("<<ComboboxSelected>>", lambda event: update_entry_text(remove_combo_box, remove_entry))

# Разделитель между секциями
separator = tk.Label(root, text="---------------------------")
separator.pack(pady=10)

# Секция для добавления новой версии
add_label = tk.Label(root, text="Add New Version",  font=("Arial", 10, "bold"))
add_label.pack(pady=10)

add_platform_label = tk.Label(root, text="Choose Platform:")
add_platform_label.pack(pady=5)

add_platforms = ["ANDROID", "IOS"]
add_combo_box = ttk.Combobox(root, values=add_platforms)
add_combo_box.set(add_platforms[0])  # Устанавливаем значение по умолчанию
add_combo_box.pack(pady=5)

add_entry_label = tk.Label(root, text="Enter Text:")
add_entry_label.pack(pady=5)

add_entry = tk.Entry(root, width=40)
update_entry_text(add_combo_box, add_entry)  # Устанавливаем текст в зависимости от платформы
add_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Version", command=on_add_button_click)
add_button.pack(pady=10)

# Обновление текста в поле ввода при смене выбора в ComboBox
add_combo_box.bind("<<ComboboxSelected>>", lambda event: update_entry_text(add_combo_box, add_entry))

# Запускаем главное событие-цикл приложения
root.mainloop()
