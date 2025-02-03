CREATE TABLE tolog_praic_lict_opros (
    REPORT_MONTH DATE,
    MOTIV_TABNUM NUMBER,  -- замените на реальный тип
    PRODUKT VARCHAR2(100),  -- замените на реальный тип
    dog_cnt NUMBER
);

INSERT INTO tolog_praic_lict_opros
SELECT 
    trunc(REPORT_MONTH, 'MM') as REPORT_MONTH, 
    MOTIV_TABNUM, 
    PRODUKT, 
    COUNT(DISTINCT DOG) as dog_cnt
FROM BALKHOVITIAV.VIEW_MOTIV_PRAIC_LICT_OPROS
WHERE trunc(REPORT_MONTH, 'MM') >= add_months(trunc(sysdate, 'MM'), -3)
GROUP BY trunc(REPORT_MONTH, 'MM'), MOTIV_TABNUM, PRODUKT;
