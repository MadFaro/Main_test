with tab_1 as (
select 
trunc(CREATED, 'HH24') as DTM, DEPARTMENT, count(*) as cnt
from (
select 
a.THREADID, a.CREATED, a.MODIFIED, a.STATE, a.OFFLINE_,
case when DEPARTMENTID in (16, 21, 26, 28) then 'mass'
when DEPARTMENTID = 22 then 'vip'
when DEPARTMENTID = 31 then '2line'
when DEPARTMENTID = 23 then 'reten' 
when DEPARTMENTID = 34 then 'ckk' else 'other' end as DEPARTMENT,
ROW_NUMBER() OVER (PARTITION BY a.THREADID ORDER BY b.DTM desc) rn
from ANALYTICS.TOLOG_BI_WEBIM_CHATTHREAD a
left join ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY b on a.THREADID = b.THREADID
where a.OPERATORFULLNAME is null and a.CREATED >= trunc(sysdate))
where rn = 1
group by trunc(CREATED, 'HH24'), DEPARTMENT
)
select 
    coalesce(a.DATE_UPDATE, sysdate + interval '50' second) as date_update,
    coalesce(a.DTM, b.DTM) as dtm,
    coalesce(a.DTM_CHAR, to_char(b.DTM, 'HH24:MI:SS')) as dtm_char,
    coalesce(a.DEPARTMENT, b.DEPARTMENT) as department,
    coalesce(a.CNT_60, 0) as cnt_60,
    coalesce(a.SL_COUNT, 0) + coalesce(b.cnt, 0) as sl_count,
    coalesce(a.CNT, 0) + coalesce(b.cnt, 0) as cnt
from (
    select 
        sysdate + interval '50' second as date_update,
        trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24') as dtm,
        to_char(trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24'), 'HH24:MI:SS') as dtm_char,
        case 
            when DEPARTMENT_ID in (16, 21, 26, 28) then 'mass'
            when DEPARTMENT_ID = 22 then 'vip'
            when DEPARTMENT_ID = 31 then '2line'
            when DEPARTMENT_ID = 23 then 'reten' 
            else 'ckk' 
        end as department,
        sum(case when (START_CHATTING_TIME - GOT_INTO_COMMON_QUEUE_TIME) * 24 * 60 * 60 <= 60 then 1 else 0 end) as cnt_60, 
        count(threadid) as sl_count,
        count(distinct threadid) as cnt
    from ANALYTICS.TOLOG_BI_WEBIM_STATS_SERVICE_LEVEL a
    where DEPARTMENT_ID in (16, 21, 26, 28, 22, 23, 31, 34) 
      and GOT_INTO_COMMON_QUEUE_TIME >= trunc(sysdate)
    group by 
        trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24'), 
        to_char(trunc(GOT_INTO_COMMON_QUEUE_TIME, 'HH24'), 'HH24:MI:SS'),
        case 
            when DEPARTMENT_ID in (16, 21, 26, 28) then 'mass'
            when DEPARTMENT_ID = 22 then 'vip'
            when DEPARTMENT_ID = 31 then '2line'
            when DEPARTMENT_ID = 23 then 'reten' 
            else 'ckk' 
        end
) a
full outer join tab_1 b 
on a.dtm = b.dtm and a.DEPARTMENT = b.DEPARTMENT;

