
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)


Sub РасставитьПерерывыСИспользованиемSolver()
    Dim ws As Worksheet
    Dim lastRow As Long, lastCol As Long
    Dim i As Long, j As Long
    Dim OperatorRange As Range
    Dim SolverApp As Object
    
    ' Указываем имя вашего листа
    Set ws = ThisWorkbook.Sheets("Лист1") ' Замените "Лист1" на имя вашего листа
    
    ' Находим последнюю заполненную строку и столбец
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
    
    ' Определение диапазона переменных Solver (все ячейки с 1)
    Set OperatorRange = ws.Range(ws.Cells(2, 2), ws.Cells(lastRow, lastCol))
    
    ' Создаем объект Solver
    Set SolverApp = Application.Solver
    
    ' Настройка параметров Solver
    SolverApp.SolverReset
    SolverApp.SolverOk SetCell:=OperatorRange, MaxMinVal:=2, ValueOf:=0, ByChange:=OperatorRange, Engine:=1, EngineDesc:="Simplex LP"
    SolverApp.SolverAdd CellRef:=OperatorRange, Relation:=1, FormulaText:=1 ' Ограничение на значения (должны быть 1 или 0)
    SolverApp.SolverOptions AssumeNonNeg:=True
    SolverApp.SolverSolve UserFinish:=True
    
    ' Присваиваем -1 там, где Solver решение указало на 1
    For i = 1 To lastRow - 1
        For j = 1 To lastCol - 1
            If OperatorRange.Cells(i, j).Value = 1 Then
                ws.Cells(i + 1, j + 1).Value = -1
            End If
        Next j
    Next i
    
    ' Освобождаем ресурсы Solver
    Set SolverApp = Nothing
End Sub
