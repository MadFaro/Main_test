select cast("ENameFull" as varchar2(100)) as FIO,  cast("Department" as varchar2(100)) as DEP from USB_FNS_LOADER.KO_AD_BK_NIGHT
where DEP_ID_L3='40050455' 
AND "StateNP"=1 
AND "StateAD"=1 
AND "Title" = 'Руководитель группы' 
AND "Element_BP" in ('Контакт-центр: входящая линия') --'Телемаркетинг: исходящая линия',
union
select
'Хвуст Владислав Валерьевич' as FIO, 
'Группа №10' as DEP from dual
