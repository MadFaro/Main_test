
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)


import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    initial_dir = "C:/Users/tolog/Desktop/schedulerapp"  # Замените на нужный путь к папке
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    if file_path:
        file_label.config(text="Выбранный файл: " + file_path)
        selected_month = month_var.get()
        month_label.config(text="Выбранный месяц: " + selected_month)
    else:
        file_label.config(text="Файл не выбран")
        month_label.config(text="Месяц не выбран")

app = tk.Tk()
app.title("Выбор файла и месяца")
app.geometry("400x250")  
app.resizable(False, False)  

open_button = tk.Button(app, text="Выбрать файл", command=open_file_dialog)
open_button.pack(pady=20)

file_label = tk.Label(app, text="Файл не выбран")
file_label.pack()

# Добавляем выпадающий список с месяцами
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
month_var = tk.StringVar()
month_var.set(months[0])  # Устанавливаем начальное значение на Январь
month_option = tk.OptionMenu(app, month_var, *months)
month_option.pack()

month_label = tk.Label(app, text="Месяц не выбран")
month_label.pack()

app.mainloop()


