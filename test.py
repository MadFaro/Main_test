select 
MAX(TYPE) KEEP (DENSE_RANK LAST ORDER BY DATE_CREATED) AS TYPE, 
MAX(DATE_CREATED) AS DATE_CREATED, 
MAX(ID) KEEP (DENSE_RANK LAST ORDER BY DATE_CREATED) AS ID, 
CLIENT_FIO, 
CLIENT_DID,
MAX(IBSO_ID_OR_CALLED_FROM_NUM) KEEP (DENSE_RANK LAST ORDER BY DATE_CREATED) AS IBSO_ID_OR_CALLED_FROM_NUM, 
CARD_TYPE,
MAX(HAVE_REDIRECT) AS HAVE_REDIRECT,
MAX(MONEY) AS MONEY from (
select TYPE, DATE_CREATED, ID, CLIENT_FIO, CLIENT_DID, IBSO_ID_OR_CALLED_FROM_NUM, CARD_TYPE, HAVE_REDIRECT, MONEY from (
select
''Чаты'' as TYPE, CREATED as DATE_CREATED, THREADID as ID, CLIENT_NAME as CLIENT_FIO, CLIENT_DID,
CLIENT_IBSO_ID as IBSO_ID_OR_CALLED_FROM_NUM,
ROW_NUMBER() OVER (PARTITION BY THREADID ORDER BY CREATED desc) as RN,
case when
SUBCATEGORY IS NULL and CATEGORY IS NULL THEN ''Не определено''
when (SUBCATEGORY in (''РБ_Закрытие_ДейстПотреб'',''РБ_Закрытие_Прибыль'',''РБ_Закрытие_МИР'',''РБ_Закрытие_Эконом'',''Дебетовые карты'') 
or CATEGORY in (''РБ_Закрытие_ДейстПотреб'',''РБ_Закрытие_Прибыль'',''РБ_Закрытие_МИР'',''РБ_Закрытие_Эконом'',''Дебетовые карты'') 
or lower(SUBCATEGORY) like ''%дебет%'' or lower(CATEGORY) like ''%дебет%'') then ''Дебетовая карта'' 
when (SUBCATEGORY in (''РБ_Закрытие_120'',''РБ_Закрытие_кредитная карта с кэшбеком'',''РБ_Закрытие_ДейстКК'',''РБ_Закрытие_КК MIR Supreme'',''РБ_Закрытие_КЦ_СКБ'',''Кредитные карты'') 
or CATEGORY in (''РБ_Закрытие_120'',''РБ_Закрытие_кредитная карта с кэшбеком'',''РБ_Закрытие_ДейстКК'',''РБ_Закрытие_КК MIR Supreme'',''РБ_Закрытие_КЦ_СКБ'',''Кредитные карты'') 
or lower(SUBCATEGORY) like ''%кредит%'' or lower(CATEGORY) like ''%кредит%'') then ''Кредитная карта'' else ''Не определено'' end as card_type,
HAVE_REDIRECT,
0 as MONEY
from ANALYTICS.TOLOG_RETENTIONS_CHATS_TABLE
where client_did is not null)
union all
select TYPE, DATE_CREATED, ID, CLIENT_FIO, CLIENT_DID, IBSO_ID_OR_CALLED_FROM_NUM, CARD_TYPE, HAVE_REDIRECT, MONEY from (
select 
''Звонки'' as Type,
a.dt - INTERVAL ''2'' HOUR as DATE_CREATED,
cast(a.call_id as number) as ID, 
a.FIO as CLIENT_FIO,
d.CLIENT_DID,
a.CALLED_FROM_NUM as IBSO_ID_OR_CALLED_FROM_NUM,
ROW_NUMBER() OVER (PARTITION BY CALL_ID ORDER BY DT desc) as RN,
case 
when (lower(a.SUBJ1) like ''%дебет%'' or lower(a.SUBJ2) like ''%дебет%'' or lower(a.SUBJ3) like ''%дебет%'' or lower(a.SUBJ4) like ''%дебет%'' or lower(a.SUBJ5) like ''%дебет%'') then ''Дебетовая карта''
when (lower(a.PRODUCT1) like ''%дебет%'' or lower(a.PRODUCT2) like ''%дебет%'' or lower(a.PRODUCT3) like ''%дебет%'' or lower(a.PRODUCT4) like ''%дебет%'' or lower(a.PRODUCT5) like ''%дебет%'') then ''Дебетовая карта''
when (lower(a.SUBJ1R) like ''%дебет%'' or lower(a.SUBJ2R) like ''%дебет%'' or lower(a.SUBJ3R) like ''%дебет%'' or lower(a.SUBJ4R) like ''%дебет%'' or lower(a.SUBJ5R) like ''%дебет%'') then ''Дебетовая карта''
when (lower(a.PRODUCT1R) like ''%дебет%'' or lower(a.PRODUCT2R) like ''%дебет%'' or lower(a.PRODUCT3R) like ''%дебет%'' or lower(a.PRODUCT4R) like ''%дебет%'' or lower(a.PRODUCT5R) like ''%дебет%'') then ''Дебетовая карта''
when (lower(a.SUBJ1) like ''%кредит%'' or lower(a.SUBJ2) like ''%кредит%'' or lower(a.SUBJ3) like ''%кредит%'' or lower(a.SUBJ4) like ''%кредит%'' or lower(a.SUBJ5) like ''%кредит%'') then ''Кредитная карта''
when (lower(a.PRODUCT1) like ''%кредит%'' or lower(a.PRODUCT2) like ''%кредит%'' or lower(a.PRODUCT3) like ''%кредит%'' or lower(a.PRODUCT4) like ''%кредит%'' or lower(a.PRODUCT5) like ''%кредит%'') then ''Кредитная карта''
when (lower(a.SUBJ1R) like ''%кредит%'' or lower(a.SUBJ2R) like ''%кредит%'' or lower(a.SUBJ3R) like ''%кредит%'' or lower(a.SUBJ4R) like ''%кредит%'' or lower(a.SUBJ5R) like ''%кредит%'') then ''Кредитная карта''
when (lower(a.PRODUCT1R) like ''%кредит%'' or lower(a.PRODUCT2R) like ''%кредит%'' or lower(a.PRODUCT3R) like ''%кредит%'' or lower(a.PRODUCT4R) like ''%кредит%'' or lower(a.PRODUCT5R) like ''%кредит%'') then ''Кредитная карта'' else
''Не определено'' end as card_type,
HAVE_REDIRECT,
0 as MONEY
from ANALYTICS.TOLOG_RETENTIONS_CALLS_TABLE a
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID d on a.client_id = d.client_kih_id
where d.client_did is not null))
GROUP BY 
EXTRACT(YEAR FROM DATE_CREATED),
EXTRACT(MONTH FROM DATE_CREATED),
CLIENT_FIO, CLIENT_DID, CARD_TYPE



