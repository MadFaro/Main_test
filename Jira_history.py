import win32com.client

# Задайте путь к вашему Excel файлу и имя выходного PDF файла
excel_file = 'your_excel_file.xlsx'
pdf_file = 'output.pdf'

# Создайте экземпляр приложения Excel
excel = win32com.client.Dispatch("Excel.Application")

# Откройте рабочую книгу
workbook = excel.Workbooks.Open(excel_file)

# Задайте лист, который нужно сохранить в PDF
sheet = workbook.Sheets[1]  # Измените индекс, если нужно сохранить другой лист

# Сохраните лист в PDF
sheet.ExportAsFixedFormat(0, pdf_file)

# Закройте рабочую книгу и завершите приложение Excel
workbook.Close(SaveChanges=False)
excel.Quit()
