import phonenumbers
from phonenumbers import geocoder

# Пример номера телефона
phone_number = "+79876543210"

# Парсинг номера телефона
parsed_number = phonenumbers.parse(phone_number, "RU")  # "RU" - страна по умолчанию (Россия)

# Определение региона
region = geocoder.description_for_number(parsed_number, "ru")  # "ru" - код языка

print(f"Регион: {region}")

