Sub CombineColumnsToNewSheet()
    Dim wsSource As Worksheet
    Dim wsTarget As Worksheet
    Dim lastRow As Long
    Dim targetRow As Long
    Dim i As Long, j As Long
    
    ' Определяем исходный лист (первый лист)
    Set wsSource = ThisWorkbook.Sheets(1)
    
    ' Создаем новый лист и назначаем его целевым
    Set wsTarget = ThisWorkbook.Sheets.Add
    wsTarget.Name = "CombinedData" ' Можно указать любое имя
    
    targetRow = 1 ' Начало вставки данных в столбец A на новом листе
    
    ' Определяем последний заполненный столбец на исходном листе
    lastCol = wsSource.Cells(1, wsSource.Columns.Count).End(xlToLeft).Column
    
    ' Проходим по всем заполненным столбцам через один
    For i = 1 To lastCol Step 2
        ' Определяем последнюю заполненную строку в текущем столбце
        lastRow = wsSource.Cells(wsSource.Rows.Count, i).End(xlUp).Row
        
        ' Копируем данные из текущего столбца на новый лист в столбец A
        For j = 1 To lastRow
            wsTarget.Cells(targetRow, 1).Value = wsSource.Cells(j, i).Value
            targetRow = targetRow + 1
        Next j
    Next i
End Sub

