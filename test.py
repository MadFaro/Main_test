set app = createobject("excel.application")

app.visible = false
app.workbooks.open("C:\Users\TologonovAB\Desktop\DT\interim\interim.xlsx")
app.ActiveWorkbook.Connections("Запрос — Светофор").Refresh
app.workbooks("interim.xlsx").close(true)

app.quit
