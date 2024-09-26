select a.*, b.FIRSTNAME,
d.SUBJ1, d.PRODUCT1, d.REZ1
from ANALYTICS.TOLOG_IVR_OPER a
left join ODS.ODS_CSC_PERSON@cdw.prod b on a.AGENT_ID = b.LOGINNAME
left join ANALYTICS.KDI_SIEBEL_PAST d on trunc(a.EVENT_TIME) = trunc(d.dt) and d.dt > a.EVENT_TIME and lower(b.FIRSTNAME) = lower(d.OPERATOR) and d.type = 'Вызов - входящий'
