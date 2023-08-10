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
    Dim expCountPerColumn() As Long
    Dim novCountPerColumn() As Long
    ReDim expCountPerColumn(1 To columnCount) As Long
    ReDim novCountPerColumn(1 To columnCount) As Long
    
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
            If rngFlags.Cells(i, 1).Value = "Îïûòíûé" Then
                expCount = expCount + 1
                ReDim Preserve expValues(1 To expCount) As Double
                expValues(expCount) = currentColumn.Cells(i, 1).Value
                expCountPerColumn(col) = expCountPerColumn(col) + 1
            ElseIf rngFlags.Cells(i, 1).Value = "Íîâè÷îê" Then
                novCount = novCount + 1
                ReDim Preserve novValues(1 To novCount) As Double
                novValues(novCount) = currentColumn.Cells(i, 1).Value
                novCountPerColumn(col) = novCountPerColumn(col) + 1
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
        
        Dim expRatio As Double
        Dim novRatio As Double
        
        expRatio = WorksheetFunction.Min(expCountPerColumn(col) * 0.3 / 0.4, 1)
        novRatio = WorksheetFunction.Min(novCountPerColumn(col) * 0.3 / 0.4, 1)
        
        percentilesExp(col, 1) = (percentile30Exp - percentile30Nov) * expRatio + percentile30Nov
        percentilesExp(col, 2) = (percentile70Exp - percentile70Nov) * expRatio + percentile70Nov
        percentilesNov(col, 1) = (percentile30Nov - percentile30Exp) * novRatio + percentile30Exp
        percentilesNov(col, 2) = (percentile70Nov - percentile70Exp) * novRatio + percentile70Exp
    Next col
    
    Dim greenCount As Long
    Dim redCount As Long
    
    greenCount = 0
    redCount = 0
    
    For col = 1 To columnCount
        greenCount = greenCount + expCountPerColumn(col) * 0.3
        redCount = redCount + novCountPerColumn(col) * 0.3
    Next col
    
    Dim yellowCount As Long
    yellowCount = rowCount - greenCount - redCount
    
    Dim targetYellowCount As Long
    targetYellowCount = yellowCount
    
    For col = 1 To columnCount
        Dim currentColumn As Range
        Set currentColumn = valuesRange.Columns(col)
        
        For i = 1 To rowCount
            Dim flagValue As String
            flagValue = rngFlags.Cells(i, 1).Value
            Dim value As Double
            value = currentColumn.Cells(i, 1).Value
            
            If flagValue = "Îïûòíûé" Then
                If value <= percentilesExp(col, 1) Then
                    If greenCount > 0 Then
                        currentColumn.Cells(i, 1).Interior.Color = RGB(146, 208, 80)
                        greenCount = greenCount - 1
                    Else
                        If targetYellowCount > 0 Then
                            currentColumn.Cells(i, 1).Interior.Color = RGB(255, 255, 0)
                            targetYellowCount = targetYellowCount - 1
                        Else
                            currentColumn.Cells(i, 1).Interior.ColorIndex = xlNone
                        End If
                    End If
                ElseIf value >= percentilesExp(col, 2) Then
                    If redCount > 0 Then
                        currentColumn.Cells(i, 1).Interior.Color = RGB(255, 0, 0)
                        redCount = redCount - 1
                    Else
                        If targetYellowCount > 0 Then
                            currentColumn.Cells(i, 1).Interior.Color = RGB(255, 255, 0)
                            targetYellowCount = targetYellowCount - 1
                        Else
                            currentColumn.Cells(i, 1).Interior.ColorIndex = xlNone
                        End If
                    End If
                Else
                    If targetYellowCount > 0 Then
                        currentColumn.Cells(i, 1).Interior.Color = RGB(255, 255, 0)
                        targetYellowCount = targetYellowCount - 1
                    Else
                        currentColumn.Cells(i, 1).Interior.ColorIndex = xlNone
                    End If
                End If
            ElseIf flagValue = "Íîâè÷îê" Then
                If value <= percentilesNov(col, 1) Then
                    If greenCount > 0 Then
                        currentColumn.Cells(i, 1).Interior.Color = RGB(146, 208, 80)
                        greenCount = greenCount - 1
                    Else
                        If targetYellowCount > 0 Then
                            currentColumn.Cells(i, 1).Interior.Color = RGB(255, 255, 0)
                            targetYellowCount = targetYellowCount - 1
                        Else
                            currentColumn.Cells(i, 1).Interior.ColorIndex = xlNone
                        End If
                    End If
                ElseIf value >= percentilesNov(col, 2) Then
                    If redCount > 0 Then
                        currentColumn.Cells(i, 1).Interior.Color = RGB(255, 0, 0)
                        redCount = redCount - 1
                    Else
                        If targetYellowCount > 0 Then
                            currentColumn.Cells(i, 1).Interior.Color = RGB(255, 255, 0)
                            targetYellowCount = targetYellowCount - 1
                        Else
                            currentColumn.Cells(i, 1).Interior.ColorIndex = xlNone
                        End If
                    End If
                Else
                    If targetYellowCount > 0 Then
                        currentColumn.Cells(i, 1).Interior.Color = RGB(255, 255, 0)
                        targetYellowCount = targetYellowCount - 1
                    Else
                        currentColumn.Cells(i, 1).Interior.ColorIndex = xlNone
                    End If
                End If
            End If
        Next i
    Next col
End Sub


