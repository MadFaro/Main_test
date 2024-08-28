Sub CombineColumnsFromMultipleSheetsWithSource()
    Dim wsSource As Worksheet
    Dim wsTarget As Worksheet
    Dim lastRow As Long
    Dim targetRow As Long
    Dim lastCol As Long
    Dim i As Long, j As Long
    
    ' Создаем новый лист и назначаем его целевым
    Set wsTarget = ThisWorkbook.Sheets.Add
    wsTarget.Name = "CombinedData" ' Можно указать любое имя для нового листа
    
    targetRow = 1 ' Начало вставки данных в столбец A на новом листе
    
    ' Добавляем заголовки
    wsTarget.Cells(1, 1).Value = "Data"
    wsTarget.Cells(1, 2).Value = "Sheet Name"
    targetRow = targetRow + 1
    
    ' Проходим по всем исходным листам
    For Each wsSource In ThisWorkbook.Sheets(Array("Провайдер 1", "Провайдер 2", "Провайдер 3"))
        
        ' Определяем последний заполненный столбец на текущем листе
        lastCol = wsSource.Cells(1, wsSource.Columns.Count).End(xlToLeft).Column
        
        ' Проходим по всем заполненным столбцам через один
        For i = 1 To lastCol Step 2
            ' Определяем последнюю заполненную строку в текущем столбце
            lastRow = wsSource.Cells(wsSource.Rows.Count, i).End(xlUp).Row
            
            ' Копируем данные из текущего столбца на новый лист в столбец A
            For j = 1 To lastRow
                wsTarget.Cells(targetRow, 1).Value = wsSource.Cells(j, i).Value
                wsTarget.Cells(targetRow, 2).Value = wsSource.Name ' Указываем название исходного листа
                targetRow = targetRow + 1
            Next j
        Next i
    Next wsSource
End Sub
