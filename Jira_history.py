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
    
    Dim col As Long
    For col = 1 To columnCount
        Dim currentColumn As Range
        Set currentColumn = valuesRange.Columns(col)
        
        Dim flagCount As Long
        flagCount = rngFlags.areas.Count
        
        Dim percentile30() As Double, percentile70() As Double
        ReDim percentile30(1 To flagCount) As Double
        ReDim percentile70(1 To flagCount) As Double
        
        Dim flagIndex As Long
        For flagIndex = 1 To flagCount
            Dim flagRange As Range
            Set flagRange = rngFlags.areas(flagIndex)
            
            Dim percentile30_flag As Double, percentile70_flag As Double
            percentile30_flag = 0
            percentile70_flag = 0
            
            Dim row As Long
            For row = 1 To rowCount
                If flagRange.Cells(row, 1).value = "Опытный" Then
                    ProcessValue currentColumn.Cells(row), percentile30_flag, percentile70_flag
                End If
            Next row
            
            percentile30(flagIndex) = percentile30_flag
            percentile70(flagIndex) = percentile70_flag
        Next flagIndex
        
        Dim rowIndex As Long
        For rowIndex = 1 To rowCount
            Dim flagValue As String
            flagValue = rngFlags.Cells(rowIndex, 1).value
            
            Dim flagIndexToUse As Long
            For flagIndex = 1 To flagCount
                Dim flagRange1 As Range
                Set flagRange1 = rngFlags.areas(flagIndex)
                If flagRange1.Cells(1, 1).value = flagValue Then
                    flagIndexToUse = flagIndex
                    Exit For
                End If
            Next flagIndex
            
            If flagValue = "Опытный" Then
                ColorCell currentColumn.Cells(rowIndex), percentile30(flagIndexToUse), percentile70(flagIndexToUse)
            End If
        Next rowIndex
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
        cell.Interior.Color = RGB(146, 208, 80)
    ElseIf cell.value <= percentile30 Then
        cell.Interior.Color = RGB(255, 0, 0)
    Else
        cell.Interior.Color = RGB(255, 255, 0)
    End If
End Sub
