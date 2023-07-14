Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim greenCount As Long
    Dim redCount As Long
    Dim yellowCount As Long
    Dim minValue As Double
    Dim maxValue As Double
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng
    rowCount = dataRange.Rows.Count
    
    ' Определение минимального и максимального значения в выбранном диапазоне
    minValue = WorksheetFunction.Min(dataRange)
    maxValue = WorksheetFunction.Max(dataRange)
    
    ' Вычисление пороговых значений для каждого цвета
    greenCount = Round(rowCount * 0.3)
    redCount = Round(rowCount * 0.3)
    yellowCount = rowCount - greenCount - redCount
    
    ' Проверка и раскраска каждой строки в соответствии с процентами
    For Each cell In dataRange
        If cell.Value >= maxValue - (maxValue - minValue) * 0.3 Then
            cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
        ElseIf cell.Value <= minValue + (maxValue - minValue) * 0.3 Then
            cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
        Else
            cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
        End If
    Next cell
End Sub

