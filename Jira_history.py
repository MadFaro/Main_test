create table analytics.tolog_cr_new_product_live as
select b.CONTRACT_UID, b.ACC_NUM, b.CONTRACT_NUM, 
case when b.ACC_CLOSE_DT is null then sysdate else b.ACC_CLOSE_DT end as ACC_CLOSE_DT, 
b.ACC_OPEN_DT, b.STATUS_NM,
a.* from analytics.finalta_3_0_full a
left join dm.contracts b on a.client_did = b.client_did and b.PRODUCT_CATEGORY_NM = 'Кредитная карта'
where trunc(a.REPORT_MONTH, 'mm') = date'2024-03-01' and a.PRIOR_PRODUCT = 'Кредитная карта' and b.ACC_OPEN_DT is not null

create table analytics.tolog_chat_cr as 
select trunc(a.created) as created, f.client_did, count(distinct f.client_did) as unic_cnt, count(*) as cnt from ODS.ODS_WIS_CHATTHREAD@cdw.prod a
left join ODS.ODS_WIS_CHATVISITOR@cdw.prod b on a.VISITORID=b.VISITORID
left join CMDM2.client f on b.PROVIDEDID=f.CLIENT_IBSO_ID
where a.created>=date'2023-01-01' and f.client_did is not null
group by trunc(a.created), f.client_did

create table analytics.tolog_calls_cr as 
select trunc(DT) as dt, CLIENT_DID, count(distinct CLIENT_ID) as unic_cnt, count(*) as cnt  from ANALYTICS.KDI_SIEBEL_PAST a
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID d on a.client_id = d.client_kih_id
where TYPE = 'Вызов - входящий' and dt >=date'2022-01-01' and CLIENT_DID is not null
group by trunc(DT), CLIENT_DID

create table analytics.tolog_cr_new_product_live_2 as
select
CASE WHEN trunc(ACC_OPEN_DT, 'mm') IS NOT NULL AND trunc(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN months_between(trunc(ACC_OPEN_DT, 'mm'), trunc(ACC_CLOSE_DT, 'mm')) / 12 ELSE NULL END as yy_bet,
a.CONTRACT_UID, a.ACC_NUM, a.CONTRACT_NUM, a.ACC_CLOSE_DT, a.ACC_OPEN_DT, a.STATUS_NM, a.CLIENT_ID, a.CLIENT_DID,
a.REPORT_MONTH, a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG,a.PRIOR_PRODUCT, a.MACROFILIAL, 
sum(NVL(b.unic_cnt, 0)) as have_chat,
sum(NVL(b.cnt, 0)) as have_sum_chat,
sum(NVL(f.unic_cnt, 0)) as have_calls,
sum(NVL(f.cnt, 0)) as have_sum_calls
from analytics.tolog_cr_new_product_live a
left join ANALYTICS.TOLOG_CHAT_CR b on a.CLIENT_DID = b.CLIENT_DID and a.ACC_OPEN_DT <= b.created  and a.ACC_CLOSE_DT >= b.created  
left join ANALYTICS.TOLOG_CALLS_CR f on a.CLIENT_DID = f.CLIENT_DID and a.ACC_OPEN_DT <= f.dt and a.ACC_CLOSE_DT >= f.dt
where ACC_OPEN_DT >=date'2022-01-01'
group by CASE WHEN trunc(ACC_OPEN_DT, 'mm') IS NOT NULL AND trunc(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN months_between(trunc(ACC_OPEN_DT, 'mm'), trunc(ACC_CLOSE_DT, 'mm')) / 12 ELSE NULL END,
a.CONTRACT_UID, a.ACC_NUM, a.CONTRACT_NUM, a.ACC_CLOSE_DT, a.ACC_OPEN_DT, a.STATUS_NM, a.CLIENT_ID, a.CLIENT_DID,
a.REPORT_MONTH, a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG,a.PRIOR_PRODUCT, a.MACROFILIAL
