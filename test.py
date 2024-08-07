create table analytics.tolog_ivr_event as
with tab_1 as (
select trunc(event_time) as event_date,
event_type_id,event_time,
lead(event_time) over (partition by call_id order by rank) as next_event_time
from ods.ods_bpu_int_ivrchd_events@cdw.prod),
tab_2 as (
select event_date,event_type_id,
sum(case when next_event_time is not null then (next_event_time - event_time) * 24 * 60 * 60 else 0 end) as total_time_spent,
count(*) as event_count
from tab_1
group by event_date, event_type_id),
tab_3 as (
select trunc(event_time) as event_date,
event_type_id, count(distinct call_id) as call_count
from ods.ods_bpu_int_ivrchd_events@cdw.prod
group by trunc(event_time), event_type_id),
tab_4 as (
select event_date,event_type_id,
total_time_spent / event_count as avg_time_spent
from tab_2)
select a.event_date, a.event_type_id,
a.call_count, b.total_time_spent, d.avg_time_spent
from tab_3 a
left join tab_2 b on a.event_date = b.event_date and a.event_type_id = b.event_type_id
left join tab_4 d on a.event_date = d.event_date and a.event_type_id = d.event_type_id
order by a.event_date, a.event_type_id;
