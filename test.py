let
    Источник = Oracle.Database("", [Query="SELECT * FROM analytics.tolog_call_evaluations_scores", CreateNavigationProperties=false]),
    #"Измененный тип" = Table.TransformColumnTypes(Источник,{{"DTM", type date}}),
    #"Добавлен пользовательский объект" = Table.AddColumn(#"Измененный тип", "Группа", each if [DESCRIPTION] = "ДДО АктивКредит" or 
[DESCRIPTION] = "ДДО Группа 1" or 
[DESCRIPTION] = "ДДО Группа 2" or 
[DESCRIPTION] = "ДДО Группа 5" or 
[DESCRIPTION] = "ДДО Группа 8" or 
[DESCRIPTION] = "ДДО Группа 9" or 
[DESCRIPTION] = "ДДО Группа 10" or
[DESCRIPTION] = "ДДО Группа 11" or
[DESCRIPTION] = "ДДО Группа 12" or
[DESCRIPTION] = "ДДО Группа 13" or
[DESCRIPTION] = "ДДО Группа 14"
then "Общая" else if 
[DESCRIPTION] = "ДДО Премиум" and ([FIRSTNAME] <> "Шекеринская Екатерина Евгеньевна" and [FIRSTNAME] <> "Сатарова Сайера Алиевна" and [FIRSTNAME] <> "Максимов Дмитрий Владимирович") then "Премиум" else [DESCRIPTION]),
    #"Добавлен пользовательский объект1" = Table.AddColumn(#"Добавлен пользовательский объект", "Неделя", each Date.ToText(Date.StartOfWeek([DTM]), "dd")&"-"&Date.ToText(Date.EndOfWeek([DTM]), "dd.MM")),
    #"Добавлен пользовательский объект2" = Table.AddColumn(#"Добавлен пользовательский объект1", "Месяц", each Date.ToText([DTM], "yy")& "." &Date.ToText([DTM], "MMM"))
in
    #"Добавлен пользовательский объект2"
