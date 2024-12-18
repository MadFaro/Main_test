
with filtered_data as (
    select 
        "FI_", 
        "Type_", 
        "Group_", 
        "Direction_", 
        "Day_", 
        trunc("Day_") as day_only,
        extract(year from "Day_") as year_,
        extract(month from "Day_") as month_,
        case 
            when trunc("Day_") - lag(trunc("Day_")) over (partition by "FI_", "Type_", "Group_", "Direction_" order by "Day_") > 1 then 1 
            else 0 
        end as new_group
    from 
        ANALYTICS.TOLOG_OPERATORS_SICK
    where 
        "Type_" = 'Больничный - неоплачиваемый' -- фильтр по типу (если нужно)
        and "Day_" >= trunc(sysdate) - 60 -- последние 60 дней
),
grouped_data as (
    select 
        "FI_", 
        "Type_", 
        "Group_", 
        "Direction_", 
        year_, 
        month_, 
        day_only,
        sum(new_group) over (partition by "FI_", "Type_", "Group_", "Direction_" order by day_only) as group_id
    from 
        filtered_data
),
final_data as (
    select 
        "FI_", 
        "Type_", 
        "Group_", 
        "Direction_", 
        count(distinct group_id) as sick_count, -- количество уникальных больничных (штук)
        count(*) as sick_days -- количество дней больничных
    from 
        grouped_data
    group by 
        "FI_", "Type_", "Group_", "Direction_"
),
ranked_data as (
    select 
        "FI_", 
        "Type_", 
        "Group_", 
        "Direction_", 
        sick_count, 
        sick_days,
        rank() over (partition by "Direction_" order by sick_count desc, sick_days desc) as rank
    from 
        final_data
)
select 
    "FI_", 
    "Type_", 
    "Group_", 
    "Direction_", 
    sick_count, 
    sick_days
from 
    ranked_data
where 
    rank <= 5 -- только ТОП-5 сотрудников в каждой дирекции
order by 
    "Direction_", sick_count desc, sick_days desc;
