Option Explicit

Dim networkPath
networkPath = "\\server\share\путь\к\файлу.xlsx" ' Замените на путь к вашему файлу на сетевом диске

Dim objWMIService, colLocks, objLock
Set objWMIService = GetObject("winmgmts:\\.\root\CIMV2")

' Получаем список блокировок для файла
Set colLocks = objWMIService.ExecQuery("SELECT * FROM Win32_SMBShare WHERE Name = '" & networkPath & "'")

If colLocks.Count > 0 Then
    ' Файл заблокирован другим пользователем
    WScript.Echo "Файл заблокирован для редактирования другим пользователем."
Else
    ' Файл доступен для редактирования
    WScript.Echo "Файл доступен для редактирования."
End If
