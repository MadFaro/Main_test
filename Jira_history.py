Public Function sla(Agents As Single, ServiceTime As Single, CallsPerHour As Single, AHT As Integer) As Single
'Copyright © T&C Limited 1996, 1999, 2001
'Calculate the service level achieved for the given number of agents
' Agents is the number of agents available
' ServiceTime is target answer time in seconds e.g. 15
' CallsPerHour is the number of calls received in one hour period
' AHT (Average handle time) is the call duration including after call work in seconds  e.g 180
Dim BirthRate As Single, DeathRate As Single, TrafficRate As Single
Dim Utilisation As Single, C As Single, SLQueued As Single
Dim Server As Single
On Error GoTo SLAError

     BirthRate = CallsPerHour
     DeathRate = 1800 / AHT
'calculate the traffic intensity
     TrafficRate = BirthRate / DeathRate
     Utilisation = TrafficRate / Agents
     If Utilisation >= 1 Then Utilisation = 0.99
     Server = Agents
     C = ErlangC(Server, TrafficRate)
'now calculate SLA % as those not queuing plus those queuing
'revised formula with thanks to Tim Bolte and Jшrn Lodahl for their input
     SLQueued = 1 - C * Exp((TrafficRate - Server) * ServiceTime / AHT)

SLAExit:
     sla = MinMax(SLQueued, 0, 1)
     Exit Function
     
SLAError:
    SLQueued = 0
    Resume SLAExit

End Function
