Sub color_value_rating_division()
    Dim rng As Range, cell As Range
    Dim columnCount As Integer
    Dim flagRange As Range, valueRange As Range
    Dim flagCell As Range, valueCell As Range
    
    Set rng = Selection
    columnCount = rng.Columns.Count
    
    Set flagRange = rng.Columns(1)
    
    For col = 2 To columnCount
        Set valueRange = rng.Columns(col)
        
        For Each flagCell In flagRange.Cells
            Set valueCell = valueRange.Cells(flagCell.Row - rng.Row + 1)
            
            If flagCell.value = "Îïûòíûé" Then
                If valueCell.value >= 30 Then
                    valueCell.Interior.Color = RGB(146, 208, 80)
                ElseIf valueCell.value >= 20 Then
                    valueCell.Interior.Color = RGB(255, 255, 0)
                ElseIf valueCell.value >= 10 Then
                    valueCell.Interior.Color = RGB(255, 0, 0)
                End If
            ElseIf flagCell.value = "Íîâè÷îê" Then
                If valueCell.value >= 30 Then
                    valueCell.Interior.Color = RGB(146, 208, 80)
                ElseIf valueCell.value >= 20 Then
                    valueCell.Interior.Color = RGB(255, 255, 0)
                ElseIf valueCell.value >= 10 Then
                    valueCell.Interior.Color = RGB(255, 0, 0)
                End If
            End If
        Next flagCell
    Next col
End Sub
