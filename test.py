select 
trunc(DT, 'mm') as MONTH_,
trunc(DT, 'iw') as WEEK_,
case when dep = 'mass' then 'Общая линия'
when dep = 'vip' then 'Премиальная линия'
when dep = 'line' then 'Вторая линия' else 'ЦКК' end as GROUP_,
sum(ALL_CHAT) as cnt
from ANALYTICS.TOLOG_WEBIM_CHAT_TABLE
where dt >= trunc(add_months(sysdate-1,-6), 'mm')
group by trunc(DT, 'mm'),  trunc(DT, 'iw'), case when dep = 'mass' then 'Общая линия'
when dep = 'vip' then 'Премиальная линия'
when dep = 'line' then 'Вторая линия' else 'ЦКК' end
order by trunc(DT, 'mm'),  trunc(DT, 'iw'), case when dep = 'mass' then 'Общая линия'
when dep = 'vip' then 'Премиальная линия'
when dep = 'line' then 'Вторая линия' else 'ЦКК' end
