# Определите функцию для преобразования значений в тип float
def to_float(x):
    try:
        return float(x)
    except ValueError:
        return x  # Если не удаётся преобразовать, оставляем значение без изменений

# Примените функцию ко всем столбцам, кроме первого
df.iloc[:, 1:] = df.iloc[:, 1:].applymap(to_float)

# Вывод преобразованного DataFrame
print(df)
