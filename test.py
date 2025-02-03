create table tolog_praic_lict_opros as
SELECT
trunc(REPORT_MONTH, 'mm') as REPORT_MONTH, MOTIV_TABNUM, PRODUKT, COUNT(DISTINCT DOG) as dog_cnt
FROM BALKHOVITIAV.VIEW_MOTIV_PRAIC_LICT_OPROS
WHERE trunc(REPORT_MONTH, 'mm') >=add_months(trunc(sysdate,'mm'),-3)
GROUP BY trunc(REPORT_MONTH, 'mm'), MOTIV_TABNUM, PRODUKT
Error report -
ORA-01830: шаблон формата даты завершается перед преобразованием всей строки ввода
01830. 00000 -  "date format picture ends before converting entire input string"
*Cause:    
*Action:
