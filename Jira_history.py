from datetime import datetime
from dateutil.relativedelta import relativedelta

# Текущая дата
current_date = datetime.now()

# Дата два месяца назад
two_months_ago = current_date - relativedelta(months=2)

# Первый день месяца два месяца назад
first_day_of_month_two_months_ago = two_months_ago.replace(day=1)

# Форматирование в строку для SQL-запроса
formatted_date = first_day_of_month_two_months_ago.strftime('%d.%m.%Y')

print(formatted_date)

