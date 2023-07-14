Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim percentile30 As Double
    Dim percentile70 As Double
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng
    rowCount = dataRange.Rows.Count
    
    ' Вычисление значений, соответствующих 30% лучшим и 30% худшим результатам
    percentile30 = WorksheetFunction.Percentile(dataRange, 0.3)
    percentile70 = WorksheetFunction.Percentile(dataRange, 0.7)
    
    ' Проверка и раскраска каждой ячейки в соответствии с процентным значением
    For Each cell In dataRange
        If cell.Value >= percentile70 Then
            cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
        ElseIf cell.Value <= percentile30 Then
            cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
        Else
            cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
        End If
    Next cell
End Sub



