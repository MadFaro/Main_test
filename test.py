select trunc(DT, 'mm') as created, sum(case when FCR=1 then 1 else 0 end)/count(*) as fcr from (
select 
a.call_id, a.OPERATOR,
a.DT,
a.CLIENT_ID,
COUNT(TRUNC(DT)) OVER(PARTITION BY TRUNC(DT), a.CLIENT_ID) AS FCR
from ANALYTICS.KDI_SIEBEL_PAST a
where a.DT>=date'2024-01-01' and a.CLIENT_ID is not null and a.TYPE = 'Вызов - входящий' and DIRECTION = 'ДДО')
group by trunc(DT, 'mm')
order by trunc(DT, 'mm')
