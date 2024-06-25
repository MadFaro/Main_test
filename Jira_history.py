Traceback (most recent call last):
  File "w.py", line 11, in <module>
    xlsx2html(wb, f)
  File "C:\Python38\lib\site-packages\xlsx2html\core.py", line 380, in xlsx2html
    wb = openpyxl.load_workbook(filepath, data_only=True)
  File "C:\Python38\lib\site-packages\openpyxl\reader\excel.py", line 344, in load_workbook
    reader = ExcelReader(filename, read_only, keep_vba,
  File "C:\Python38\lib\site-packages\openpyxl\reader\excel.py", line 123, in __init__
    self.archive = _validate_archive(fn)
  File "C:\Python38\lib\site-packages\openpyxl\reader\excel.py", line 77, in _validate_archive
    file_format = os.path.splitext(filename)[-1].lower()
  File "C:\Python38\lib\ntpath.py", line 196, in splitext
    p = os.fspath(p)
TypeError: expected str, bytes or os.PathLike object, not Workbook
