SELECT 
       date(date_time) AS date,
       count(*) as cnt
FROM log
where login != 'ADMIN' and type_log ='Вход'
group by date(date_time)
order by date(date_time);
