import pandas as pd
from datetime import timedelta

file_path = r"V:\VOL2\Contact-center\Файлы\Аналитика\Численность ДДО\022025\3.Чаты\Профиль нагрузки_чаты_022025.xlsx"

data = pd.read_excel(file_path, skiprows=1, usecols=range(28, 55)) 
data = data.drop(columns=data.columns[[0, 1, 2]]) 
data = data[data.iloc[:, 13].notna()] 

dates = pd.read_excel(file_path, usecols=[0], skiprows=1)

rows = []

for i, row in data.iterrows():
    date = dates.iloc[i, 0].strftime("%d.%m.%Y")
    
    for hour in range(24):
        time = f"{hour:02d}:00"
        
        # Преобразуем строку времени в объект datetime
        date_time_str = f"{date} {time}"
        date_time = pd.to_datetime(date_time_str, format="%d.%m.%Y %H:%M")
        
        # Сдвигаем время на 2 часа вперед для Уфы
        date_time_ufa = date_time + timedelta(hours=2)
        
        # Получаем новое время в формате "ДД.ММ.ГГГГ ЧЧ:ММ"
        new_time = date_time_ufa.strftime("%d.%m.%Y %H:%M")
        
        # Получаем значение для этого часа
        value = int(row[hour])
        
        # Добавляем строку с учетом сдвигов
        rows.append(["WEBIM_Chat", new_time, "01:00", value])

output_df = pd.DataFrame(rows, columns=["Имя очереди", "Дата и время", "Интервал времени", "Требования ЭПЗ"])

output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("DATE_TIME_FORMAT\n")
    f.write("DD.MM.YYYY HH:mm\n")
    f.write("Имя очереди\tДата и время\tИнтервал времени\tТребования ЭПЗ\n")
    
    for _, row in output_df.iterrows():
        line = "\t".join(str(value) for value in row)
        f.write(line + "\n")

print(f"Данные успешно преобразованы и сохранены в {output_file}")
