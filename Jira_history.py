import re

# Ваша запись
record = "from table1@link1 sdsd или left join table2@link2 s или inner join table3@link3 или ничего"

# Паттерн регулярного выражения
pattern = r'\b\w+@\w+\b'

# Ищем совпадения
matches = re.findall(pattern, record)

# Выводим найденные совпадения
for match in matches:
    print(match)
