set App = createobject("excel.application")

App.visible = false
App.Workbooks.Open("C:\Users\TologonovAB\Desktop\Динамика показателей ДТ(рабочая версия).xlsx"),,,,,255
'App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").RefreshAll
'App.Calculate
App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").Cells.Select
App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").Cells.Copy
App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").Cells.Selection.PasteSpecial Paste:=xlPasteValuesAndNumberFormats
App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").SaveAs "C:\Users\TologonovAB\Desktop\Динамика показателей ДТ(рабочая версия) итог.xlsx"
App.quit
