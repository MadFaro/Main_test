with tab_1 as (
select 
client_did as client_id,
deact_description,
clnt_segment,
cast(int_create_date as date) as date_added,
dozvon
from 
analytics.rap_tech_voronka_polotn 
where 
int_create_date >= date '2024-06-01' 
and template_code in ('pk_difrate_35', 'pk_topup_35', 'tm_cc_35')
and (deact_description is null or deact_description not in ('Причина1', 'Причина2'))
and clnt_segment in ('Сегмент1', 'Сегмент2')
),
tab_2 as (
select 
client_id, 
date_added,
dozvon,
lag(date_added) over (partition by client_id order by date_added) as prev_date
from 
tab_1
),
tab_3 as (
select 
client_id, 
date_added, 
prev_date,
dozvon,
case 
when prev_date is not null then (date_added - prev_date) 
else null 
end as day_diff
from 
tab_2
),
tab_4 as (
select 
client_id, 
date_added, 
prev_date, 
day_diff,
dozvon,
case 
when prev_date is null then '0 повторений'
when day_diff between 1 and 14 then '1-14 дней'
when day_diff between 15 and 20 then '15-20 дней'
when day_diff between 21 and 25 then '21-25 дней'
when day_diff between 26 и 30 then '26-30 дней'
else 'больше 30 дней' 
end as interval_category
from 
tab_3
)
select
to_char(trunc(date_added, 'mm'), 'yyyy-mm') as month,
interval_category,
count(*) as count_of_repeats,
sum(case when dozvon = 1 then 1 else 0 end) as count_of_dozvons,
round(sum(case when dozvon = 1 then 1 else 0 end) / count(*) * 100, 2) as percent_of_dozvons
from 
tab_4
group by 
to_char(trunc(date_added, 'mm'), 'yyyy-mm'), 
interval_category
order by 
month, interval_category;
