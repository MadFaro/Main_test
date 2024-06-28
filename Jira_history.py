case
    when to_number(to_char(a.DATE_BEGIN_CRIF, 'HH24')) >= 7 and to_number(to_char(a.DATE_BEGIN_CRIF, 'HH24')) < 20 then 'Worktime (7:00 -20:00 МСК)'
    else 'Night (20:00-7:00 МСК)'
end as work_time
