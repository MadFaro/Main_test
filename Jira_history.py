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
    
    Dim percentiles() As Variant
    ReDim percentiles(1 To columnCount, 1 To 2) As Variant
    
    Dim col As Long
    For col = 1 To columnCount
        Dim currentColumn As Range
        Set currentColumn = valuesRange.Columns(col)
        
        percentiles(col, 1) = WorksheetFunction.Percentile(currentColumn, 0.3)
        percentiles(col, 2) = WorksheetFunction.Percentile(currentColumn, 0.7)
    Next col
    
    For col = 1 To columnCount
        Dim currentColumn1 As Range
        Set currentColumn1 = valuesRange.Columns(col)
        
        For row = 1 To rowCount
            Dim flagValue1 As String
            flagValue1 = rngFlags.Cells(row, 1).Value
            
            If flagValue1 = "Опытный" Then
                ColorCell currentColumn1.Cells(row), percentiles(col, 1), percentiles(col, 2), "Опытный"
            ElseIf flagValue1 = "Новичок" Then
                ColorCell currentColumn1.Cells(row), percentiles(col, 1), percentiles(col, 2), "Новичок"
            End If
        Next row
    Next col
End Sub

Sub ColorCell(ByVal cell As Range, ByVal percentile30 As Double, ByVal percentile70 As Double, ByVal flagValue As String)
    If cell.Value >= percentile70 And flagValue = "Опытный" Then
        cell.Interior.Color = RGB(146, 208, 80)
    ElseIf cell.Value >= percentile70 And flagValue = "Новичок" Then
        cell.Interior.Color = RGB(0, 176, 240)
    ElseIf cell.Value <= percentile30 And flagValue = "Опытный" Then
        cell.Interior.Color = RGB(255, 0, 0)
    ElseIf cell.Value <= percentile30 And flagValue = "Новичок" Then
        cell.Interior.Color = RGB(255, 192, 0)
    Else
        cell.Interior.Color = RGB(255, 255, 0)
    End If
End Sub

