Function GetPercentile(sortedValues() As Double, percentile As Double) As Double
    Dim count As Long
    
    If IsEmpty(sortedValues) Or Len(sortedValues) = 0 Then
        count = 0
    Else
        count = UBound(sortedValues) - LBound(sortedValues) + 1
    End If
    
    If count <= 0 Then
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




