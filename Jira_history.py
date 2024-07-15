= Text.Combine(List.Select(Text.ToList([Column1]), each not Text.Contains([Column2], _)), "")

