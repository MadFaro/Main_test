Sub QuickSort(arr() As Double, ByVal left As Long, ByVal right As Long)
    Dim i As Long
    Dim j As Long
    Dim pivot As Double
    Dim temp As Double
    
    i = left
    j = right
    
    If left >= right Then Exit Sub ' Дополнительная проверка, если left >= right
    
    If left + 1 = right Then
        If arr(left) > arr(right) Then
            temp = arr(left)
            arr(left) = arr(right)
            arr(right) = temp
        End If
        Exit Sub
    End If
    
    pivot = arr((left + right) \ 2)
    
    While i <= j
        While arr(i) < pivot
            i = i + 1
        Wend
        While arr(j) > pivot
            j = j - 1
        Wend
        If i <= j Then
            temp = arr(i)
            arr(i) = arr(j)
            arr(j) = temp
            i = i + 1
            j = j - 1
        End If
    Wend
    
    If left < j Then QuickSort arr, left, j
    If i < right Then QuickSort arr, i, right
End Sub

