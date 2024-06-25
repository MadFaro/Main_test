# Задайте виртуальный PDF-принтер (например, Microsoft Print to PDF)
excel.ActivePrinter = "Microsoft Print to PDF"

# Путь для сохранения PDF файла
sheet.PrintOut(PrintToFile=True, PrToFileName=pdf_file)
