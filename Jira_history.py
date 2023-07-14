Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim cell As Range
    Dim rowCount As Long
    Dim percentile30 As Double
    Dim percentile70 As Double
    Dim опытныйValues() As Double
    Dim новичокValues() As Double
    Dim опытныйCount As Long
    Dim новичокCount As Long
    
    ' Выбор диапазона, в котором нужно раскрасить результаты
    Set rng = Selection
    Set dataRange = rng.Columns(2) ' Выбор только второго столбца
    rowCount = dataRange.Rows.Count
    
    ' Создание отдельных массивов для опытных и новичков
    опытныйCount = Application.WorksheetFunction.CountIf(rng.Columns(1), "Опытный")
    новичокCount = Application.WorksheetFunction.CountIf(rng.Columns(1), "Новичок")
    ReDim опытныйValues(1 To опытныйCount)
    ReDim новичокValues(1 To новичокCount)
    
    ' Заполнение массивов значениями для опытных и новичков
    Dim i As Long
    Dim j As Long
    i = 1
    j = 1
    For Each cell In rng.Columns(1)
        If cell.Value = "Опытный" Then
            опытныйValues(i) = cell.Offset(0, 1).Value
            i = i + 1
        ElseIf cell.Value = "Новичок" Then
            новичокValues(j) = cell.Offset(0, 1).Value
            j = j + 1
        End If
    Next cell
    
    ' Расчет и раскраска для опытных
    For Each cell In rng.Columns(2)
        If IsNumeric(cell.Offset(0, -1).Value) And cell.Offset(0, -1).Value = "Опытный" Then
            percentile30 = CalculatePercentile(опытныйValues, 0.3)
            percentile70 = CalculatePercentile(опытныйValues, 0.7)
            
            ' Применение соответствующей заливки
            If cell.Value >= percentile70 Then
                cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf cell.Value <= percentile30 Then
                cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
            End If
        End If
    Next cell
    
    ' Расчет и раскраска для новичков
    For Each cell In rng.Columns(2)
        If IsNumeric(cell.Offset(0, -1).Value) And cell.Offset(0, -1).Value = "Новичок" Then
            percentile30 = CalculatePercentile(новичокValues, 0.3)
            percentile70 = CalculatePercentile(новичокValues, 0.7)
            
            ' Применение соответствующей заливки
            If cell.Value >= percentile70 Then
                cell.Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf cell.Value <= percentile30 Then
                cell.Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                cell.Interior.Color = RGB(255, 255, 0) ' Желтый цвет
            End If
        End If
    Next cell
End Sub

Function CalculatePercentile(values() As Double, percentile As Double) As Double
    Dim count As Long
    Dim sortedValues() As Double
    
    ' Подсчет количества значений
    count = UBound(values)
    
    ' Копирование значений в новый массив
    ReDim sortedValues(1 To count)
    For i = 1 To count
        sortedValues(i) = values(i)
    Next i
    
    ' Сортировка массива значений по возрастанию
    Call QuickSort(sortedValues, 1, count)
    
    ' Вычисление процентиля
    CalculatePercentile = sortedValues(Application.WorksheetFunction.RoundUp(percentile * count, 0))
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


