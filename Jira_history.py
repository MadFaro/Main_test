set App = createobject("excel.application")
App.visible = false
App.Workbooks.Open("C:\Users\TologonovAB\Desktop\Динамика показателей ДТ(рабочая версия).xlsx"),,,,,255 
App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").WorkSheets("Таблица").UsedRange.Value2 = App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").WorkSheets("Таблица").UsedRange.Value2 
App.Workbooks("Динамика показателей ДТ(рабочая версия).xlsx").SaveAs "C:\Users\TologonovAB\Desktop\Динамика показателей ДТ(рабочая версия) итог.xlsx" 
App.quit
