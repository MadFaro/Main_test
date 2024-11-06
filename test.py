select trunc(TIME_CLOSE, 'mm') as mm, round(DT-TIME_CLOSE) as dt, count(distinct CALL_ID) from (
select distinct CLIENT_DID, TIME_CLOSE, CALL_ID, DT from ANALYTICS.TOLOG_CLOSED_CARDS_CC_CALL)
group by trunc(TIME_CLOSE, 'mm'), round(DT-TIME_CLOSE)
order by trunc(TIME_CLOSE, 'mm'), round(DT-TIME_CLOSE)
