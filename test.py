import pandas as pd

# Чтение данных из Excel файла
excel_file = 'input.xlsx'  # Ваш файл Excel
sheet_name = 'Sheet1'      # Название листа
df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[1])  # Чтение только столбца B (индекс 1)

# Добавление пустого столбца перед данными
df.insert(0, 'Empty_Column', '')  # Вставляем пустой столбец перед данными

# Сохранение в CSV с разделителем запятая
csv_file = 'output.csv'
df.to_csv(csv_file, sep=',', index=False, header=False)

print(f'Данные сохранены в файл {csv_file}')
