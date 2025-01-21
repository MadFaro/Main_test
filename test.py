SELECT
    TO_CHAR(INTERV, 'YY.MMM') AS "Месяц год",
    TO_CHAR(TRUNC(INTERV, 'IW'), 'DD') || '-' || TO_CHAR(TRUNC(INTERV + 6, 'IW'), 'DD.MM') AS "Неделя",
    CASE 
        WHEN ENTERPRISENAME IN (
            'CCM_PG_1.SG_DDO_ActiveCredit', 
            'CCM_PG_1.SG_DDO_CityBank', 
            'CCM_PG_1.SG_Operator', 
            'CCM_PG_1.SG_Operator_1', 
            'CCM_PG_1.SG_Operator_2', 
            'CCM_PG_1.SG_Operator_3', 
            'CCM_PG_1.SG_Operator_4', 
            'CCM_PG_1.SG_Operator_5', 
            'CCM_PG_1.SG_DDO_T_Bank'
        ) THEN 'All'
        ELSE ENTERPRISENAME
    END AS "Группа",
    SUM(ANS1) + SUM(ANS2) + SUM(ANS3) + SUM(ANS4) + SUM(ANS5) +
    SUM(ANS6) + SUM(ANS7) + SUM(ANS8) + SUM(ANS9) + SUM(ANS10) +
    SUM(ABAN1) + SUM(ABAN2) + SUM(ABAN3) + SUM(ABAN4) + SUM(ABAN5) +
    SUM(ABAN6) + SUM(ABAN7) + SUM(ABAN8) + SUM(ABAN9) + SUM(ABAN10) AS income_call,
    SUM(ABAN1) + SUM(ABAN2) + SUM(ABAN3) + SUM(ABAN4) + SUM(ABAN5) +
    SUM(ABAN6) + SUM(ABAN7) + SUM(ABAN8) + SUM(ABAN9) + SUM(ABAN10) AS lost_call,
    (SUM(ABAN1) + SUM(ABAN2) + SUM(ABAN3) + SUM(ABAN4) + SUM(ABAN5) +
    SUM(ABAN6) + SUM(ABAN7) + SUM(ABAN8) + SUM(ABAN9) + SUM(ABAN10)) - SUM(ABAN1) AS lost_call_5_sec,
    SUM(ANS1) + SUM(ANS2) + SUM(ANS3) AS Sl_ans,
    (SUM(ANS1) + SUM(ANS2) + SUM(ANS3) + SUM(ANS4) + SUM(ANS5) +
    SUM(ANS6) + SUM(ANS7) + SUM(ANS8) + SUM(ANS9) + SUM(ANS10) +
    SUM(ABAN1) + SUM(ABAN2) + SUM(ABAN3) + SUM(ABAN4) + SUM(ABAN5) +
    SUM(ABAN6) + SUM(ABAN7) + SUM(ABAN8) + SUM(ABAN9) + SUM(ABAN10)) - SUM(ABAN1) AS income_call_5_sec
FROM
    ANALYTICS.CISCO_SL_TABLE
WHERE
    INTERV >= TRUNC(ADD_MONTHS(SYSDATE, -6), 'MM')
    AND ENTERPRISENAME <> 'CCM_PG_1.SG_TLM_RetentionUnit'
GROUP BY
    INTERV,
    ENTERPRISENAME;
