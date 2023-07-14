Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim greenCount As Long
    Dim redCount As Long
    Dim yellowCount As Long
    Dim sortedRange As Range
    Dim percentile30 As Double
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng
    rowCount = dataRange.Rows.Count
    
    ' Определение числа строк, соответствующего 30% лучших значений
    greenCount = Round(rowCount * 0.3)
    
    ' Сортировка диапазона по возрастанию
    Set sortedRange = dataRange.Resize(, 1).Offset(, 1)
    sortedRange.Value = dataRange.Value
    sortedRange.Sort Key1:=sortedRange, Order1:=xlAscending, Header:=xlNo
    
    ' Определение значения, соответствующего 30% лучших значений
    percentile30 = sortedRange.Cells(greenCount).Value
    
    ' Проверка и раскраска каждой строки в соответствии с процентным значением
    For Each cell In dataRange
        If cell.Value >= percentile30 Then
            cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
        ElseIf cell.Value < percentile30 Then
            cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
        End If
    Next cell
    
    ' Очистка временного диапазона, используемого для сортировки
    sortedRange.Clear
End Sub


