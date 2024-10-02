select * from ANALYTICS.TOLOG_TMP_SIEBL1
where call_id not in (
select distinct CALL_SIEBEL as call_id from ANALYTICS.TOLOG_IVR_OPER_THEMA
where trunc(EVENT_TIME) = date'2024-09-16'--
)
