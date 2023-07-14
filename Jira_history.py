Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim percentile30 As Double
    Dim percentile70 As Double
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng.Columns(2) ' Выбор только второго столбца
    rowCount = dataRange.Rows.Count
    
    ' Проверка и раскраска каждой ячейки во втором столбце в соответствии с процентным значением
    For Each cell In dataRange
        If cell.Offset(0, -1).Value = "Опытный" Then
            percentile30 = WorksheetFunction.PercentileIf(rng.Columns(2), "Опытный", rng.Columns(1), "<=" & cell.Offset(0, -1).Value)
            percentile70 = WorksheetFunction.PercentileIf(rng.Columns(2), "Опытный", rng.Columns(1), "<=" & cell.Offset(0, -1).Value)
        ElseIf cell.Offset(0, -1).Value = "Новичок" Then
            percentile30 = WorksheetFunction.PercentileIf(rng.Columns(2), "Новичок", rng.Columns(1), "<=" & cell.Offset(0, -1).Value)
            percentile70 = WorksheetFunction.PercentileIf(rng.Columns(2), "Новичок", rng.Columns(1), "<=" & cell.Offset(0, -1).Value)
        End If
        
        If cell.Value >= percentile70 Then
            cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
        ElseIf cell.Value <= percentile30 Then
            cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
        Else
            cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
        End If
    Next cell
End Sub





