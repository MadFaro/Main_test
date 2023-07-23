Option Explicit

Dim networkPath
networkPath = "\\server\share\путь\к\файлу.xlsx" ' Замените на путь к вашему файлу на сетевом диске

Dim excelApp, excelWorkbook
Set excelApp = CreateObject("Excel.Application")

' Пытаемся открыть файл
On Error Resume Next
Set excelWorkbook = excelApp.Workbooks.Open(networkPath, False, True) ' False - не открывать в режиме редактирования
On Error GoTo 0

If excelWorkbook Is Nothing Then
    ' Файл заблокирован для редактирования
    WScript.Echo "Файл заблокирован для редактирования."
Else
    ' Файл доступен для редактирования
    WScript.Echo "Файл доступен для редактирования."
    excelWorkbook.Close False ' Закрываем файл без сохранения, так как он открыт только для проверки блокировки
End If

excelApp.Quit


