with tab_1 as (
select client_did, deact_description, clnt_segment,
cast(int_create_date as date) as int_create_date, dozvon
from analytics.rap_tech_voronka_polotn 
where int_create_date >= date '2024-06-01' 
and template_code in ('pk_difrate_35', 'pk_topup_35', 'tm_cc_35')
),
tab_2 as (
select client_did, int_create_date, dozvon,
lag(int_create_date) over (partition by client_id order by int_create_date) as prev_date
from tab_1
),
tab_3 as (
select client_did, int_create_date, prev_date, dozvon,
case when prev_date is not null then (date_added - prev_date) else null end as day_diff
from tab_2
),
tab_4 as (
select client_did, int_create_date, prev_date, day_diff, dozvon,
case when prev_date is null then '0 повторений'
when day_diff between 1 and 14 then '1-14 дней'
when day_diff between 15 and 20 then '15-20 дней'
when day_diff between 21 and 25 then '21-25 дней'
when day_diff between 26 и 30 then '26-30 дней'
else 'больше 30 дней' end as interval_category
from tab_3
)
select
trunc(date_added, 'mm') as month_,
interval_category,
count(*) as count_of_repeats,
sum(case when dozvon = 1 then 1 else 0 end) as count_of_dozvons,
from tab_4
group by to_char(trunc(date_added, 'mm'), 'yyyy-mm'), interval_category
order by month_, interval_category;

ORA-00905: отсутствует ключевое слово
00905. 00000 -  "missing keyword"
*Cause:    
*Action:
Error at Line: 24 Column: 47
