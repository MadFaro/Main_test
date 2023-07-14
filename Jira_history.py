Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim rowCount As Long
    Dim greenCount As Long
    Dim redCount As Long
    Dim yellowCount As Long
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng.Value
    rowCount = dataRange.Rows.Count
    
    ' Вычисление количества строк для каждого цвета
    greenCount = Round(rowCount * 0.3)
    redCount = Round(rowCount * 0.3)
    yellowCount = rowCount - greenCount - redCount
    
    ' Проверка и раскраска каждой строки в соответствии с процентами
    For i = 1 To rowCount
        If i <= greenCount Then
            rng.Rows(i).Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
        ElseIf i > rowCount - redCount Then
            rng.Rows(i).Interior.Color = RGB(255, 0, 0) ' Красный цвет
        Else
            rng.Rows(i).Interior.Color = RGB(255, 255, 0) ' Желтый цвет
        End If
    Next i
End Sub
