Function ErlangC(Servers As Double, Intensity As Double) As Double
    Dim B As Double, C As Double
    Dim Count As Long
    
    If Servers <= 0 Or Intensity <= 0 Then
        ErlangC = 0
        Exit Function
    End If
    
    B = 1
    For Count = 1 To Servers
        B = B * (Intensity / Count)
    Next Count
    
    C = B / (WorksheetFunction.SumProduct(WorksheetFunction.Power(Intensity, Application.Transpose(Evaluate("row(1:" & Servers & ")"))) / WorksheetFunction.Fact(Application.Transpose(Evaluate("row(1:" & Servers & ")")))) + B)
    
    ErlangC = C
End Function

Function CalculateSL(CallsPerHour As Double, Agents As Double, Utilization As Double, AHT As Integer, SLTime As Integer) As Double
    Dim TrafficIntensity As Double
    Dim ErlangCValue As Double
    
    ' Расчет интенсивности трафика (Traffic Intensity)
    TrafficIntensity = CallsPerHour * AHT / 3600
    
    ' Расчет количества операторов (Agents)
    Agents = Application.WorksheetFunction.Ceiling(TrafficIntensity / Utilization, 1)
    
    ' Расчет Erlang C
    ErlangCValue = ErlangC(Agents, TrafficIntensity)
    
    ' Расчет SL
    CalculateSL = 1 - ErlangCValue * Exp(-SLTime / AHT)
End Function
