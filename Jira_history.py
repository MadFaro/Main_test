Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim percentile30 As Double
    Dim percentile70 As Double
    Dim categoryColumn As Range
    Dim valueColumn As Range
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng.Columns(2) ' Выбор только второго столбца
    rowCount = dataRange.Rows.Count
    
    ' Проверка и раскраска каждой ячейки во втором столбце в соответствии с процентным значением
    For Each cell In dataRange
        Set categoryColumn = rng.Columns(1) ' Столбец с категориями ("Опытный" или "Новичок")
        Set valueColumn = rng.Columns(2) ' Столбец с числовыми значениями
        
        ' Расчет процентилей для каждой категории
        percentile30 = CalculatePercentile(categoryColumn, valueColumn, cell.Offset(0, -1).Value, 0.3)
        percentile70 = CalculatePercentile(categoryColumn, valueColumn, cell.Offset(0, -1).Value, 0.7)
        
        ' Применение соответствующей заливки
        If cell.Value >= percentile70 Then
            cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
        ElseIf cell.Value <= percentile30 Then
            cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
        Else
            cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
        End If
    Next cell
End Sub

Function CalculatePercentile(categoryColumn As Range, valueColumn As Range, category As String, percentile As Double) As Double
    Dim categoryValues As Range
    Dim valueRange As Range
    Dim i As Long
    Dim values() As Double
    Dim count As Long
    
    ' Определение диапазона значений для указанной категории
    Set categoryValues = categoryColumn.Cells
    Set valueRange = valueColumn.Cells
    
    ' Подсчет количества значений для указанной категории
    count = Application.WorksheetFunction.CountIf(categoryValues, category)
    
    ' Заполнение массива значениями для указанной категории
    ReDim values(1 To count)
    For i = 1 To count
        values(i) = valueRange.Cells(Application.WorksheetFunction.Match(category, categoryValues, 0) + i - 1).Value
    Next i
    
    ' Сортировка массива значений по возрастанию
    Call QuickSort(values, 1, count)
    
    ' Вычисление процентиля для указанной категории
    CalculatePercentile = values(Application.WorksheetFunction.RoundUp(percentile * count, 0))
End Function

Sub QuickSort(arr() As Double, left As Long, right As Long)
    Dim i As Long
    Dim j As Long
    Dim pivot As Double
    Dim temp As Double
    
    i = left
    j = right
    pivot = arr((left + right) \ 2)
    
    Do While i <= j
        Do While arr(i) < pivot
            i = i + 1
        Loop
        
        Do While arr(j) > pivot
            j = j - 1
        Loop
        
        If i <= j Then
            temp = arr(i)
            arr(i) = arr(j)
            arr(j) = temp
            i = i + 1
            j = j - 1
        End If
    Loop
    
    If left < j Then
        Call QuickSort(arr, left, j)
    End If
    
    If i < right Then
        Call QuickSort(arr, i, right)
    End If
End Sub






