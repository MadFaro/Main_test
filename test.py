search_filter = "(objectClass=computer)"  # Получим все компьютеры
attributes = ["cn", "distinguishedName", "operatingSystem"]

# Выполним поиск
conn.search(SEARCH_BASE, search_filter, attributes=attributes)

# Выведем результаты
if conn.entries:
    for entry in conn.entries:
        print(entry)
else:
    print("Ничего не найдено.")
