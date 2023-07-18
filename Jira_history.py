Sub color_value_rating_division()
    Dim rngFlags As Range
    Dim rngValues As Range
    
    Dim selectedRange As Range
    Set selectedRange = Selection
    Set rngFlags = selectedRange.Areas(1).Columns(1)
    
    Dim valuesRange As Range
    If selectedRange.Areas.count > 1 Then
        Set valuesRange = selectedRange.Areas(2)
    Else
        Set valuesRange = selectedRange.Offset(0, 1).Resize(selectedRange.Rows.count, selectedRange.Columns.count - 1)
    End If
    
    Dim rowCount As Long
    Dim columnCount As Long
    
    rowCount = valuesRange.Rows.count
    columnCount = valuesRange.Columns.count
    
    Dim percentilesExp() As Variant
    Dim percentilesNov() As Variant
    ReDim percentilesExp(1 To columnCount, 1 To 2) As Variant
    ReDim percentilesNov(1 To columnCount, 1 To 2) As Variant
    
    Dim col As Long
    For col = 1 To columnCount
        Dim currentColumn As Range
        Set currentColumn = valuesRange.Columns(col)
        
        Dim expValues() As Double
        Dim novValues() As Double
        Dim expCount As Long
        Dim novCount As Long
        
        expCount = 0
        novCount = 0
        
        Dim i As Long
        For i = 1 To rowCount
            If rngFlags.Cells(i, 1).value = "Опытный" Then
                expCount = expCount + 1
                ReDim Preserve expValues(1 To expCount) As Double
                expValues(expCount) = currentColumn.Cells(i, 1).value
            ElseIf rngFlags.Cells(i, 1).value = "Новичок" Then
                novCount = novCount + 1
                ReDim Preserve novValues(1 To novCount) As Double
                novValues(novCount) = currentColumn.Cells(i, 1).value
            End If
        Next i

        QuickSort expValues, 1, expCount
        QuickSort novValues, 1, novCount

        Dim percentile30Exp As Double
        Dim percentile30Nov As Double
        Dim percentile70Exp As Double
        Dim percentile70Nov As Double
        
        percentile30Exp = GetPercentile(expValues, 0.3)
        percentile30Nov = GetPercentile(novValues, 0.3)
        percentile70Exp = GetPercentile(expValues, 0.7)
        percentile70Nov = GetPercentile(novValues, 0.7)
        
        percentilesExp(col, 1) = percentile30Exp
        percentilesExp(col, 2) = percentile70Exp
        percentilesNov(col, 1) = percentile30Nov
        percentilesNov(col, 2) = percentile70Nov
    Next col
    
    For col = 1 To columnCount
        For i = 1 To rowCount
            Dim flagValue As String
            flagValue = rngFlags.Cells(i, 1).value
            
            If flagValue = "Опытный" Then
                ColorCell valuesRange.Cells(i, col), percentilesExp(col, 1), percentilesExp(col, 2)
            ElseIf flagValue = "Новичок" Then
                ColorCell valuesRange.Cells(i, col), percentilesNov(col, 1), percentilesNov(col, 2)
            End If
        Next i
    Next col
End Sub
Function GetPercentile(sortedValues() As Double, percentile As Double) As Double
    Dim count As Long
    
    If Not IsEmpty(sortedValues) Then
        count = Application.WorksheetFunction.count(sortedValues)
    Else
        count = 0
    End If
    
    If count = 0 Then
        GetPercentile = 0
        Exit Function
    End If
    
    Dim percentileIndex As Double
    percentileIndex = Application.WorksheetFunction.Floor((percentile * count) + 1, 1)
    
    Dim k As Long
    k = CLng(percentileIndex)
    
    If k >= count Then
        GetPercentile = sortedValues(count)
    ElseIf k <= 1 Then
        GetPercentile = sortedValues(1)
    Else
        Dim d As Double
        d = percentileIndex - k
        
        GetPercentile = sortedValues(k) + d * (sortedValues(k + 1) - sortedValues(k))
    End If
End Function

Sub ColorCell(ByVal cell As Range, ByVal percentile30 As Double, ByVal percentile70 As Double)
    Dim value As Double
    value = cell.value

    If value >= percentile70 Then
        cell.Interior.Color = RGB(146, 208, 80)
    ElseIf value <= percentile30 Then
        cell.Interior.Color = RGB(255, 0, 0)
    Else
        cell.Interior.Color = RGB(255, 255, 0)
    End If
End Sub

Sub QuickSort(arr() As Double, ByVal left As Long, ByVal right As Long)
    Dim i As Long
    Dim j As Long
    Dim pivot As Double
    Dim temp As Double
    
    i = left
    j = right
    
    If left >= right Then Exit Sub
    
    If left + 1 = right Then
        If arr(left) > arr(right) Then
            temp = arr(left)
            arr(left) = arr(right)
            arr(right) = temp
        End If
        Exit Sub
    End If
    
    pivot = arr((left + right) \ 2)
    
    While i <= j
        While arr(i) < pivot
            i = i + 1
        Wend
        While arr(j) > pivot
            j = j - 1
        Wend
        If i <= j Then
            temp = arr(i)
            arr(i) = arr(j)
            arr(j) = temp
            i = i + 1
            j = j - 1
        End If
    Wend
    
    If left < j Then QuickSort arr, left, j
    If i < right Then QuickSort arr, i, right
End Sub



