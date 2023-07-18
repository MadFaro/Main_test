Sub color_value_rating()
    Dim rng As Range, cell As Range
    Dim percentile30 As Double, percentile70 As Double
    Dim columnCount As Integer
    
    Set rng = Selection
    columnCount = rng.Columns.Count
    
    For col = 1 To columnCount
        percentile30 = WorksheetFunction.Percentile(rng.Columns(col), 0.3)
        percentile70 = WorksheetFunction.Percentile(rng.Columns(col), 0.7)
        
        For Each cell In rng.Columns(col).Cells
            If cell.Value >= percentile70 Then
                cell.Interior.Color = RGB(146, 208, 80)
            ElseIf cell.Value <= percentile30 Then
                cell.Interior.Color = RGB(255, 0, 0)
            Else
                cell.Interior.Color = RGB(255, 255, 0)
            End If
        Next cell
    Next col
End Sub
