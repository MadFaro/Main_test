CREATE TABLE analytics.tolog_cr_new_product_live_2 AS
SELECT
    CASE WHEN trunc(ACC_OPEN_DT, 'mm') IS NOT NULL AND trunc(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN months_between(trunc(ACC_OPEN_DT, 'mm'), trunc(ACC_CLOSE_DT, 'mm')) / 12 ELSE NULL END AS yy_bet,
    a.CONTRACT_UID, 
    a.ACC_NUM, 
    a.CONTRACT_NUM, 
    a.ACC_CLOSE_DT, 
    a.ACC_OPEN_DT, 
    a.STATUS_NM, 
    a.CLIENT_ID, 
    a.CLIENT_DID,
    a.REPORT_MONTH, 
    a.PIL, 
    a.AUTO, 
    a.MORT, 
    a.CONTRACT_CC, 
    a.CONTRACT_OVER, 
    a.CREDIT_CARD, 
    a.DEBIT_CARD, 
    a.DC_CL, 
    a.TERM_DEPOSIT, 
    a.DVS, 
    a.REPAYMENT_ANNUITET, 
    a.CURRENT_ACCOUNT, 
    a.REPAYMENT_CC, 
    a.IS_NTB, 
    a.CLIENT_SEGMENT, 
    a.RETAIL_SEG,
    a.PRIOR_PRODUCT, 
    a.MACROFILIAL, 
    COUNT(DISTINCT CASE WHEN b.created >= a.ACC_OPEN_DT AND b.created < ADD_MONTHS(a.ACC_OPEN_DT, 1) THEN b.created END) AS contacted_in_1_month,
    COUNT(DISTINCT CASE WHEN b.created >= ADD_MONTHS(a.ACC_OPEN_DT, 1) AND b.created < ADD_MONTHS(a.ACC_OPEN_DT, 2) THEN b.created END) AS contacted_in_2_month,
    SUM(NVL(b.unic_cnt, 0)) AS have_chat,
    SUM(NVL(b.cnt, 0)) AS have_sum_chat,
    SUM(NVL(f.unic_cnt, 0)) AS have_calls,
    SUM(NVL(f.cnt, 0)) AS have_sum_calls
FROM 
    analytics.tolog_cr_new_product_live a
LEFT JOIN 
    ANALYTICS.TOLOG_CHAT_CR b ON 
    a.CLIENT_DID = b.CLIENT_DID
LEFT JOIN 
    ANALYTICS.TOLOG_CALLS_CR f ON 
    a.CLIENT_DID = f.CLIENT_DID
WHERE 
    ACC_OPEN_DT >= DATE '2022-01-01'
GROUP BY 
    CASE WHEN trunc(ACC_OPEN_DT, 'mm') IS NOT NULL AND trunc(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN months_between(trunc(ACC_OPEN_DT, 'mm'), trunc(ACC_CLOSE_DT, 'mm')) / 12 ELSE NULL END,
    a.CONTRACT_UID, 
    a.ACC_NUM, 
    a.CONTRACT_NUM, 
    a.ACC_CLOSE_DT, 
    a.ACC_OPEN_DT, 
    a.STATUS_NM, 
    a.CLIENT_ID, 
    a.CLIENT_DID,
    a.REPORT_MONTH, 
    a.PIL, 
    a.AUTO, 
    a.MORT, 
    a.CONTRACT_CC, 
    a.CONTRACT_OVER, 
    a.CREDIT_CARD, 
    a.DEBIT_CARD, 
    a.DC_CL, 
    a.TERM_DEPOSIT, 
    a.DVS, 
    a.REPAYMENT_ANNUITET, 
    a.CURRENT_ACCOUNT, 
    a.REPAYMENT_CC, 
    a.IS_NTB, 
    a.CLIENT_SEGMENT, 
    a.RETAIL_SEG,
    a.PRIOR_PRODUCT, 
    a.MACROFILIAL;
