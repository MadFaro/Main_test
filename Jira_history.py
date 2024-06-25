pip install openpyxl pdfkit xlsx2html

import openpyxl
from xlsx2html import xlsx2html
import pdfkit

# Загрузите ваш Excel файл
wb = openpyxl.load_workbook('your_excel_file.xlsx')
sheet = wb.active

# Конвертируйте лист Excel в HTML
with open('output.html', 'w', encoding='utf-8') as f:
    xlsx2html(wb, f)

# Опции для pdfkit, чтобы установить правильный размер страницы и ориентацию
options = {
    'page-size': 'A4',
    'orientation': 'Landscape',  # или 'Portrait'
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

# Конвертируйте HTML в PDF
pdfkit.from_file('output.html', 'output.pdf', options=options)

