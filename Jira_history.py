Option Explicit

Dim networkPath
networkPath = "\\server\share\путь\к\файлу.xlsx" ' Замените на путь к вашему файлу на сетевом диске

Dim fso, lockFile
Set fso = CreateObject("Scripting.FileSystemObject")

' Проверяем, существует ли временный файл блокировки
lockFile = fso.GetFile(networkPath & ".xlsx" & ".lock")

If fso.FileExists(lockFile) Then
    ' Файл заблокирован для редактирования
    WScript.Echo "Файл заблокирован для редактирования."
Else
    ' Файл не заблокирован и доступен для редактирования
    WScript.Echo "Файл доступен для редактирования."
End If
