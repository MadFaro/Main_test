Sub color_value_rating()
    Dim rng, cell As Range
    Dim percentile30, percentile70 As Double
    
    Set rng = Selection
    
    percentile30 = WorksheetFunction.Percentile(rng, 0.3)
    percentile70 = WorksheetFunction.Percentile(rng, 0.7)
    
    For Each cell In rng
        If cell.Value >= percentile70 Then
            cell.Interior.Color = RGB(146, 208, 80)
        ElseIf cell.Value <= percentile30 Then
            cell.Interior.Color = RGB(255, 0, 0)
        Else
            cell.Interior.Color = RGB(255, 255, 0)
        End If
    Next cell
End Sub
