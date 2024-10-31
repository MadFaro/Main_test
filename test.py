    select 
    THREADHISTORYID, 
    THREADID, 
    NUMBER as NUMBER_, 
    DTM, 
    STATE, 
    OPERATORID, 
    DEPARTMENTID, 
    EVENT from chatthreadhistory where DTM >= %S

ANALYTICS.TOLOG_BI_WEBIM_CHATTHREADHISTORY
