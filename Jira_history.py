Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim percentile30 As Double
    Dim percentile70 As Double
    Dim i As Long
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng
    rowCount = dataRange.Rows.Count
    
    ' Проверка и раскраска каждой ячейки в соответствии с процентным значением
    For Each cell In dataRange
        If cell.Offset(0, -1).Value = "Опытный" Then
            percentile30 = WorksheetFunction.PercentileIf(dataRange.Offset(0, 1), cell.Value, "<=" & "Опытный")
            percentile70 = WorksheetFunction.PercentileIf(dataRange.Offset(0, 1), cell.Value, "<=" & "Опытный")
        ElseIf cell.Offset(0, -1).Value = "Новичок" Then
            percentile30 = WorksheetFunction.PercentileIf(dataRange.Offset(0, 1), cell.Value, "<=" & "Новичок")
            percentile70 = WorksheetFunction.PercentileIf(dataRange.Offset(0, 1), cell.Value, "<=" & "Новичок")
        End If
        
        For i = 1 To rowCount
            If cell.Value >= percentile70 Then
                cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf cell.Value <= percentile30 Then
                cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
            End If
        Next i
    Next cell
End Sub




