Sub PIK()
Application.DisplayAlerts = False
Dim lastrange, lastrange2 As Long
Dim i As Integer
Dim kniga, sh, name, shn As String
kniga = Sheets(1).Range("A2")
sh = Sheets(1).Range("B2")
name = Dir(kniga)
shn = Dir(sh)
Workbooks.Open (kniga), False, False, , , 255
Workbooks.Open (sh), False, True, , , 255
Workbooks(shn).Worksheets("Шаблон").Range(Cells(2, 1), Cells(Cells(Rows.Count, 1).End(xlUp).Row, 2)).Copy
Workbooks(name).Worksheets("Свод").Activate
Cells(Cells(Rows.Count, 1).End(xlUp).Row + 1, 1).PasteSpecial Paste:=12
Range(Cells(Cells(Rows.Count, 3).End(xlUp).Row, 3), Cells(Cells(Rows.Count, 3).End(xlUp).Row, 32)).AutoFill Destination:=Range(Cells(Cells(Rows.Count, 3).End(xlUp).Row, 3), Cells(Cells(Rows.Count, 3).End(xlUp).Row + 1, 32)), Type:=xlFillDefault
lastrange = Cells.SpecialCells(xlCellTypeFormulas, 3).Row
lastrange2 = Cells(Rows.Count, 3).End(xlUp).Row
Range(Cells(lastrange, 3), Cells(lastrange2 - 1, 32)).Copy
Range(Cells(lastrange, 3), Cells(lastrange2 - 1, 32)).PasteSpecial Paste:=xlPasteValuesAndNumberFormats
Range(Cells(lastrange2, 3), Cells(lastrange2, 32)).AutoFill Destination:=Range(Cells(lastrange2, 3), Cells(Cells(Rows.Count, 1).End(xlUp).Row, 32)), Type:=xlFillDefault
lastrange2 = Cells(Rows.Count, 1).End(xlUp).Row
Range(Cells(lastrange2, 1), Cells(lastrange2, 1)).NumberFormat = "[$-419]mmmm yyyy;@"
lastrange = Cells.SpecialCells(xlCellTypeFormulas, 3).Row
Range(Cells(lastrange, 1), Cells(lastrange2, 2)).HorizontalAlignment = xlCenter
Range(Cells(lastrange, 1), Cells(lastrange2, 2)).VerticalAlignment = xlCenter
Range(Cells(lastrange, 1), Cells(lastrange2, 2)).Borders.LineStyle = xlContinuous
Workbooks(shn).Activate
Workbooks(shn).Worksheets("Шаблон").Range(Cells(2, 1), Cells(Cells(Rows.Count, 1).End(xlUp).Row, 2)).Copy
Workbooks(name).Worksheets("Свод Страховка").Activate
Cells(Cells(Rows.Count, 1).End(xlUp).Row + 1, 1).PasteSpecial Paste:=12
Range(Cells(Cells(Rows.Count, 3).End(xlUp).Row, 3), Cells(Cells(Rows.Count, 3).End(xlUp).Row, 23)).AutoFill Destination:=Range(Cells(Cells(Rows.Count, 3).End(xlUp).Row, 3), Cells(Cells(Rows.Count, 3).End(xlUp).Row + 1, 23)), Type:=xlFillDefault
lastrange = Cells.SpecialCells(xlCellTypeFormulas, 3).Row
lastrange2 = Cells(Rows.Count, 3).End(xlUp).Row
Range(Cells(lastrange, 3), Cells(lastrange2 - 1, 23)).Copy
Range(Cells(lastrange, 3), Cells(lastrange2 - 1, 23)).PasteSpecial Paste:=xlPasteValuesAndNumberFormats
Range(Cells(lastrange2, 3), Cells(lastrange2, 23)).AutoFill Destination:=Range(Cells(lastrange2, 3), Cells(Cells(Rows.Count, 1).End(xlUp).Row, 23)), Type:=xlFillDefault
lastrange2 = Cells(Rows.Count, 1).End(xlUp).Row
Range(Cells(lastrange2, 1), Cells(lastrange2, 1)).NumberFormat = "[$-419]mmmm yyyy;@"
lastrange = Cells.SpecialCells(xlCellTypeFormulas, 3).Row
Range(Cells(lastrange, 1), Cells(lastrange2, 2)).HorizontalAlignment = xlCenter
Range(Cells(lastrange, 1), Cells(lastrange2, 2)).VerticalAlignment = xlCenter
Range(Cells(lastrange, 1), Cells(lastrange2, 2)).Borders.LineStyle = xlContinuous
Workbooks(name).Worksheets("Сотрудники(Дни)").Range("A3") = Date
Calculate
Workbooks(shn).Close False
Workbooks(name).Close True
Application.DisplayAlerts = True
Call KP
End Sub
