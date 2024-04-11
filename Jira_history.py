create table analytics.tolog_cr_new_product_live as
select b.CONTRACT_UID, b.ACC_NUM, b.CONTRACT_NUM, 
case when b.ACC_CLOSE_DT is null then sysdate else b.ACC_CLOSE_DT end as ACC_CLOSE_DT, 
b.ACC_OPEN_DT, b.STATUS_NM,
a.CLIENT_ID, a.CLIENT_DID,
a.REPORT_MONTH, a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG,a.PRIOR_PRODUCT, a.MACROFILIAL
from analytics.finalta_3_0_full a
left join dm.contracts b on a.client_did = b.client_did and b.PRODUCT_CATEGORY_NM = 'Кредитная карта'
where trunc(a.REPORT_MONTH, 'mm') >= date'2022-01-01' and a.PRIOR_PRODUCT = 'Кредитная карта' and b.ACC_OPEN_DT is not null
group by b.CONTRACT_UID, b.ACC_NUM, b.CONTRACT_NUM, 
case when b.ACC_CLOSE_DT is null then sysdate else b.ACC_CLOSE_DT end, 
b.ACC_OPEN_DT, b.STATUS_NM,
a.CLIENT_ID, a.CLIENT_DID,
a.REPORT_MONTH, a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG, a.PRIOR_PRODUCT, a.MACROFILIAL
