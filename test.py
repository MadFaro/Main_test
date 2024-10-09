import pandas as pd

# Чтение исходного файла
filename = "data.txt"

# Чтение данных из файла (пропускаем первую строку и задаем разделитель как табуляцию)
data = pd.read_csv(filename, delimiter='\t', skiprows=2, header=None)

# Умножаем значения 5-го столбца (объём) на 140% (или 1.4)
data[4] = data[4] * 1.4

# Сохранение измененного файла
data.to_csv("data_updated.txt", sep='\t', index=False, header=False)
