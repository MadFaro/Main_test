select * from (
select MONTH,
CASE WHEN cnt >= 3 THEN 'Месяцев подряд 3+'
WHEN cnt = 2 THEN 'Месяцев подряд 2'
ELSE 'Месяцев подряд 1' END AS cnt_category,
COUNT(DISTINCT FIO) AS employee_cnt from (
select FIO, MONTH,
COUNT(*) OVER (PARTITION BY FIO, grp ORDER BY MONTH ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cnt from (
select FIO, MONTH,
ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY MONTH) AS rn,
ADD_MONTHS(MONTH, -ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY MONTH)) AS grp from (
select FIO, MONTH
from ANALYTICS.TOLOG_LIGHTS_FINALLY
where RANK_SUM = 1)))
group by MONTH, 
CASE WHEN cnt >= 3 THEN 'Месяцев подряд 3+'
WHEN cnt = 2 THEN 'Месяцев подряд 2'
ELSE 'Месяцев подряд 1' END)
order by MONTH, CNT_CATEGORY
