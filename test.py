select trunc(CREATED, 'mm') as created, sum(case when FCR=1 then 1 else 0 end)/count(*) as fcr from (
select 
a.OPERATORFULLNAME, a.OPERATORID, 
a.CREATED,
a.VISITORID,
COUNT(TRUNC(CREATED)) OVER(PARTITION BY TRUNC(CREATED), a.VISITORID) AS FCR
from ODS.ODS_WIS_CHATTHREAD@cdw.prod a
where a.CREATED>=date'2023-12-01'
and threadid in (select distinct threadid from ODS.ODS_WIS_chatthreadhistory@cdw.prod
where dtm >=date'2023-12-01' and DEPARTMENTID in (22))
)
group by trunc(CREATED, 'mm')
order by trunc(CREATED, 'mm')
