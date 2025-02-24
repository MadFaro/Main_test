select 
    a.*, 
    b.dt,
    case 
        when b.dt is null then 'не уволился'
        when months_between(b.dt, a.month) >= 6 then 'отработал 6 месяцев или более'
        when months_between(b.dt, a.month) >= 3 then 'отработал 3 месяца'
        else 'менее 3 месяцев'
    end as work_duration_category
from (
    select month, tabnum,
    case 
        when cnt >= 3 then 'месяцев подряд 3+'
        when cnt = 2 then 'месяцев подряд 2'
        else 'месяцев подряд 1' 
    end as cnt_category 
    from (
        select tabnum, month,
        count(*) over (partition by tabnum, grp order by month rows between unbounded preceding and current row) as cnt
        from (
            select tabnum, month,
            row_number() over (partition by tabnum order by month) as rn,
            add_months(month, -row_number() over (partition by tabnum order by month)) as grp
            from analytics.tolog_lights_finally
            where rank_sum = 1
        )
    )
) a
left join (
    select person_number, max(date_end) as dt
    from analytics.np_personal_report
    where status = 'Не работает'
    group by person_number
) b on a.tabnum = b.person_number
order by a.month, a.cnt_category, a.tabnum;
