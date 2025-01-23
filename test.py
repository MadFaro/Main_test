let
    Источник = Oracle.Database("", [Query="select * from analytics.tolog_fcr_call_them", CreateNavigationProperties=false, CommandTimeout=#duration(0, 0, 5, 0)]),
    #"Измененный тип" = Table.TransformColumnTypes(Источник,{{"DT", type date}}),
    #"Добавлен пользовательский объект1" = Table.AddColumn(#"Измененный тип", "Неделя", each Date.ToText(Date.StartOfWeek([DT]), "dd")&"-"&Date.ToText(Date.EndOfWeek([DT]), "dd.MM")),
    #"Добавлен пользовательский объект2" = Table.AddColumn(#"Добавлен пользовательский объект1", "Месяц", each Date.ToText([DT], "yy")&"."&Date.ToText([DT],"MMM")),
    #"Добавлен пользовательский объект" = Table.AddColumn(#"Добавлен пользовательский объект2", "Группа", each if [PODRAZDELENIE] <> "Группа по работе с ключевыми клиентами" and [PODRAZDELENIE] <> "Группа сопровождения ипотечных сделок" then "Общая" else [PODRAZDELENIE]),
    #"Добавлен пользовательский объект3" = Table.AddColumn(#"Добавлен пользовательский объект", "Тематики брокер", each if [SUBJ1] = "Уралсиб Брокер" then 1 else if [SUBJ1] = "Твой Брокер" then 1 else 0)
in
    #"Добавлен пользовательский объект3"
