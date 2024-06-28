update analytics.kdi_ipoteka_final_with_time_fix
set DATE_BEGIN_CRIF_FIX=DATE_IN_WORK_FIX-
(180-((extract (hour from DATE_BEGIN_CRIF_FIX)-17)*60+extract (minute from DATE_BEGIN_CRIF_FIX))+
case when to_char(DATE_IN_WORK_FIX, 'Day') in ('Воскресенье', 'Суббота    ') 
then (extract (hour from DATE_IN_WORK_FIX)-8)*60+extract (minute from DATE_IN_WORK_FIX)
else (extract (hour from DATE_IN_WORK_FIX)-7)*60+extract (minute from DATE_IN_WORK_FIX) end)/24/60
where extract (hour from (DATE_IN_WORK_FIX-DATE_BEGIN_CRIF_FIX))>2
and extract (hour from (DATE_IN_WORK_FIX-DATE_BEGIN_CRIF_FIX))<18
and extract (hour from DATE_BEGIN_CRIF_FIX)>=17
and 180-((extract (hour from DATE_BEGIN_CRIF_FIX)-17)*60+extract (minute from DATE_BEGIN_CRIF_FIX))+
case when to_char(DATE_IN_WORK_FIX, 'Day') in ('Воскресенье', 'Суббота    ') 
then (extract (hour from DATE_IN_WORK_FIX)-8)*60+extract (minute from DATE_IN_WORK_FIX)
else (extract (hour from DATE_IN_WORK_FIX)-7)*60+extract (minute from DATE_IN_WORK_FIX) end<180
