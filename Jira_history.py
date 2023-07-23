Option Explicit

Dim networkPath
networkPath = "\\server\share\путь\к\файлу.xlsx" ' Замените на путь к вашему файлу на сетевом диске

Dim fso, file
Set fso = CreateObject("Scripting.FileSystemObject")

' Пытаемся открыть файл на чтение
On Error Resume Next
Set file = fso.OpenTextFile(networkPath, 1, False) ' 1 - режим только чтение
On Error GoTo 0

If Err.Number = 0 Then
    ' Файл доступен для редактирования
    WScript.Echo "Файл доступен для редактирования."
    file.Close
Else
    ' Файл заблокирован для редактирования
    WScript.Echo "Файл заблокирован для редактирования."
End If
