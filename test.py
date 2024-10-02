with tab_1 as (
select 
call_id,
number_,
max(event_time) as end_time
from ods.ods_bpu_int_ivrchd_events@cdw.prod
where number_ = '9063705301'
group by call_id, number_
),
tab_2 as (
select 
call_id as prev_call_id,
number_,
end_time as prev_end_time,
lead(end_time) over (partition by number_ order by end_time) as next_start_time
from tab_1
)
select 
number_, 
prev_call_id, 
prev_end_time, 
next_start_time,
round((next_start_time - prev_end_time) * 1440) as diff_minutes,
case 
  when next_start_time is null then 'не вернулся вообще'
  when round((next_start_time - prev_end_time) * 1440) <= 1 then '1 минута'
  when round((next_start_time - prev_end_time) * 1440) <= 2 then '2 минуты'
  when round((next_start_time - prev_end_time) * 1440) <= 5 then '5 минут'
  when round((next_start_time - prev_end_time) * 1440) <= 10 then '10 минут'
  when round((next_start_time - prev_end_time) * 1440) <= 15 then '15 минут'
  when round((next_start_time - prev_end_time) * 1440) <= 20 then '20 минут'
  when round((next_start_time - prev_end_time) * 1440) <= 30 then '30 минут'
  else 'более 30 минут'
end as return_time_category
from tab_2
order by prev_end_time;

