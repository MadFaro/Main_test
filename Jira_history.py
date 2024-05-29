Public Function EngsetB(Servers As Single, Events As Single, Intensity As Single) As Single
'Copyright © T&C Limited 1996, 1999
'The Engset B formula calculates the percentage likelyhood of the call
' being blocked, that is that all the trunks are in use and the caller
' will receive a busy signal. This uses the Engset model, based on the
' hindrance formula.
' Servers = Number of telephone lines
' Events = Number of calls
' Intensity = average intensity per call
Dim Val As Single, Last As Single, B As Single, Ev As Single
Dim Count As Long, MaxIterate As Long
On Error GoTo EngsetError
     If (Servers < 0) Or (Intensity < 0) Then
          EngsetB = 0
          Exit Function
     End If
     MaxIterate = Fix(Servers)
     Val = Intensity
     Ev = Events
     Last = 1  'for servers = 0
     For Count = 1 To MaxIterate
          B = (Last * (Count / ((Ev - Count) * Val))) + 1
          Last = B
     Next Count
EngsetExit:
     If B = 0 Then EngsetB = 0 Else EngsetB = MinMax((1 / B), 0, 1)
     Exit Function
     
EngsetError:
     B = 0
     Resume EngsetExit
End Function
'-----------------------------------------------------------------------
Public Function ErlangC(Servers As Single, Intensity As Single) As Single
'Copyright © T&C Limited 1996, 1999
'This formula gives the percentage likelyhood of the caller being
' placed in a queue.
' Servers = Number of agents
' Intensity = Arrival rate of calls / Completion rate of calls
'   Arrival rate = the number of calls arriving per hour
'   Completion rate = the number of calls completed per hour
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
