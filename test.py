let
    Источник = Oracle.Database("bd", [HierarchicalNavigation=true, Query="select trunc(a.DATE_) as DATETIME, b.DESCRIPTION, b.FULLNAME, coalesce(a.CREDITFLOW, 0) as CREDITFLOW,#(lf)sum(b.LOGGEDONTIME) as LOGGEDONTIME, sum(b.TALKTIME) as TALKTIME,#(lf)sum(b.HOLDTIME) as HOLDTIME,#(lf)sum(b.WRAPTIME) as WRAPTIME, sum(b.AVAILTIME) as AVAILTIME, #(lf)sum(b.RESERVEDTIME) as RESERVEDTIME, sum(b.CALLSHANDLED) as CALLSHANDLED,#(lf)sum(b.HANDLEDCALLSTIME) as HANDLEDCALLSTIME, sum(b.ANSWERWAITTIME) as ANSWERWAITTIME,#(lf)sum(b.CALLSANSWERED) as CALLSANSWERED#(lf)from ANALYTICS.TOLOG_CISCO_OPERATOR_STATE a#(lf)left join ANALYTICS.CISCO_OPERATOR b on a.OPERATOR_ = SUBSTR(b.FULLNAME, INSTR(b.FULLNAME, ', ') + 2) and a.DATE_ = trunc(b.DATETIME)#(lf)where b.DESCRIPTION like '%ДДО%' and DATETIME>= trunc(add_months(sysdate,-6), 'mm')#(lf)group by trunc(a.DATE_), b.DESCRIPTION, b.FULLNAME, a.CREDITFLOW"]),
    #"Сортированные строки" = Table.Sort(Источник,{{"DATETIME", Order.Ascending}}),
    #"Измененный тип" = Table.TransformColumnTypes(#"Сортированные строки",{{"DATETIME", type date}}),
    #"Замененное значение" = Table.ReplaceValue(#"Измененный тип","ДДО Брокер","ДДО Премиум",Replacer.ReplaceText,{"DESCRIPTION"}),
    #"Сгруппированные строки" = Table.Group(#"Замененное значение", {"DATETIME", "DESCRIPTION", "FULLNAME"}, {{"LOGGEDONTIME", each List.Sum([LOGGEDONTIME]), type number}, {"TALKTIME", each List.Sum([TALKTIME]), type number}, {"HOLDTIME", each List.Sum([HOLDTIME]), type number}, {"WRAPTIME", each List.Sum([WRAPTIME]), type number}, {"AVAILTIME", each List.Sum([AVAILTIME]), type number}, {"RESERVEDTIME", each List.Sum([RESERVEDTIME]), type number}, {"CALLSHANDLED", each List.Sum([CALLSHANDLED]), type number}, {"HANDLEDCALLSTIME", each List.Sum([HANDLEDCALLSTIME]), type number}, {"ANSWERWAITTIME", each List.Sum([ANSWERWAITTIME]), type number}, {"CALLSANSWERED", each List.Sum([CALLSANSWERED]), type number}, {"CREDITFLOW", each List.Sum([CREDITFLOW]), type number}}),
    #"Добавлен пользовательский объект1" = Table.AddColumn(#"Сгруппированные строки", "Неделя", each Date.ToText(Date.StartOfWeek([DATETIME]), "dd")&"-"&Date.ToText(Date.EndOfWeek([DATETIME]), "dd.MM")),
    #"Добавлен пользовательский объект2" = Table.AddColumn(#"Добавлен пользовательский объект1", "Месяц", each Date.ToText([DATETIME], "yy")& "." &Date.ToText([DATETIME], "MMM")),
    #"Добавлен пользовательский объект" = Table.AddColumn(#"Добавлен пользовательский объект2", "Фильтр", each "Да"),
    #"Добавлен пользовательский объект3" = Table.AddColumn(#"Добавлен пользовательский объект", "Группа", each if [DESCRIPTION] = "ДДО АктивКредит" or 
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
[DESCRIPTION] = "ДДО Премиум" and ([FULLNAME] <> "11317, Шекеринская Екатерина Евгеньевна" and [FULLNAME] <> "12288, Сатарова Сайера Алиевна" and [FULLNAME] <> "12296, Максимов Дмитрий Владимирович") then "Премиум" else [DESCRIPTION]),
    #"Переупорядоченные столбцы" = Table.ReorderColumns(#"Добавлен пользовательский объект3",{"DATETIME", "DESCRIPTION", "FULLNAME", "LOGGEDONTIME", "TALKTIME", "HOLDTIME", "WRAPTIME", "AVAILTIME", "RESERVEDTIME", "CALLSHANDLED", "HANDLEDCALLSTIME", "ANSWERWAITTIME", "CALLSANSWERED", "Неделя", "Месяц", "Фильтр", "Группа", "CREDITFLOW"})
in
    #"Переупорядоченные столбцы"
