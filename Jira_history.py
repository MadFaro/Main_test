Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim опытныйRange As Range
    Dim новичокRange As Range
    Dim опытныйValues() As Variant
    Dim новичокValues() As Variant
    Dim i As Long
    
    ' Выбор диапазона с данными
    Set rng = Selection
    
    ' Выделение столбца "Опытный"
    Set опытныйRange = Range(Cells(1, 1), Cells(rng.Rows.Count, 1))
    ' Выделение столбца "Значение"
    Set новичокRange = Range(Cells(1, 2), Cells(rng.Rows.Count, 2))
    
    ' Получение значений из столбцов
    опытныйValues = опытныйRange.Value
    новичокValues = новичокRange.Value
    
    ' Расчет и раскраска для опытных
    Dim опытный30 As Double
    Dim опытный70 As Double
    опытный30 = CalculatePercentile(опытныйValues, 0.3)
    опытный70 = CalculatePercentile(опытныйValues, 0.7)
    
    For i = 1 To UBound(опытныйValues)
        If опытныйValues(i, 1) = "Опытный" Then
            If новичокValues(i, 1) >= опытный70 Then
                новичокRange.Cells(i, 1).Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf новичокValues(i, 1) <= опытный30 Then
                новичокRange.Cells(i, 1).Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                новичокRange.Cells(i, 1).Interior.Color = RGB(255, 255, 0) ' Желтый цвет
            End If
        End If
    Next i
    
    ' Расчет и раскраска для новичков
    Dim новичок30 As Double
    Dim новичок70 As Double
    новичок30 = CalculatePercentile(новичокValues, 0.3)
    новичок70 = CalculatePercentile(новичокValues, 0.7)
    
    For i = 1 To UBound(новичокValues)
        If опытныйValues(i, 1) = "Новичок" Then
            If новичокValues(i, 1) >= новичок70 Then
                новичокRange.Cells(i, 1).Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf новичокValues(i, 1) <= новичок30 Then
                новичокRange.Cells(i, 1).Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                новичокRange.Cells(i, 1).Interior.Color = RGB(255, 255, 0) ' Желтый цвет
            End If
        End If
    Next i
End Sub

Function CalculatePercentile(values() As Variant, percentile As Double) As Double
    Dim sortedValues() As Variant
    sortedValues = values
    Call QuickSort(sortedValues, LBound(sortedValues), UBound(sortedValues))
    CalculatePercentile = sortedValues(Application.WorksheetFunction.RoundUp(percentile * UBound(sortedValues), 0))
End Function

Sub QuickSort(arr() As Variant, left As Long, right As Long)
    Dim i As Long
    Dim j As Long
    Dim pivot As Variant
    Dim temp As Variant
    
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
