Sub color_value_rating_division()
    Dim rngFlags As Range
    Dim rngValues As Range
    
    Dim selectedRange As Range
    Set selectedRange = Selection
    Set rngFlags = selectedRange.Areas(1).Columns(1)
    
    Dim valuesRange As Range
    If selectedRange.Areas.Count > 1 Then
        Set valuesRange = selectedRange.Areas(2)
    Else
        Set valuesRange = selectedRange.Offset(0, 1).Resize(selectedRange.Rows.Count, selectedRange.Columns.Count - 1)
    End If
    
    Dim rowCount As Long
    Dim columnCount As Long
    
    rowCount = valuesRange.Rows.Count
    columnCount = valuesRange.Columns.Count
    
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
            If rngFlags.Cells(i, 1).Value = "Опытный" Then
                expCount = expCount + 1
                ReDim Preserve expValues(1 To expCount) As Double
                expValues(expCount) = currentColumn.Cells(i, col).Value
            ElseIf rngFlags.Cells(i, 1).Value = "Новичок" Then
                novCount = novCount + 1
                ReDim Preserve novValues(1 To novCount) As Double
                novValues(novCount) = currentColumn.Cells(i, col).Value
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
            flagValue = rngFlags.Cells(i, 1).Value
            
            If flagValue = "Опытный" Then
                ColorCell valuesRange.Cells(i, col), percentilesExp(col, 1), percentilesExp(col, 2)
            ElseIf flagValue = "Новичок" Then
                ColorCell valuesRange.Cells(i, col), percentilesNov(col, 1), percentilesNov(col, 2)
            End If
        Next i
    Next col
End Sub


