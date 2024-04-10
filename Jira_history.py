create table analytics.tolog_cr_new_product_live_2 as
with tab_chat as (
select trunc(a.created) as created, f.client_did, count(distinct f.client_did) as unic_cnt, count(*) as cnt from ODS.ODS_WIS_CHATTHREAD@cdw.prod a
left join ODS.ODS_WIS_CHATVISITOR@cdw.prod b on a.VISITORID=b.VISITORID
left join CMDM2.client f on b.PROVIDEDID=f.CLIENT_IBSO_ID
group by trunc(a.created), f.client_did),
tab_calls as (
select trunc(DT) as dt, CLIENT_DID, count(distinct CLIENT_ID) as unic_cnt, count(*) as cnt  from ANALYTICS.KDI_SIEBEL_PAST a
left join cmdm2.CLIENT_AGR_ID_X_CLIENT_DID d on a.client_id = d.client_kih_id
where TYPE = 'Вызов - входящий'
group by trunc(DT), CLIENT_DID)
select
CASE WHEN trunc(ACC_OPEN_DT, 'mm') IS NOT NULL AND trunc(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN months_between(trunc(ACC_OPEN_DT, 'mm'), trunc(ACC_CLOSE_DT, 'mm')) / 12 ELSE NULL END as mm_bet,
a.CONTRACT_UID, a.ACC_NUM, a.CONTRACT_NUM, a.ACC_CLOSE_DT, a.ACC_OPEN_DT, a.STATUS_NM, a.CLIENT_ID, a.CLIENT_DID,
a.REPORT_MONTH, a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG,a.PRIOR_PRODUCT, a.MACROFILIAL, 
sum(NVL(b.unic_cnt, 0)) as have_chat,
sum(NVL(b.cnt, 0)) as have_sum_chat,
sum(NVL(f.unic_cnt, 0)) as have_calls,
sum(NVL(f.cnt, 0)) as have_sum_calls
from analytics.tolog_cr_new_product_live a
left join tab_chat b on a.CLIENT_DID = b.CLIENT_DID and a.ACC_OPEN_DT <= b.created  and a.ACC_CLOSE_DT >= b.created  
left join tab_calls f on a.CLIENT_DID = f.CLIENT_DID and a.ACC_OPEN_DT <= f.dt and a.ACC_CLOSE_DT >= f.dt
group by CASE WHEN trunc(ACC_OPEN_DT, 'mm') IS NOT NULL AND trunc(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN months_between(trunc(ACC_OPEN_DT, 'mm'), trunc(ACC_CLOSE_DT, 'mm')) / 12 ELSE NULL END,
a.CONTRACT_UID, a.ACC_NUM, a.CONTRACT_NUM, a.ACC_CLOSE_DT, a.ACC_OPEN_DT, a.STATUS_NM, a.CLIENT_ID, a.CLIENT_DID,
a.REPORT_MONTH, a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG,a.PRIOR_PRODUCT, a.MACROFILIAL;
