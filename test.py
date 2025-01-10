import pandas as pd

# Чтение данных из Excel файла с листа 1
excel_file = 'input.xlsx'  # Укажите имя вашего файла
sheet_name = 'Sheet1'      # Название листа (обычно "Sheet1" по умолчанию)
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Сохранение данных в CSV файл с запятой в качестве разделителя
csv_file = 'output.csv'  # Укажите имя выходного файла
df.to_csv(csv_file, sep=',', index=False)

print(f'Данные сохранены в файл {csv_file}')

