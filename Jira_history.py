CREATE TABLE analytics.tolog_cr_new_product_live_2 AS
WITH tab_chat AS (
    SELECT 
        TRUNC(a.created) AS created, 
        f.client_did, 
        COUNT(DISTINCT f.client_did) AS unic_cnt, 
        COUNT(*) AS cnt 
    FROM 
        ODS.ODS_WIS_CHATTHREAD@cdw.prod a
    LEFT JOIN 
        ODS.ODS_WIS_CHATVISITOR@cdw.prod b ON a.VISITORID = b.VISITORID
    LEFT JOIN 
        CMDM2.client f ON b.PROVIDEDID = f.CLIENT_IBSO_ID
    GROUP BY 
        TRUNC(a.created), 
        f.client_did
),
tab_calls AS (
    SELECT 
        TRUNC(DT) AS dt, 
        CLIENT_DID, 
        COUNT(DISTINCT CLIENT_ID) AS unic_cnt, 
        COUNT(*) AS cnt  
    FROM 
        ANALYTICS.KDI_SIEBEL_PAST a
    LEFT JOIN 
        cmdm2.CLIENT_AGR_ID_X_CLIENT_DID d ON a.client_id = d.client_kih_id
    WHERE 
        TYPE = 'Вызов - входящий'
    GROUP BY 
        TRUNC(DT), 
        CLIENT_DID
)
SELECT
    CASE 
        WHEN TRUNC(ACC_OPEN_DT, 'mm') IS NOT NULL AND TRUNC(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN MONTHS_BETWEEN(TRUNC(ACC_OPEN_DT, 'mm'), TRUNC(ACC_CLOSE_DT, 'mm')) / 12 
        ELSE NULL 
    END AS mm_bet,
    a.CONTRACT_UID, a.ACC_NUM, a.CONTRACT_NUM, a.ACC_CLOSE_DT, a.ACC_OPEN_DT, 
    a.STATUS_NM, a.CLIENT_ID, a.CLIENT_DID,a.REPORT_MONTH, 
    a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, 
    a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
    a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, 
    a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG, a.PRIOR_PRODUCT, a.MACROFILIAL,
    SUM(NVL(b.unic_cnt, 0)) AS have_chat,
    SUM(NVL(b.cnt, 0)) AS have_sum_chat,
    SUM(NVL(f.unic_cnt, 0)) AS have_calls,
    SUM(NVL(f.cnt, 0)) AS have_sum_calls
FROM 
    analytics.tolog_cr_new_product_live a
LEFT JOIN 
    tab_chat b ON a.CLIENT_DID = b.CLIENT_DID AND a.ACC_OPEN_DT <= b.created AND a.ACC_CLOSE_DT >= b.created  
LEFT JOIN 
    tab_calls f ON a.CLIENT_DID = f.CLIENT_DID AND a.ACC_OPEN_DT <= f.dt AND a.ACC_CLOSE_DT >= f.dt
GROUP BY 
    CASE 
        WHEN TRUNC(ACC_OPEN_DT, 'mm') IS NOT NULL AND TRUNC(ACC_CLOSE_DT, 'mm') IS NOT NULL THEN MONTHS_BETWEEN(TRUNC(ACC_OPEN_DT, 'mm'), TRUNC(ACC_CLOSE_DT, 'mm')) / 12 
        ELSE NULL 
    END,
    a.CONTRACT_UID, a.ACC_NUM, a.CONTRACT_NUM, a.ACC_CLOSE_DT, a.ACC_OPEN_DT, 
    a.STATUS_NM, a.CLIENT_ID, a.CLIENT_DID,a.REPORT_MONTH, 
    a.PIL, a.AUTO, a.MORT, a.CONTRACT_CC, a.CONTRACT_OVER, 
    a.CREDIT_CARD, a.DEBIT_CARD, a.DC_CL, a.TERM_DEPOSIT, 
    a.DVS, a.REPAYMENT_ANNUITET, a.CURRENT_ACCOUNT, a.REPAYMENT_CC, 
    a.IS_NTB, a.CLIENT_SEGMENT, a.RETAIL_SEG, a.PRIOR_PRODUCT, a.MACROFILIAL

