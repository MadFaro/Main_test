with tab_1 as (
select 
trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24') as dtm,
case when DEPARTMENT_ID in (16, 21, 26, 28) then 'mass'
when DEPARTMENT_ID = 22 then 'vip'
when DEPARTMENT_ID = 31 then '2line'
when DEPARTMENT_ID = 23 then 'reten' else 'ckk' end as DEPARTMENT,
sum(case when (START_CHATTING_TIME-GOT_INTO_COMMON_QUEUE_TIME)*24*60*60<=60 then 1 else 0 end) as cnt_60, 
count(threadid) as sl_count
from ANALYTICS.TOLOG_BI_WEBIM_STATS_SERVICE_LEVEL a
where DEPARTMENT_ID in (16, 21, 26, 28, 22, 23, 31, 34) and GOT_INTO_COMMON_QUEUE_TIME >= trunc(sysdate)
group by trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24'), case when DEPARTMENT_ID in (16, 21, 26, 28) then 'mass'
when DEPARTMENT_ID = 22 then 'vip'
when DEPARTMENT_ID = 31 then '2line'
when DEPARTMENT_ID = 23 then 'reten' else 'ckk' end
order by case when DEPARTMENT_ID in (16, 21, 26, 28) then 'mass'
when DEPARTMENT_ID = 22 then 'vip'
when DEPARTMENT_ID = 31 then '2line'
when DEPARTMENT_ID = 23 then 'reten' else 'ckk' end, trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24')
)
select a.date_update, a.dtm, a.dtm_char, a.department, NVL(b.cnt_60, 0) as cnt_60, NVL(b.sl_count, a.cnt) as sl_count, a.cnt from (
select 
sysdate + interval '50' second as date_update,
trunc(DTM, 'HH24') as dtm,
to_char(trunc(DTM, 'HH24'), 'HH24:MI:SS') as dtm_char,
case when DEPARTMENTID in (16, 21, 26, 28) then 'mass'
when DEPARTMENTID = 22 then 'vip'
when DEPARTMENTID = 31 then '2line'
when DEPARTMENTID = 23 then 'reten' else 'ckk' end as DEPARTMENT,
count(distinct threadid) as cnt
from ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY
where DEPARTMENTID in (16, 21, 26, 28, 22, 23, 31, 34) and DTM >= trunc(sysdate)
group by trunc(DTM, 'HH24'), to_char(trunc(DTM, 'HH24'), 'HH24:MI:SS'),
case when DEPARTMENTID in (16, 21, 26, 28) then 'mass'
when DEPARTMENTID = 22 then 'vip'
when DEPARTMENTID = 31 then '2line'
when DEPARTMENTID = 23 then 'reten' else 'ckk' end) a
left join tab_1 b on a.dtm = b.dtm and a.DEPARTMENT = b.DEPARTMENT

