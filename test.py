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
category_entry as (
    -- Находим дату первого попадания в категорию для каждого сотрудника
    select tabnum, cnt_category, min(month) as category_start_month
    from base
    group by tabnum, cnt_category
),
work_duration as (
    -- Считаем количество месяцев, отработанных после попадания в категорию
    select 
        base.tabnum,
        base.month,
        base.cnt_category,
        category_entry.category_start_month,
        trunc(months_between(base.month, category_entry.category_start_month)) as months_worked
    from base
    join category_entry on base.tabnum = category_entry.tabnum and base.cnt_category = category_entry.cnt_category
),
final as (
    -- Присваиваем группы по отработанным месяцам
    select 
        tabnum,
        month,
        cnt_category,
        months_worked,
        case 
            when months_worked >= 6 then 'отработали 6 месяцев'
            when months_worked >= 3 then 'отработали 3 месяца'
            else 'менее 3 месяцев'
        end as work_duration_group
    from work_duration
)
select *
from final
order by month, cnt_category, tabnum;

