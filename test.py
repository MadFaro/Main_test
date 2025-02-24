select a.*, b.DT from (
select month,TABNUM,
case when cnt >= 3 then 'месяцев подряд 3+'
when cnt = 2 then 'месяцев подряд 2'
else 'месяцев подряд 1' end as cnt_category from (
select TABNUM, month,
count(*) over (partition by TABNUM, grp order by month rows between unbounded preceding and current row) as cnt from (
select TABNUM, month,
row_number() over (partition by TABNUM order by month) as rn,
add_months(month, -row_number() over (partition by TABNUM order by month)) as grp
from analytics.tolog_lights_finally
where rank_sum = 1))) a
left join (Select PERSON_NUMBER, max(DATE_END) as DT
from analytics.NP_PERSONAL_REPORT
where STATUS='Не работает'
group by PERSON_NUMBER) b on a.TABNUM = b.PERSON_NUMBER
order by a.month, a.cnt_category, a.TABNUM
