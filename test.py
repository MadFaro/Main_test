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
    -- Дата первого попадания в категорию
    select tabnum, cnt_category, min(month) as category_start_month
    from base
    group by tabnum, cnt_category
),
work_duration as (
    -- Считаем месяцы работы:
    -- если dt есть и меньше month -> считаем до даты увольнения
    -- если dt = null -> считаем до month и отмечаем "не уволен"
    select 
        base.tabnum,
        base.month,
        base.cnt_category,
        base.dt,
        category_entry.category_start_month,
        trunc(
            months_between(
                case 
                    when base.dt is not null and base.dt < base.month then base.dt
                    else base.month
                end,
                category_entry.category_start_month
            )
        ) as months_worked,
        case 
            when base.dt is null then 'не уволен'
            else 'уволен'
        end as termination_status
    from base
    join category_entry 
        on base.tabnum = category_entry.tabnum 
       and base.cnt_category = category_entry.cnt_category
),
final as (
    -- Присваиваем группу по отработанным месяцам
    select 
        tabnum,
        month,
        cnt_category,
        dt,
        termination_status,
        months_worked,
        case 
            when termination_status = 'не уволен' then 'не уволен'
            when months_worked >= 6 then 'отработали 6 месяцев'
            when months_worked >= 3 then 'отработали 3 месяца'
            else 'менее 3 месяцев'
        end as work_duration_group
    from work_duration
)
select *
from final
order by month, cnt_category, tabnum;
