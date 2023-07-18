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
    
    Dim percentile30() As Double, percentile70() As Double
    ReDim percentile30(1 To columnCount, 1 To 2) As Double
    ReDim percentile70(1 To columnCount, 1 To 2) As Double
    
    Dim col As Long
    For col = 1 To columnCount
        Dim currentColumn As Range
        Set currentColumn = valuesRange.Columns(col)
        
        Dim percentile30_flag1 As Double, percentile70_flag1 As Double
        Dim percentile30_flag2 As Double, percentile70_flag2 As Double
        percentile30_flag1 = 0
        percentile70_flag1 = 0
        percentile30_flag2 = 0
        percentile70_flag2 = 0
        
        Dim row As Long
        For row = 1 To rowCount
            Dim flagValue As String
            flagValue = rngFlags.Cells(row, 1).value
            
            If flagValue = "Опытный" Then
                ProcessValue currentColumn.Cells(row), percentile30_flag1, percentile70_flag1
            ElseIf flagValue = "Новичок" Then
                ProcessValue currentColumn.Cells(row), percentile30_flag2, percentile70_flag2
            End If
        Next row
        
        percentile30(col, 1) = percentile30_flag1
        percentile70(col, 1) = percentile70_flag1
        percentile30(col, 2) = percentile30_flag2
        percentile70(col, 2) = percentile70_flag2
    Next col
    
    For col = 1 To columnCount
        Dim currentColumn1 As Range
        Set currentColumn1 = valuesRange.Columns(col)
        
        For row = 1 To rowCount
            Dim flagValue1 As String
            flagValue1 = rngFlags.Cells(row, 1).value
            
            If flagValue1 = "Опытный" Then
                ColorCell currentColumn1.Cells(row), percentile30(col, 1), percentile70(col, 1)
            ElseIf flagValue1 = "Новичок" Then
                ColorCell currentColumn1.Cells(row), percentile30(col, 2), percentile70(col, 2)
            End If
        Next row
    Next col
End Sub

Sub ProcessValue(ByVal cell As Range, ByRef percentile30 As Double, ByRef percentile70 As Double)
    If Not IsEmpty(cell) Then
        If percentile30 = 0 Then
            percentile30 = cell.value
            percentile70 = cell.value
        Else
            If cell.value < percentile30 Then
                percentile30 = cell.value
            ElseIf cell.value > percentile70 Then
                percentile70 = cell.value
            End If
        End If
    End If
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
