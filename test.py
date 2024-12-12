
create or replace procedure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         tolog_retention_finally as 
begin
execute immediate 'truncate table analytics.tolog_tab_transaction';
execute immediate
'insert into analytics.tolog_tab_transaction
select /*+parallel(4)*/
a.CLIENT_DID,
a.CARD_ID,
TRUNC(a.TRANSACTION_DATETIME) as TRANSACTION_DATETIME,
max(b.start_date) as date_card,
case when lower(b.scheme_name) like ''%rc%'' then ''Договор на текущий счет для кредитной карты'' else ''Договор на текущий счет для дебетовой карты'' end as product_category_name
from cmdm2.transaction a
left join cmdm2.card b on a.CARD_ID = b.CARD_ID
where TRANSACTION_DATETIME>=date''2023-04-01'' and AMOUNT>100
group by a.CLIENT_DID, a.CARD_ID, TRUNC(a.TRANSACTION_DATETIME), 
case when lower(b.scheme_name) like ''%rc%'' then ''Договор на текущий счет для кредитной карты'' else ''Договор на текущий счет для дебетовой карты'' end';

execute immediate 'truncate table analytics.tolog_tab_contract';
execute immediate
'insert into analytics.tolog_tab_contract
select /*+parallel(4)*/
distinct CONTRACT_UID, 
case when lower(scheme_name) like ''%rc%'' then ''Договор на текущий счет для кредитной карты'' else ''Договор на текущий счет для дебетовой карты'' end as product_category_name
from cmdm2.card
where START_DATE >= date''2023-04-01''';

execute immediate 'truncate table analytics.tolog_tab_card_credit';
execute immediate
'insert into analytics.tolog_tab_card_credit 
select /*+parallel(4)*/
CLIENT_DID, min(START_DATE) as START_DATE from (
select START_DATE, CLIENT_DID, 
case when lower(scheme_name) like ''%rc%'' then ''Договор на текущий счет для кредитной карты'' else ''Договор на текущий счет для дебетовой карты'' end as product_category_name
from cmdm2.card
where STATUS_NAME <> ''CARD CLOSED'')
where product_category_name = ''Договор на текущий счет для кредитной карты''
group by CLIENT_DID';

execute immediate 'truncate table analytics.tolog_tab_card_debet';
execute immediate
'insert into analytics.tolog_tab_card_debet
select /*+parallel(4)*/
CLIENT_DID, min(START_DATE) as START_DATE from (
select START_DATE, CLIENT_DID, 
case when lower(scheme_name) like ''%rc%'' then ''Договор на текущий счет для кредитной карты'' else ''Договор на текущий счет для дебетовой карты'' end as product_category_name
from cmdm2.card
where STATUS_NAME <> ''CARD CLOSED'')
where product_category_name = ''Договор на текущий счет для дебетовой карты''
group by CLIENT_DID';

execute immediate 'truncate table analytics.tolog_tab_card_dc';
execute immediate
'insert into analytics.tolog_tab_card_dc
select /*+parallel(4)*/
b.CLIENT_KIH_ID, a.START_DATE from CMDM2.CARD a
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID b on a.CLIENT_DID = b.CLIENT_DID
where a.START_DATE >= date''2023-04-01'' and a.CONTRACT_UID in (select distinct CONTRACT_UID from analytics.tolog_tab_contract
                                                where product_category_name <> ''Договор на текущий счет для кредитной карты'')';

execute immediate 'truncate table analytics.tolog_tab_card_cc';
execute immediate
'insert into analytics.tolog_tab_card_cc
select /*+parallel(4)*/
b.CLIENT_KIH_ID, a.START_DATE from CMDM2.CARD a
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID b on a.CLIENT_DID = b.CLIENT_DID
where a.START_DATE >= date''2023-04-01'' and a.CONTRACT_UID in (select distinct CONTRACT_UID from analytics.tolog_tab_contract
                                                where product_category_name = ''Договор на текущий счет для кредитной карты'')';

execute immediate 'truncate table analytics.tolog_tab_card';
execute immediate
'insert into analytics.tolog_tab_card
SELECT /*+parallel(4)*/
c.*, 
a.TIME_CLOSE, 
a.call_flag, 
case when lower(c.scheme_name) like ''%rc%'' then ''Договор на текущий счет для кредитной карты'' else ''Договор на текущий счет для дебетовой карты'' end as product_category_name
FROM ANALYTICS.TOLOG_CLOSED_CARDS_AND_PACKAGES_ON_CALL  a
left JOIN dm.cards b ON a.obj_id = b.card_src_id
left JOIN cmdm2.card c ON b.card_uid = c.card_uid
WHERE a.CLASS_ID = ''OWS_CARDS''';

execute immediate 'truncate table analytics.tolog_tab_mex';
execute immediate
'insert into analytics.tolog_tab_mex
with tab_login as(
select * from (
select FIO_LEAD as FIO, replace(NETNAME, ''FC\'', '''') AS login from ANALYTICS.RAP_OPERATORS_REP
where NETNAME is not null
group by FIO_LEAD, replace(NETNAME, ''FC\'', '''')))
select /*+parallel(4)*/
RESPONSE_TIMESTAMP, CLIENT_IBSO_ID, CLIENT_DID, MONEY, NO_MONEY, RETENTION_PRODUCT_CODE, RETENTION_PRODUCT_NAME, RETENTION_PRODUCT_COST, OPERATOR_ID, FIO from (
select distinct a.*, b.fio from (
select a.* from (
select a.*
from (
select trunc(a.RESPONSE_TIMESTAMP) as RESPONSE_TIMESTAMP, a.CLIENT_IBSO_ID, c.CLIENT_DID,
case when b.retention_product_cost >0 then ''Денежная механика'' else null end as money,
case when b.retention_product_cost >0 then null when a.retention_product_code is not null then ''Неденежная механика'' else null end as no_money,
a.retention_product_code,
b.retention_product_name,
b.retention_product_cost,
upper(a.OPERATOR_ID) as OPERATOR_ID
from stage_unc.rsa_ret_unit_responses@cvm a
left join stage_unc.dict_ret_unit_products@cvm b on a.retention_product_code = b.retention_product_code
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID c on a.CLIENT_ID=c.client_kih_id
where a.RESPONSE_TIMESTAMP >= date''2023-04-01'' and CLIENT_DID is not null and RETENTION_UNIT_RESP_TYPE = ''RETENTION_CODE_CHOSEN'') a 
where money is not null or no_money is not null) a) a
left join tab_login b on b.login = a.OPERATOR_ID)
group by RESPONSE_TIMESTAMP, CLIENT_IBSO_ID, CLIENT_DID, MONEY, NO_MONEY, RETENTION_PRODUCT_CODE, RETENTION_PRODUCT_NAME, RETENTION_PRODUCT_COST, OPERATOR_ID, FIO';

execute immediate 'TRUNCATE TABLE ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE';
INSERT INTO ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE 
select /*+parallel(4)*/ distinct a.*,
case when b.CLIENT_DID is not null then 1 else 0 end as have_credit,
case when d.CLIENT_DID is not null then 1 else 0 end as have_debit
from (
select a.*, 
case when b.money is not null or a.them in ('Отмена комиссии по 120 дней_КК','Отмена комиссии по Прибыли','Сниж.ставки на POS/ATM 3мес_КК',
'Повыш. %на остаток 2мес._ДК','Доп.2% УБ на 6мес_ДК',
'Доп.2% по УБ на 6мес_КК','Кэшбэк 10% на 1 мес_ДК','Кэшбэк 10% на 1 мес_КК',
'РБ_Закрытие_120_Отмена комиссии за обслуживание',
'РБ_Закрытие_МИР_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_Прибыль_сохранена без механики',
'РБ_Закрытие_Прибыль_Повышенный %на остаток на 2 мес',
'РБ_Закрытие_Прибыль_Дополнительно 2% по УБ на 6 мес',
'РБ_Закрытие_120_Снижение ставки на POS и ATM по КК на 3 мес',
'РБ_Закрытие_Прибыль_Отмена комиссии за обслуживание',
'РБ_Закрытие_120_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_Прибыль_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_120_сохранена без механики',
'РБ_Закрытие_Кред.карта с кэшбеком_сохранена без механики',
'РБ_Закрытие_Кред.карта с кэшбеком_Дополнительно 2% по УБ на 6 мес',
'РБ_Закрытие_Эконом_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_Кред.карта с кэшбеком_Снижение ставки на POS и ATM по КК на 3 мес',
'РБ_Закрытие_Копилка_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_Кред.карта с кэшбеком__Кэшбэк 10% на 1 мес'
)
then 1 else 0 end as money,
case when b.no_money is not null or them in ('Сохранена без механики_ДК','Сохранена без механики_КК', 'РБ_Закрытие_120_сохранена без механики', 'РБ_Закрытие_Прибыль_сохранена без механики', 'РБ_Закрытие_Кред.карта с кэшбеком_сохранена без механики') then 1 else 0 end as no_money,
case when b.RETENTION_PRODUCT_CODE = 'R_PRODUCT_27' or a.them in ('Кэшбэк 10% на 1 мес_ДК','Кэшбэк 10% на 1 мес_КК',
'РБ_Закрытие_МИР_Кэшбэк 10% на 1 мес','РБ_Закрытие_120_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_Прибыль_Кэшбэк 10% на 1 мес','РБ_Закрытие_Эконом_Кэшбэк 10% на 1 мес',
'РБ_Закрытие_Копилка_Кэшбэк 10% на 1 мес','РБ_Закрытие_Кред.карта с кэшбеком__Кэшбэк 10% на 1 мес'
) then 1 else 0 end as money1,
case when b.RETENTION_PRODUCT_CODE = 'R_PRODUCT_62' or a.them in ('Отмена комиссии по 120 дней_КК', 'РБ_Закрытие_120_Отмена комиссии за обслуживание', 'РБ_Закрытие_Кред.карта с кэшбеком_Отмена комиссии за обслуживание') then 1 else 0 end as money2,
case when b.RETENTION_PRODUCT_CODE = 'R_PRODUCT_60' or a.them in ('Повыш. %на остаток 2мес._ДК', 'РБ_Закрытие_Прибыль_Повышенный %на остаток на 2 мес') then 1 else 0 end as money3,
case when b.RETENTION_PRODUCT_CODE = 'R_PRODUCT_58' or a.them in ('Доп.2% УБ на 6мес_ДК', 'Доп.2% по УБ на 6мес_КК', 'РБ_Закрытие_Прибыль_Дополнительно 2% по УБ на 6 мес', 'РБ_Закрытие_Кред.карта с кэшбеком_Дополнительно 2% по УБ на 6 мес', 'РБ_Закрытие_120_Дополнительно 2% по УБ на 6 мес') then 1 else 0 end as money4,
case when b.RETENTION_PRODUCT_CODE = 'R_PRODUCT_61' or a.them in ('Сниж.ставки на POS/ATM 3мес_КК', 'РБ_Закрытие_120_Снижение ставки на POS и ATM по КК на 3 мес', 'РБ_Закрытие_Кред.карта с кэшбеком_Снижение ставки на POS и ATM по КК на 3 мес') then 1 else 0 end as money5,
case when b.RETENTION_PRODUCT_CODE = 'R_PRODUCT_59' or a.them in ('Отмена комиссии по Прибыли', 'РБ_Закрытие_Прибыль_Отмена комиссии за обслуживание', 'РБ_Закрытие_120_Отмена комиссии за обслуживание') then 1 else 0 end as money6
from (
select distinct
'Звонки' as type,
a.dt - INTERVAL '2' HOUR as date_created,
cast(a.call_id as number) as id,
a.operator as operator_ddo,
a.rr_operator as operator_rr,
a.fio as client_fio,
a.client_did as client_did,
a.called_from_num as ibso_id_or_called_from_num,
case 
when (lower(a.SUBJ1) like '%дебет%' or lower(a.SUBJ2) like '%дебет%' or lower(a.SUBJ3) like '%дебет%' or lower(a.SUBJ4) like '%дебет%' or lower(a.SUBJ5) like '%дебет%') then 'Дебетовая карта'
when (lower(a.PRODUCT1) like '%дебет%' or lower(a.PRODUCT2) like '%дебет%' or lower(a.PRODUCT3) like '%дебет%' or lower(a.PRODUCT4) like '%дебет%' or lower(a.PRODUCT5) like '%дебет%') then 'Дебетовая карта'
when (lower(a.SUBJ1R) like '%дебет%' or lower(a.SUBJ2R) like '%дебет%' or lower(a.SUBJ3R) like '%дебет%' or lower(a.SUBJ4R) like '%дебет%' or lower(a.SUBJ5R) like '%дебет%') then 'Дебетовая карта'
when (lower(a.PRODUCT1R) like '%дебет%' or lower(a.PRODUCT2R) like '%дебет%' or lower(a.PRODUCT3R) like '%дебет%' or lower(a.PRODUCT4R) like '%дебет%' or lower(a.PRODUCT5R) like '%дебет%') then 'Дебетовая карта'
when (lower(a.SUBJ1) like '%кредит%' or lower(a.SUBJ2) like '%кредит%' or lower(a.SUBJ3) like '%кредит%' or lower(a.SUBJ4) like '%кредит%' or lower(a.SUBJ5) like '%кредит%') then 'Кредитная карта'
when (lower(a.PRODUCT1) like '%кредит%' or lower(a.PRODUCT2) like '%кредит%' or lower(a.PRODUCT3) like '%кредит%' or lower(a.PRODUCT4) like '%кредит%' or lower(a.PRODUCT5) like '%кредит%') then 'Кредитная карта'
when (lower(a.SUBJ1R) like '%кредит%' or lower(a.SUBJ2R) like '%кредит%' or lower(a.SUBJ3R) like '%кредит%' or lower(a.SUBJ4R) like '%кредит%' or lower(a.SUBJ5R) like '%кредит%') then 'Кредитная карта'
when (lower(a.PRODUCT1R) like '%кредит%' or lower(a.PRODUCT2R) like '%кредит%' or lower(a.PRODUCT3R) like '%кредит%' or lower(a.PRODUCT4R) like '%кредит%' or lower(a.PRODUCT5R) like '%кредит%') then 'Кредитная карта' else
'Не определено' end as card_type,
a.have_transaction_new_debet,
a.have_transaction_old_debet,
a.have_transaction_new_credit,
a.have_transaction_old_credit,
a.have_redirect,
a.have_offer_debet,
a.have_offer_credit,
a.card_close_debet,
a.card_close_cc_debet,
a.card_close_ofice_debet,
a.card_close_credit,
a.card_close_cc_credit,
a.card_close_ofice_credit,
case when b.CLIENT_KIH_ID is not null then 1 else 0 end as have_new_product_debet,
case when c.CLIENT_KIH_ID is not null then 1 else 0 end as have_new_product_credit,
a.have_termination,
a.RESUL_CALLS as them
from(
Select distinct a.*,
case when b.CLIENT_DID is not null  then 1 else 0 end as have_transaction_new_debet,
case when c.CLIENT_DID is not null  then 1 else 0 end as have_transaction_old_debet,
case when d.CLIENT_DID is not null  then 1 else 0 end as have_transaction_new_credit,
case when e.CLIENT_DID is not null  then 1 else 0 end as have_transaction_old_credit
from(
Select distinct a.*, c.CLIENT_DID, 
case when b.CLIENT_DID is not null and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_debet,
case when b.CLIENT_DID is not null and b.call_flag=1 and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_CC_debet,
case when b.CLIENT_DID is not null and b.call_flag=0 and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_OFICE_debet,
case when b.CLIENT_DID is not null and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_credit,
case when b.CLIENT_DID is not null and b.call_flag=1 and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_CC_credit,
case when b.CLIENT_DID is not null and b.call_flag=0 and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_OFICE_credit,
case when d.CLIENT_DID is not null then 1 else 0 end as have_termination
from analytics.tolog_retentions_calls_table a
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID c on a.CLIENT_ID=c.client_kih_id
left join analytics.tolog_tab_card b on c.CLIENT_DID=b.CLIENT_DID and b.TIME_CLOSE>=a.DT and b.TIME_CLOSE<a.DT + INTERVAL '31' DAY
left join analytics.tolog_tab_card d on c.CLIENT_DID=d.CLIENT_DID and d.TIME_CLOSE<a.DT and (d.FACT_CLOSE_DATE>a.DT or d.FACT_CLOSE_DATE is null)
where TODO_ACTL_START_DT>=date'2023-04-01') a
left join analytics.tolog_tab_transaction b on a.CLIENT_DID=b.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and b.TRANSACTION_DATETIME>=a.DT and b.TRANSACTION_DATETIME<a.DT + interval '31' day and b.DATE_CARD > a.DT and b.PRODUCT_CATEGORY_NAME <> 'Договор на текущий счет для кредитной карты'
left join analytics.tolog_tab_transaction c on a.CLIENT_DID=c.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and c.TRANSACTION_DATETIME>=a.DT and c.TRANSACTION_DATETIME<a.DT + interval '31' day and c.DATE_CARD < a.DT and c.PRODUCT_CATEGORY_NAME <> 'Договор на текущий счет для кредитной карты'
left join analytics.tolog_tab_transaction d on a.CLIENT_DID=d.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and d.TRANSACTION_DATETIME>=a.DT and d.TRANSACTION_DATETIME<a.DT + interval '31' day and d.DATE_CARD > a.DT and d.PRODUCT_CATEGORY_NAME = 'Договор на текущий счет для кредитной карты'
left join analytics.tolog_tab_transaction e on a.CLIENT_DID=e.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and e.TRANSACTION_DATETIME>=a.DT and e.TRANSACTION_DATETIME<a.DT + interval '31' day and e.DATE_CARD < a.DT and e.PRODUCT_CATEGORY_NAME = 'Договор на текущий счет для кредитной карты') a
left join analytics.tolog_tab_card_dc b on a.CLIENT_ID = b.CLIENT_KIH_ID and b.START_DATE > a.DT
left join analytics.tolog_tab_card_cc c on a.CLIENT_ID = c.CLIENT_KIH_ID and c.START_DATE > a.DT
union all
Select distinct
'Чаты' as type,
a.created as date_created,
a.threadid as id,
a.operatorfullname as operator_ddo,
case when a.rr_operator = '176420' then 'Музафаров Тимур Надирович'
when a.rr_operator = '176423' then 'Фазлиахметова Альбина Ансафовна'
when a.rr_operator = '176421' then 'Сабанаева Эльвина Линафовна'
when a.rr_operator = '176422' then 'Трапезников Дмитрий Павлович'
when a.rr_operator = '176417' then 'Филиппова Екатерина Сергеевна'
when a.rr_operator = '176381' then 'Антонов Антон Валерьевич'
when a.rr_operator = '176560' then 'Аскарова Диана Ураловна'
when a.rr_operator = '176251' then 'Сафина Диана Мансуровна'
when a.rr_operator = '176669' then 'Тахаутдинова Эльвира Руслановна'
when a.rr_operator = '176768' then 'Камалиева Малена Венеровна'
when a.rr_operator = '176557' then 'Рахимова Азалия Азатовна' else null end as operator_rr,
a.client_name as client_fio,
a.client_did as client_did,
a.client_ibso_id as ibso_id_or_called_from_num,
case when
a.SUBCATEGORY IS NULL and a.CATEGORY IS NULL THEN 'Не определено'
when (a.SUBCATEGORY in (
'РБ_Закрытие_ДейстПотреб',
'РБ_Закрытие_Прибыль',
'РБ_Закрытие_МИР',
'РБ_Закрытие_Эконом',
'Дебетовые карты') or a.CATEGORY in (
'РБ_Закрытие_ДейстПотреб',
'РБ_Закрытие_Прибыль',
'РБ_Закрытие_МИР',
'РБ_Закрытие_Эконом',
'Дебетовые карты') or lower(a.SUBCATEGORY) like '%дебет%' or lower(a.CATEGORY) like '%дебет%') then 'Дебетовая карта' 
when (a.SUBCATEGORY in (
'РБ_Закрытие_120',
'РБ_Закрытие_кредитная карта с кэшбеком',
'РБ_Закрытие_ДейстКК',
'РБ_Закрытие_КК MIR Supreme',
'РБ_Закрытие_КЦ_СКБ',
'Кредитные карты') or a.CATEGORY in (
'РБ_Закрытие_120',
'РБ_Закрытие_кредитная карта с кэшбеком',
'РБ_Закрытие_ДейстКК',
'РБ_Закрытие_КК MIR Supreme',
'РБ_Закрытие_КЦ_СКБ',
'Кредитные карты') or lower(a.SUBCATEGORY) like '%кредит%' or lower(a.CATEGORY) like '%кредит%') then 'Кредитная карта' 
else 'Не определено' end as card_type,
case when b.CLIENT_DID is not null  then 1 else 0 end as have_transaction_new_debet,
case when c.CLIENT_DID is not null  then 1 else 0 end as have_transaction_old_debet,
case when d.CLIENT_DID is not null  then 1 else 0 end as have_transaction_new_credit,
case when e.CLIENT_DID is not null  then 1 else 0 end as have_transaction_old_credit,
a.have_redirect,
a.have_offer_debet,
a.have_offer_credit,
a.card_close_debet,
a.card_close_cc_debet,
a.card_close_ofice_debet,
a.card_close_credit,
a.card_close_cc_credit,
a.card_close_ofice_credit,
a.have_new_product_debet,
a.have_new_product_credit,
a.have_termination,
a.SUBCATEGORY as them
from(
Select distinct a.*, 
case when b.CLIENT_DID is not null and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_debet,
case when b.CLIENT_DID is not null and b.call_flag=1 and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_CC_debet,
case when b.CLIENT_DID is not null and b.call_flag=0 and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_OFICE_debet,
case when b.CLIENT_DID is not null and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_credit,
case when b.CLIENT_DID is not null and b.call_flag=1 and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_CC_credit,
case when b.CLIENT_DID is not null and b.call_flag=0 and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end as card_close_OFICE_credit,
case when d.CLIENT_DID is not null then 1 else 0 end as have_termination
from (
select distinct a.*, 
case when b.CLIENT_DID is not null then 1 else 0 end as have_new_product_debet,
case when c.CLIENT_DID is not null then 1 else 0 end as have_new_product_credit
from ANALYTICS.TOLOG_RETENTIONS_CHATS_TABLE a
left join CMDM2.CARD b on a.CLIENT_DID=b.CLIENT_DID and a.CREATED < b.START_DATE and b.CONTRACT_UID in (select distinct CONTRACT_UID from analytics.tolog_tab_contract
                                                where product_category_name <> 'Договор на текущий счет для кредитной карты')
left join CMDM2.CARD c on a.CLIENT_DID=c.CLIENT_DID and a.CREATED < c.START_DATE and c.CONTRACT_UID in (select distinct CONTRACT_UID from analytics.tolog_tab_contract
                                                where product_category_name = 'Договор на текущий счет для кредитной карты')) a
left join analytics.tolog_tab_card b on a.CLIENT_DID=b.CLIENT_DID and b.TIME_CLOSE>=a.CREATED and b.TIME_CLOSE<a.CREATED + INTERVAL '31' DAY
left join analytics.tolog_tab_card d on a.CLIENT_DID=d.CLIENT_DID and d.TIME_CLOSE<a.CREATED) a
left join analytics.tolog_tab_transaction b on a.CLIENT_DID=b.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and b.TRANSACTION_DATETIME>=a.CREATED and b.TRANSACTION_DATETIME<a.CREATED + interval '31' day and b.DATE_CARD > a.CREATED and b.PRODUCT_CATEGORY_NAME <> 'Договор на текущий счет для кредитной карты'
left join analytics.tolog_tab_transaction c on a.CLIENT_DID=c.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and c.TRANSACTION_DATETIME>=a.CREATED and c.TRANSACTION_DATETIME<a.CREATED + interval '31' day and c.DATE_CARD < a.CREATED and c.PRODUCT_CATEGORY_NAME <> 'Договор на текущий счет для кредитной карты'
left join analytics.tolog_tab_transaction d on a.CLIENT_DID=d.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and d.TRANSACTION_DATETIME>=a.CREATED and d.TRANSACTION_DATETIME<a.CREATED + interval '31' day and d.DATE_CARD > a.CREATED and d.PRODUCT_CATEGORY_NAME = 'Договор на текущий счет для кредитной карты'
left join analytics.tolog_tab_transaction e on a.CLIENT_DID=e.CLIENT_DID and card_close_debet = 0 and card_close_credit=0 and e.TRANSACTION_DATETIME>=a.CREATED and e.TRANSACTION_DATETIME<a.CREATED + interval '31' day and e.DATE_CARD < a.CREATED and e.PRODUCT_CATEGORY_NAME = 'Договор на текущий счет для кредитной карты') a
left join analytics.tolog_tab_mex b on a.CLIENT_DID = b.CLIENT_DID and trunc(a.DATE_CREATED) = trunc(b.RESPONSE_TIMESTAMP) and upper(b.fio) = upper(a.operator_rr)) a
left join analytics.tolog_tab_card_credit b on a.CLIENT_DID=b.CLIENT_DID and a.date_created >= b.START_DATE
left join analytics.tolog_tab_card_debet d on a.CLIENT_DID=d.CLIENT_DID and a.date_created >= d.START_DATE;
commit;
execute immediate 'TRUNCATE TABLE ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE_CLIENT'; 
insert /*+NO_GATHER_OPTIMIZER_STATISTICS*/ into ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE_CLIENT 
with tab_card_count as ( 
select CLIENT_DID, sum(CNT) as CNT from ANALYTICS.TOLOG_CARD_COUNT
group by CLIENT_DID)
select a.*, b.CNT
from (
select a.*,
case when b.CLIENT_DID is not null then 1 else 0 end as have_credit,
case when d.CLIENT_DID is not null then 1 else 0 end as have_debit
from (
select
CLIENT_DID,
CLIENT_FIO,
TYPE as type_,
CARD_TYPE,
trunc(DATE_CREATED, 'mm') as Date_,
max(ID),
max(IBSO_ID_OR_CALLED_FROM_NUM),
max(HAVE_TRANSACTION_NEW_DEBET),
max(HAVE_TRANSACTION_OLD_DEBET),
max(HAVE_TRANSACTION_NEW_CREDIT),
max(HAVE_TRANSACTION_OLD_CREDIT),
max(HAVE_REDIRECT),
max(HAVE_OFFER_DEBET),
max(HAVE_OFFER_CREDIT),
max(CARD_CLOSE_DEBET),
max(CARD_CLOSE_CC_DEBET),
max(CARD_CLOSE_OFICE_DEBET),
max(CARD_CLOSE_CREDIT),
max(CARD_CLOSE_CC_CREDIT),
max(CARD_CLOSE_OFICE_CREDIT),
max(HAVE_NEW_PRODUCT_DEBET),
max(HAVE_NEW_PRODUCT_CREDIT),
max(HAVE_TERMINATION),
max(MONEY) AS MONEY,
max(MONEY1) AS MONEY1,
max(MONEY2) AS MONEY2,
max(MONEY3) AS MONEY3,
max(MONEY4) AS MONEY4,
max(MONEY5) AS MONEY5,
max(MONEY6) AS MONEY6
from ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE
group by CLIENT_DID, CLIENT_FIO, TYPE, CARD_TYPE, THEM, trunc(DATE_CREATED, 'mm')) a
left join analytics.tolog_tab_card_credit b on a.CLIENT_DID=b.CLIENT_DID and a.Date_ >= b.START_DATE
left join analytics.tolog_tab_card_debet d on a.CLIENT_DID=d.CLIENT_DID and a.Date_ >= d.START_DATE) a
left join tab_card_count b on a.client_did = b.client_did;
commit;
execute immediate 'TRUNCATE TABLE ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE_CONTROL';
insert /*+NO_GATHER_OPTIMIZER_STATISTICS*/ into ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE_CONTROL
with tab_calls as (select * from (
select a.*,
case when (b.CLIENT_DID is not null and b.OFFER_NAME = 'Retention_CC_wnt_cls_in_call') or 
(e.CLIENT_DID is not null and e.OFFER_NAME = 'Retention_CC_wnt_cls_in_call')
then 1 else 0 end as have_cc_credit,
case when (b.CLIENT_DID is not null and b.OFFER_NAME in ('Retention_DC_wnt_cls_in_call', 'Retention_Prib6mplus_wnt_cls_in_call', 'Retention_Prib6mless_wnt_cls_in_call')) or 
(e.CLIENT_DID is not null and e.OFFER_NAME in ('Retention_DC_wnt_cls_in_call', 'Retention_Prib6mplus_wnt_cls_in_call', 'Retention_Prib6mless_wnt_cls_in_call'))
then 1 else 0 end as have_dc_credit
from ANALYTICS.TOLOG_RETENTIONS_FINALLY_TABLE a
left join ANALYTICS.TOLOG_RETENTION_CONTROL b on a.CLIENT_DID = b.CLIENT_DID and b.contact_dt < a.DATE_CREATED and b.CONTACT_STATUS_NAME = 'Control'
left join ANALYTICS.TOLOG_RETENTION_CONTROL e on a.CLIENT_DID = e.CLIENT_DID and e.contact_dt < a.DATE_CREATED and e.CONTACT_DATE_TIME > a.DATE_CREATED and e.CONTACT_STATUS_NAME in ('Stopped', 'Stopping'))
where have_cc_credit = 1 or have_dc_credit = 1),
tab_card_count as ( 
select CLIENT_DID, sum(CNT) as CNT from ANALYTICS.TOLOG_CARD_COUNT
group by CLIENT_DID)
select a.*, b.CNT from (
select a.*,
case when b.CLIENT_DID is not null then 1 else 0 end as have_credit,
case when d.CLIENT_DID is not null then 1 else 0 end as have_debit
from (
select
CLIENT_DID,
CLIENT_FIO,
TYPE as type_,
CARD_TYPE,
THEM,
trunc(DATE_CREATED, 'mm') as Date_,
max(ID),
max(IBSO_ID_OR_CALLED_FROM_NUM),
max(HAVE_TRANSACTION_NEW_DEBET),
max(HAVE_TRANSACTION_OLD_DEBET),
max(HAVE_TRANSACTION_NEW_CREDIT),
max(HAVE_TRANSACTION_OLD_CREDIT),
max(HAVE_REDIRECT),
max(HAVE_OFFER_DEBET),
max(HAVE_OFFER_CREDIT),
max(CARD_CLOSE_DEBET),
max(CARD_CLOSE_CC_DEBET),
max(CARD_CLOSE_OFICE_DEBET),
max(CARD_CLOSE_CREDIT),
max(CARD_CLOSE_CC_CREDIT),
max(CARD_CLOSE_OFICE_CREDIT),
max(HAVE_NEW_PRODUCT_DEBET),
max(HAVE_NEW_PRODUCT_CREDIT),
max(HAVE_TERMINATION),
max(MONEY) AS MONEY,
max(MONEY1) AS MONEY1,
max(MONEY2) AS MONEY2,
max(MONEY3) AS MONEY3,
max(MONEY4) AS MONEY4,
max(MONEY5) AS MONEY5,
max(MONEY6) AS MONEY6
from tab_calls
group by CLIENT_DID, CLIENT_FIO, TYPE, CARD_TYPE, THEM, trunc(DATE_CREATED, 'mm')) a
left join analytics.tolog_tab_card_credit b on a.CLIENT_DID=b.CLIENT_DID and a.Date_ >= b.START_DATE
left join analytics.tolog_tab_card_debet d on a.CLIENT_DID=d.CLIENT_DID and a.Date_ >= d.START_DATE) a
left join tab_card_count b on a.client_did = b.client_did;
commit;
end;
