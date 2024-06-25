Traceback (most recent call last):
  File "w.py", line 17, in <module>
    excel.ActivePrinter = "Microsoft Print to PDF"
  File "C:\Python38\lib\site-packages\win32com\client\dynamic.py", line 685, in __setattr__
    self._oleobj_.Invoke(entry.dispid, 0, invoke_type, 0, value)
pywintypes.com_error: (-2147352567, 'Ошибка.', (0, 'Microsoft Excel', 'Нельзя установить свойство ActivePrinter класса Application', 'xlmain11.chm', 0, -2146827284), None)
