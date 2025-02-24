select * from (
select month,fio,
case when cnt >= 3 then 'месяцев подряд 3+'
when cnt = 2 then 'месяцев подряд 2'
else 'месяцев подряд 1' end as cnt_categoryfrom (
select fio, month,
count(*) over (partition by fio, grp order by month rows between unbounded preceding and current row) as cntfrom (
select fio, month,
row_number() over (partition by fio order by month) as rn,
add_months(month, -row_number() over (partition by fio order by month)) as grp
from analytics.tolog_lights_finally
where rank_sum = 1)))
order by month, cnt_category, fio;
