= Text.Combine(List.Select(Text.ToList(Text.From([Column1])), each not List.Contains(Text.ToList(Text.From([Column2])), _)), "")
