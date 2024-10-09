import pandas as pd

# Чтение исходного файла
filename = "data.txt"

# Чтение данных из файла (пропускаем первые две строки и задаем разделитель как табуляцию)
data = pd.read_csv(filename, delimiter='\t', skiprows=2, header=None)

# Преобразование столбца 5 (индекс 4) в числовой формат
data[4] = pd.to_numeric(data[4], errors='coerce')

# Умножаем значения 5-го столбца (объём) на 140% (или 1.4)
data[4] = data[4] * 1.4

# Сохранение измененного файла
data.to_csv("data_updated.txt", sep='\t', index=False, header=False)
