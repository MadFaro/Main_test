Sub CopyAndPasteValues()
    Dim App As Object
    Dim wb As Object
    Dim ws As Object
    
    Set App = CreateObject("Excel.Application")
    App.Visible = False
    
    Set wb = App.Workbooks.Open("C:\Users\TologonovAB\Desktop\Динамика показателей ДТ(рабочая версия).xlsx")
    Set ws = wb.Sheets("название_листа_с_формулами") ' Замените "название_листа_с_формулами" на актуальное имя листа
    
    ' Копируем и вставляем значения и форматы вместо формул
    ws.UsedRange.Copy
    ws.UsedRange.PasteSpecial Paste:=xlPasteValuesAndNumberFormats
    Application.CutCopyMode = False ' Очистить буфер обмена
    
    ' Сохраняем книгу
    wb.SaveAs "C:\Users\TologonovAB\Desktop\Динамика показателей ДТ(рабочая версия) итог.xlsx"
    
    ' Закрываем Excel и очищаем переменные
    wb.Close
    App.Quit
    Set ws = Nothing
    Set wb = Nothing
    Set App = Nothing
End Sub
