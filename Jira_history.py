= Text.Combine(List.Select(Text.ToList([Column1]), each not List.Contains(Text.ToList([Column2]), _)), "")
