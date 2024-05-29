Public Function sla(CallsPerHour As Single, AHT As Integer, ServiceTime As Single) As Single
    Dim BirthRate As Single, DeathRate As Single, TrafficRate As Single
    Dim Utilisation As Single, C As Single, SLQueued As Single
    Dim Agents As Single, MinAgents As Single
    On Error GoTo SLAError

    BirthRate = CallsPerHour
    DeathRate = 3600 / AHT  ' Количество секунд в часе
    TrafficRate = BirthRate * AHT / 3600  ' Преобразуем AHT в часы для расчета TrafficRate

    ' Рассчитываем минимальное количество операторов для соблюдения утилизации <= 0.75
    MinAgents = TrafficRate / 0.75
    Agents = Application.WorksheetFunction.Ceiling(MinAgents, 1)  ' Округляем до целого числа вверх

    ' Пересчитываем утилизацию с новым количеством операторов
    Utilisation = TrafficRate / Agents

    C = ErlangC(Agents, TrafficRate)
    SLQueued = 1 - C * Exp(-((Agents - TrafficRate) * ServiceTime / AHT))

SLAExit:
    sla = MinMax(SLQueued, 0, 1)
    Exit Function
SLAError:
    SLQueued = 0
    Resume SLAExit
End Function

Private Function ErlangB(Servers As Single, Intensity As Single) As Single
    Dim Val As Single, Last As Single, B As Single
    Dim Count As Long, MaxIterate As Long
    On Error GoTo ErlangBError

    If (Servers < 0) Or (Intensity < 0) Then
        ErlangB = 0
        Exit Function
    End If

    MaxIterate = Fix(Servers)
    Val = Intensity
    Last = 1

    For Count = 1 To MaxIterate
        B = (Val * Last) / (Count + (Val * Last))
        Last = B
    Next Count

ErlangBExit:
    ErlangB = MinMax(B, 0, 1)
    Exit Function
ErlangBError:
    B = 0
    Resume ErlangBExit
End Function

Private Function ErlangC(Servers As Single, Intensity As Single) As Single
    Dim B As Single, C As Single
    Dim Count As Long, MaxIterate As Long
    On Error GoTo ErlangCError

    If (Servers < 0) Or (Intensity < 0) Then
        ErlangC = 0
        Exit Function
    End If

    B = ErlangB(Servers, Intensity)
    C = B / (((Intensity / Servers) * B) + (1 - (Intensity / Servers)))

ErlangCExit:
    ErlangC = MinMax(C, 0, 1)
    Exit Function
ErlangCError:
    C = 0
    Resume ErlangCExit
End Function

Private Function MinMax(Val As Single, Min As Single, Max As Single) As Single
    MinMax = Val
    If Val < Min Then MinMax = Min
    If Val > Max Then MinMax = Max
End Function
