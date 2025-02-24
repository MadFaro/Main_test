with base as (
    select a.*, b.dt 
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
),
min_dates as (
    select tabnum, min(month) as min_month
    from base
    group by tabnum
)
select 
    base.*, 
    case 
        when base.dt is not null then months_between(base.dt, min_dates.min_month)
        else null
    end as months_from_first_month
from base
join min_dates on base.tabnum = min_dates.tabnum
order by base.month, base.cnt_category, base.tabnum;
