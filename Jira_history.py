
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav  

Private Function MinMax(Val As Single, Min As Single, Max As Single) As Single

    MinMax = Val
    If Val < Min Then MinMax = Min
    If Val > Max Then MinMax = Max
    
End Function
Public Function ErlangB(Servers As Single, Intensity As Single) As Single

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
Public Function ErlangC(Servers As Single, Intensity As Single) As Single

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
Public Function sla(Agents As Single, ServiceTime As Single, CallsPerHour As Single, AHT As Integer) As Single

Dim BirthRate As Single, DeathRate As Single, TrafficRate As Single
Dim Utilisation As Single, C As Single, SLQueued As Single
Dim Server As Single

On Error GoTo SLAError
     BirthRate = CallsPerHour
     DeathRate = 1800 / AHT
     TrafficRate = BirthRate / DeathRate
     Utilisation = TrafficRate / Agents
     If Utilisation >= 1 Then Utilisation = 0.99
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
