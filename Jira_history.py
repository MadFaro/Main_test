Sub РаскраситьРезультаты()
    Dim rng As Range
    Dim dataRange As Range
    Dim values() As Variant
    Dim опытныйValues() As Variant
    Dim новичокValues() As Variant
    Dim i As Long
    
    ' Выбор диапазона с данными
    Set rng = Range("A1:B14")
    Set dataRange = rng.Resize(rng.Rows.Count, 1) ' Выбор только первого столбца (категория)
    
    ' Получение значений из выбранного столбца
    values = dataRange.Value
    
    ' Определение размеров массивов для опытных и новичков
    Dim опытныйCount As Long
    Dim новичокCount As Long
    For i = 1 To UBound(values)
        If values(i, 1) = "Опытный" Then
            опытныйCount = опытныйCount + 1
        ElseIf values(i, 1) = "Новичок" Then
            новичокCount = новичокCount + 1
        End If
    Next i
    
    ' Создание массивов для опытных и новичков
    ReDim опытныйValues(1 To опытныйCount)
    ReDim новичокValues(1 To новичокCount)
    
    ' Заполнение массивов значениями для опытных и новичков
    Dim опытныйIndex As Long
    Dim новичокIndex As Long
    опытныйIndex = 1
    новичокIndex = 1
    For i = 1 To UBound(values)
        If values(i, 1) = "Опытный" Then
            опытныйValues(опытныйIndex) = values(i, 2)
            опытныйIndex = опытныйIndex + 1
        ElseIf values(i, 1) = "Новичок" Then
            новичокValues(новичокIndex) = values(i, 2)
            новичокIndex = новичокIndex + 1
        End If
    Next i
    
    ' Расчет и раскраска для опытных
    Dim опытный30 As Double
    Dim опытный70 As Double
    опытный30 = CalculatePercentile(опытныйValues, 0.3)
    опытный70 = CalculatePercentile(опытныйValues, 0.7)
    
    For i = 1 To UBound(values)
        If values(i, 1) = "Опытный" Then
            If values(i, 2) >= опытный70 Then
                rng.Cells(i, 2).Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf values(i, 2) <= опытный30 Then
                rng.Cells(i, 2).Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                rng.Cells(i, 2).Interior.Color = RGB(255, 255, 0) ' Желтый цвет
            End If
        End If
    Next i
    
    ' Расчет и раскраска для новичков
    Dim новичок30 As Double
    Dim новичок70 As Double
    новичок30 = CalculatePercentile(новичокValues, 0.3)
    новичок70 = CalculatePercentile(новичокValues, 0.7)
    
    For i = 1 To UBound(values)
        If values(i, 1) = "Новичок" Then
            If values(i, 2) >= новичок70 Then
                rng.Cells(i, 2).Interior.Color = RGB(255, 0, 0) ' Красный цвет
            ElseIf values(i, 2) <= новичок30 Then
                rng.Cells(i, 2).Interior.Color = RGB(0, 255, 0) ' Зеленый цвет
            Else
                rng.Cells(i, 2).Interior.Color = RGB(255, 255, 0) ' Желтый цвет
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
