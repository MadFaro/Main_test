Error starting at line : 1 in command -
create table analytics.tolog_lights_bi_ddo as
with tab_1 as (
select * from (
select TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, TYPE_CODE
FROM ANALYTICS.TOLOG_LIGHTS_FINALLY
where MONTH >= add_months(trunc(sysdate, 'mm'), -1))),
tab_2 as (
select TO_CHAR("ENameFull") as FIO,  TO_CHAR("Department") as DEP from USB_FNS_LOADER.KO_AD_BK_NIGHT
where DEP_ID_L3='40050455' 
AND "StateNP"=1 
AND "StateAD"=1 
AND "Title" = 'Руководитель группы' 
AND "Element_BP" in ('Контакт-центр: входящая линия') --'Телемаркетинг: исходящая линия',
union all
select 
TO_CHAR('Хвуст Владислав Валерьевич') as FIO,  
TO_CHAR('Группа №10') as DEP 
from dual
),
tab_3 as (
select 
a.MONTH,
tab_1.TABNUM as TABNUM, tab_1.FIO as FIO, tab_1.DOLZHHNOST as DOLZHHNOST, 
case when tab_1.PODRAZDELENIE = 'Группа сопровождения ипотечных сделок' then 'Ипотека'
when tab_1.PODRAZDELENIE = 'Группа по работе с ключевыми клиентами' then 'Вип' else tab_1.PODRAZDELENIE end as PODRAZDELENIE, tab_1.STAG as STAG, tab_1.DIRECT as DIRECT,
cast(tab_2.FIO as varchar2(300)) as RG,
a.STATUS, tab_1.TYPE_CODE as TYPE_CODE, 
a.SALES, a.ATT, a.CSI, a.SCORE, 
a.DISCIPLINE, a.TEST, a.SUM, 
a.RANK_SALES, a.RANK_ATT, a.RANK_CSI, 
a.RANK_SCORE, a.RANK_DISCIPLINE, 
a.RANK_TEST, a.RANK_SUM
FROM ANALYTICS.TOLOG_LIGHTS_FINALLY a
left join tab_1 on a.TABNUM = tab_1.TABNUM
left join tab_2 on tab_1.PODRAZDELENIE = tab_2.DEP
where MONTH >= add_months(trunc(sysdate, 'mm'), -3) and tab_1.TABNUM is not null)
select 
MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, MARK, 
case when MARK_RANK = 1 then 'Зеленая зона' 
when MARK_RANK = 2 then 'Желтая зона' else 'Красная зона' end as MARK_RANK
from (
select
'Кредиты' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, SALES as MARK, RANK_SALES as MARK_RANK
from tab_3
union all
select
'Холд от ATT' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, ATT as MARK, RANK_ATT as MARK_RANK
from tab_3
union all
select
'CSI' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, CSI as MARK, RANK_CSI as MARK_RANK
from tab_3
union all
select
'Качество' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, SCORE as MARK, RANK_SCORE as MARK_RANK
from tab_3
union all
select
'Дисциплина' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, DISCIPLINE as MARK, RANK_DISCIPLINE as MARK_RANK
from tab_3
union all
select
'Тест' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, TEST as MARK, RANK_TEST as MARK_RANK
from tab_3
union all
select
'Итоговый' as MARK_TYPE,
MONTH, TABNUM, FIO, DOLZHHNOST, PODRAZDELENIE, STAG, DIRECT, RG, STATUS, TYPE_CODE, SUM as MARK, RANK_SUM as MARK_RANK
from tab_3)
Error report -
ORA-00997: неверное использование типа данных LONG
00997. 00000 -  "illegal use of LONG datatype"
*Cause:    
*Action:
