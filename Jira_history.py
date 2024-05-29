Public Function sla(Agents As Single, ServiceTime As Single, CallsPerHour As Single, AHT As Integer) As Single
    Dim BirthRate As Single, DeathRate As Single, TrafficRate As Single
    Dim Utilisation As Single, C As Single, SLQueued As Single
    Dim Server As Single
    On Error GoTo SLAError
    
    BirthRate = CallsPerHour
    DeathRate = 3600 / AHT  ' Количество секунд в часе
    TrafficRate = BirthRate / DeathRate
    Utilisation = TrafficRate / Agents
    
    ' Ограничение утилизации до 0.75
    If Utilisation > 0.75 Then
        Agents = TrafficRate / 0.75
        Utilisation = 0.75
    End If
    
    Server = Agents
    
    C = ErlangC(Server, TrafficRate)
    SLQueued = 1 - C * Exp(-((Server - TrafficRate) * ServiceTime / AHT))
    
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
