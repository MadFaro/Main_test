with grouped_periods as (
    select
        fi_,
        type_,
        group_,
        start_,
        end_,
        direction_,
        day_,
        extract(year from day_) as year_,
        extract(month from day_) as month_,
        sum(case 
                when trunc(day_) - lag(trunc(day_)) over (partition by fi_, type_, group_, extract(year from day_), extract(month from day_) order by day_) > 1 then 1 
                else 0 
            end) over (partition by fi_, type_, group_, extract(year from day_), extract(month from day_) order by day_) as group_id
    from 
        your_table
)
select 
    fi_,
    type_,
    group_,
    year_,
    month_,
    count(distinct group_id) as status_count
from 
    grouped_periods
group by 
    fi_,
    type_,
    group_,
    year_,
    month_
order by 
    fi_, year_, month_;

