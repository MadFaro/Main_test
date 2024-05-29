Function sla(Agents As Single, ServiceTime As Single, CallsPerHour As Single, AHT As Integer) As Single
    Dim BirthRate As Single, DeathRate As Single, TrafficRate As Single
    Dim Utilisation As Single, C As Single, SLQueued As Single
    Dim Server As Single
    On Error GoTo SLAError

    BirthRate = CallsPerHour
    DeathRate = 1800 / AHT
    TrafficRate = BirthRate / DeathRate
    
    ' Расчет утилизации с ограничением до 0.85
    Utilisation = TrafficRate / Agents
    If Utilisation > 0.85 Then Utilisation = 0.85
    
    Server = Agents
    C = ErlangC(Server, TrafficRate)
    SLQueued = 1 - C * Exp((TrafficRate - Server) * ServiceTime / AHT)

SLAExit:
    sla = MinMax(SLQueued, 0, 1)
    Exit Function

SLAError:
    SLQueued = 0
    Resume SLAExit
End Function
