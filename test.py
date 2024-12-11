select distinct a.OPERATORID, b.FULLNAME, 
case when a.DEPARTMENTID in (16, 21, 26, 28) then 'mass'
when a.DEPARTMENTID = 22 then 'vip'
when a.DEPARTMENTID = 31 then '2line'
when a.DEPARTMENTID = 23 then 'reten' else 'ckk' end as DEPARTMENT
from ODS.ODS_WIS_CHATOPERATORDEPARTMENT@cdw.prod a
left join ODS.ODS_WIH_CHATOPERATOR@cdw.prod b on a.OPERATORID = b.OPERATORID
where a.DEPARTMENTID in (16, 21, 22, 23, 26, 28, 31, 34)
