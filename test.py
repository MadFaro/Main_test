with tab_1 as (
select "FI_", "Type_", "Group_", year_, month_, "Day_",
sum(new_group) over (partition by "FI_", "Type_", "Group_", year_, month_ order by "Day_") as group_id from (
select "Type_", "Group_", "FI_", "Start_", "End_", "Direction_", "Day_",
extract(year from "Day_") as year_,
extract(month from "Day_") as month_,
case when trunc("Day_") - lag(trunc("Day_")) over (partition by "FI_", "Type_", "Group_", extract(year from "Day_"), extract(month from "Day_") order by "Day_") > 1 then 1 else 0 end as new_group
from ANALYTICS.TOLOG_OPERATORS_SICK))
select"FI_", "Type_", "Group_", year_, month_, count(distinct group_id) as status_count
from tab_1
group by "FI_", "Type_", "Group_", year_, month_
order by "FI_", year_, month_;


"штуки больничных" и по умолчанию выводить на график ТОП 5 ФИО с каждой дирекции с максимальным количеством дней больничных и штук больничных за последние 60 дней. с указанием значения, дирекции и групп
