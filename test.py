let
    Источник = Oracle.Database("bd", [HierarchicalNavigation=true, Query="select * from ANALYTICS.CISCO_SL_TABLE#(lf)Where INTERV >= trunc(add_months(sysdate,-6), 'mm') and ENTERPRISENAME <> 'CCM_PG_1.SG_TLM_RetentionUnit'"]),
    #"Измененный тип" = Table.TransformColumnTypes(Источник,{{"INTERV", type date}}),
    #"Сгруппированные строки" = Table.Group(#"Измененный тип", {"INTERV", "ENTERPRISENAME"}, {{"ANS1", each List.Sum([ANS1]), type number}, {"ANS2", each List.Sum([ANS2]), type number}, {"ANS3", each List.Sum([ANS3]), type number}, {"ANS4", each List.Sum([ANS4]), type number}, {"ANS5", each List.Sum([ANS5]), type number}, {"ANS6", each List.Sum([ANS6]), type number}, {"ANS7", each List.Sum([ANS7]), type number}, {"ANS8", each List.Sum([ANS8]), type number}, {"ANS9", each List.Sum([ANS9]), type number}, {"ANS10", each List.Sum([ANS10]), type number}, {"ABAN1", each List.Sum([ABAN1]), type number}, {"ABAN2", each List.Sum([ABAN2]), type number}, {"ABAN3", each List.Sum([ABAN3]), type number}, {"ABAN4", each List.Sum([ABAN4]), type number}, {"ABAN5", each List.Sum([ABAN5]), type number}, {"ABAN6", each List.Sum([ABAN6]), type number}, {"ABAN7", each List.Sum([ABAN7]), type number}, {"ABAN8", each List.Sum([ABAN8]), type number}, {"ABAN9", each List.Sum([ABAN9]), type number}, {"ABAN10", each List.Sum([ABAN10]), type number}}),
    #"Добавлен пользовательский объект" = Table.AddColumn(#"Сгруппированные строки", "Месяц год", each Date.ToText([INTERV], "yy")& "." &Date.ToText([INTERV], "MMM")),
    #"Добавлен пользовательский объект1" = Table.AddColumn(#"Добавлен пользовательский объект", "Неделя", each Date.ToText(Date.StartOfWeek([INTERV]), "dd")&"-"&Date.ToText(Date.EndOfWeek([INTERV]), "dd.MM")),
    #"Добавлен пользовательский объект2" = Table.AddColumn(#"Добавлен пользовательский объект1", "Группа", each if [ENTERPRISENAME] = "CCM_PG_1.SG_DDO_ActiveCredit" or
[ENTERPRISENAME] = "CCM_PG_1.SG_DDO_CityBank" or 
[ENTERPRISENAME] = "CCM_PG_1.SG_Operator" or 
[ENTERPRISENAME] = "CCM_PG_1.SG_Operator_1" or 
[ENTERPRISENAME] = "CCM_PG_1.SG_Operator_2" or 
[ENTERPRISENAME] = "CCM_PG_1.SG_Operator_3" or 
[ENTERPRISENAME] = "CCM_PG_1.SG_Operator_4" or 
[ENTERPRISENAME] = "CCM_PG_1.SG_Operator_5" or
[ENTERPRISENAME] = "CCM_PG_1.SG_DDO_T_Bank"
then "All" else [ENTERPRISENAME]),
    #"Вставлено: сумма" = Table.AddColumn(#"Добавлен пользовательский объект2", "income_call", each List.Sum({[ANS1], [ANS2], [ANS3], [ANS4], [ANS5], [ANS6], [ANS7], [ANS8], [ANS9], [ANS10], [ABAN1], [ABAN2], [ABAN3], [ABAN4], [ABAN5], [ABAN6], [ABAN7], [ABAN8], [ABAN9], [ABAN10]}), type number),
    #"Вставлено: сумма1" = Table.AddColumn(#"Вставлено: сумма", "lost_call", each List.Sum({[ABAN1], [ABAN2], [ABAN3], [ABAN4], [ABAN5], [ABAN6], [ABAN7], [ABAN8], [ABAN9], [ABAN10]}), type number),
    #"Добавлен пользовательский объект3" = Table.AddColumn(#"Вставлено: сумма1", "lost_call_5_sec", each [lost_call]-[ABAN1]),
    #"Вставлено: сумма2" = Table.AddColumn(#"Добавлен пользовательский объект3", "Sl_ans", each List.Sum({[ANS1], [ANS2], [ANS3]}), type number),
    #"Добавлен пользовательский объект4" = Table.AddColumn(#"Вставлено: сумма2", "income_call_5_sec", each [income_call]-[ABAN1])
in
    #"Добавлен пользовательский объект4"
