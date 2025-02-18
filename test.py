WITH base_data AS (
    select 
        THREADID, CREATED, MODIFIED, STATE, OFFLINE_, DEPARTMENT, 
        case 
            when DEPARTMENT in ('ckk', '2line') then (sysdate + interval '50' second - DTM) * 1440 
            else (sysdate + interval '50' second - CREATED) * 1440 
        end as AWAIT_TIME
    from (
        select 
            a.THREADID, a.CREATED, a.MODIFIED, a.OFFLINE_,
            case 
                when DEPARTMENTID in (16, 21, 26, 28) then 'mass'
                when DEPARTMENTID = 22 then 'vip'
                when DEPARTMENTID = 31 then '2line'
                when DEPARTMENTID = 23 then 'reten' 
                when DEPARTMENTID = 34 then 'ckk' 
                else 'other' 
            end as DEPARTMENT,
            b.dtm,
            b.STATE,
            ROW_NUMBER() OVER (PARTITION BY a.THREADID ORDER BY b.DTM desc) rn
        from ANALYTICS.TOLOG_BI_WEBIM_CHATTHREAD a
        left join ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY b 
            on a.THREADID = b.THREADID
        where a.STATE = 'queue' and a.CREATED >= trunc(sysdate)
    ) 
    where rn = 1 and STATE = 'queue'
),
high_await_chats AS (
    SELECT COUNT(*) as cnt 
    FROM base_data 
    WHERE AWAIT_TIME > 150
)
SELECT * 
FROM base_data
WHERE (SELECT cnt FROM high_await_chats) > 3 
    OR AWAIT_TIME <= 150;
