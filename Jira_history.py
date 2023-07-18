Sub color_value_rating_division()
    Dim rng As Range, cell As Range
    Dim percentile30_flag1 As Double, percentile70_flag1 As Double
    Dim percentile30_flag2 As Double, percentile70_flag2 As Double
    Dim rowCount As Integer, columnCount As Integer
    Dim flagColumn As Range
    
    Set rng = Selection
    rowCount = rng.Rows.Count
    columnCount = rng.Columns.Count
    
    Set flagColumn = rng.Columns(1)
    
    For Row = 1 To rowCount
        If flagColumn.Cells(Row, 1).value = "Опытный" Then
            For col = 2 To columnCount
                If percentile30_flag1 = 0 Then
                    percentile30_flag1 = rng.Cells(Row, col).value
                    percentile70_flag1 = rng.Cells(Row, col).value
                Else
                    If rng.Cells(Row, col).value < percentile30_flag1 Then
                        percentile30_flag1 = rng.Cells(Row, col).value
                    ElseIf rng.Cells(Row, col).value > percentile70_flag1 Then
                        percentile70_flag1 = rng.Cells(Row, col).value
                    End If
                End If
            Next col
        ElseIf flagColumn.Cells(Row, 1).value = "Новичок" Then
            For col = 2 To columnCount
                If percentile30_flag2 = 0 Then
                    percentile30_flag2 = rng.Cells(Row, col).value
                    percentile70_flag2 = rng.Cells(Row, col).value
                Else
                    If rng.Cells(Row, col).value < percentile30_flag2 Then
                        percentile30_flag2 = rng.Cells(Row, col).value
                    ElseIf rng.Cells(Row, col).value > percentile70_flag2 Then
                        percentile70_flag2 = rng.Cells(Row, col).value
                    End If
                End If
            Next col
        End If
    Next Row
    
    For Row = 1 To rowCount
        For col = 2 To columnCount
            If flagColumn.Cells(Row, 1).value = "Опытный" Then
                If rng.Cells(Row, col).value >= percentile70_flag1 Then
                    rng.Cells(Row, col).Interior.Color = RGB(146, 208, 80)
                ElseIf rng.Cells(Row, col).value <= percentile30_flag1 Then
                    rng.Cells(Row, col).Interior.Color = RGB(255, 0, 0)
                Else
                    rng.Cells(Row, col).Interior.Color = RGB(255, 255, 0)
                End If
            ElseIf flagColumn.Cells(Row, 1).value = "Новичок" Then
                If rng.Cells(Row, col).value >= percentile70_flag2 Then
                    rng.Cells(Row, col).Interior.Color = RGB(146, 208, 80)
                ElseIf rng.Cells(Row, col).value <= percentile30_flag2 Then
                    rng.Cells(Row, col).Interior.Color = RGB(255, 0, 0)
                Else
                    rng.Cells(Row, col).Interior.Color = RGB(255, 255, 0)
                End If
            End If
        Next col
    Next Row
End Sub
