Private Function MinMax(Val As Single, Min As Single, Max As Single) As Single
'Apply minimum and maximum bounds to a value
    MinMax = Val
    If Val < Min Then MinMax = Min
    If Val > Max Then MinMax = Max
End Function
