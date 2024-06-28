select a.*,
case when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=8 and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<20 then  DATE_BEGIN_CRIF  
 when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<8 then  trunc(DATE_BEGIN_CRIF)+8/24 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=20 then  trunc(DATE_BEGIN_CRIF)+1+8/24 
 
 when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=7 and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<20 then  DATE_BEGIN_CRIF  
 when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<7 then  trunc(DATE_BEGIN_CRIF)+7/24 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=20 then  trunc(DATE_BEGIN_CRIF)+1+7/24 
  else null end as DATE_BEGIN_CRIF_fix,

case when DATE_IN_WORK>=DATE_BEGIN_CRIF and DATE_IN_WORK<case when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=8 and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<20 then  DATE_BEGIN_CRIF  
 when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<8 then  trunc(DATE_BEGIN_CRIF)+8/24 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=20 then  trunc(DATE_BEGIN_CRIF)+1+8/24 
 
 when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=7 and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<20 then  DATE_BEGIN_CRIF  
 when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<7 then  trunc(DATE_BEGIN_CRIF)+7/24 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=20 then  trunc(DATE_BEGIN_CRIF)+1+7/24 
  else null end then 
  case when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<8 then trunc(DATE_BEGIN_CRIF)+8/24+1/(24*60) 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=8 then trunc(DATE_BEGIN_CRIF)+1+8/24+1/(24*60) 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))<7 then trunc(DATE_BEGIN_CRIF)+7/24+1/(24*60) 
  when to_char(DATE_BEGIN_CRIF, 'Day', 'NLS_DATE_LANGUAGE = ''RUSSIAN''') not in ('Воскресенье', 'Суббота    ') and extract (hour from cast(DATE_BEGIN_CRIF as timestamp))>=7 then trunc(DATE_BEGIN_CRIF)+1+7/24+1/(24*60) 
   end
   else DATE_IN_WORK end as DATE_IN_WORK_FIX
 from analytics.kdi_ipoteka_final a
