select /*+ PARALLEL(8) */
DTM, FORM_TITLE, DESCRIPTION, FIRSTNAME, SCORE from (
select 
trunc(LOCAL_START_TIME) as DTM,
FORM_TITLE,
GROUP_NAME as DESCRIPTION,
EVALUATEE_NAME as FIRSTNAME,
SCORE,
ROW_NUMBER() OVER (PARTITION BY EVALUATEE_NAME, LOCAL_START_TIME ORDER BY LOCAL_START_TIME) as rnk
from ods.ods_vrn_evaluations_scores_all@cdw.prod
where LOCAL_START_TIME >= trunc(add_months(sysdate,-6), 'mm') and FORM_TITLE = 'Чек лист ДДО')
where rnk = 1
