Function ErlangC(Servers As Double, Intensity As Double) As Double
    Dim B As Double, C As Double
    Dim Count As Long
    Dim Numbers() As Double
    
    If Servers <= 0 Or Intensity <= 0 Then
        ErlangC = 0
        Exit Function
    End If
    
    ReDim Numbers(1 To Servers)
    For Count = 1 To Servers
        Numbers(Count) = Count
    Next Count
    
    B = 1
    For Count = 1 To Servers
        B = B * (Intensity / Numbers(Count))
    Next Count
    
    Dim PowerArray() As Double
    Dim FactArray() As Double
    ReDim PowerArray(1 To Servers)
    ReDim FactArray(1 To Servers)
    
    For Count = 1 To Servers
        PowerArray(Count) = Intensity
        FactArray(Count) = Count
    Next Count
    
    C = B / (WorksheetFunction.SumProduct(PowerArray) / WorksheetFunction.SumProduct(FactArray) + B)
    
    ErlangC = C
End Function
