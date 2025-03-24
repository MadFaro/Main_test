with tab_1 as (
select call_id,number_, VARIABLE_7, max(event_time) as end_time
from ods.ods_bpu_int_ivrchd_events@cdw.prod
where START_EVENT_TIME >=date'2025-03-01' and VARIABLE_7 is not null and AGENT_ID is null
group by call_id, number_, VARIABLE_7
)
select 
call_id as prev_call_id, number_,
end_time as prev_end_time,
lead(end_time) over (partition by number_ order by end_time) as next_start_time
from tab_1
