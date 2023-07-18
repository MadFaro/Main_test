Sub color_value_rating()
    Dim rngFlags As Range
    Dim rngValues As Range
    
    Dim selectedRange As Range
    Set selectedRange = Selection
    
    ' Определение диапазона флагов
    Set rngFlags = selectedRange.areas(1).Columns(1)
    
    ' Определение диапазона значений
    Dim valuesRange As Range
    If selectedRange.areas.Count > 1 Then
        Set valuesRange = selectedRange.areas(2)
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
            flagValue1 = rngFlags.Cells(row, 1).value
            
            If flagValue1 = "Опытный" Then
                ColorCell currentColumn1.Cells(row), percentiles(col, 1), percentiles(col, 2)
            ElseIf flagValue1 = "Новичок" Then
                ColorCell currentColumn1.Cells(row), percentiles(col, 1), percentiles(col, 2)
            End If
        Next row
    Next col
End Sub

Sub ColorCell(ByVal cell As Range, ByVal percentile30 As Double, ByVal percentile70 As Double)
    If cell.value >= percentile70 Then
        cell.Interior.Color = RGB(146, 208, 80) ' Зеленый
    ElseIf cell.value <= percentile30 Then
        cell.Interior.Color = RGB(255, 0, 0) ' Красный
    Else
        cell.Interior.Color = RGB(255, 255, 0) ' Желтый
    End If
End Sub
