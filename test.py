case when TIME_BACK <= 5 then '0-5 min'
when TIME_BACK <= 10 THEN '6-10 min'
when TIME_BACK <= 15 THEN '11-15 min'
when TIME_BACK <= 20 THEN '16-20 min'
when TIME_BACK <= 30 THEN '21-30 min' ELSE '31+ min' END AS TIME_RANK
