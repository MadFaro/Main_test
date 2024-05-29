Public Function ErlangB(Servers As Single, Intensity As Single) As Single
'Copyright © T&C Limited 1996, 1999
'The Erlang B formula calculates the percentage likelyhood of the call
' being blocked, that is that all the trunks are in use and the caller
' will receive a busy signal.
' Servers = Number of telephone lines
' Intensity = Arrival rate of calls / Completion rate of calls
'   Arrival rate = the number of calls arriving per hour
'   Completion rate = the number of calls completed per hour
Dim Val As Single, Last As Single, B As Single
Dim Count As Long, MaxIterate As Long
On Error GoTo ErlangBError
     If (Servers < 0) Or (Intensity < 0) Then
          ErlangB = 0
          Exit Function
     End If
     MaxIterate = Fix(Servers)
     Val = Intensity
     Last = 1 ' for server = 0
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
