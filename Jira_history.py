С разработчиками вебим и графана обсуждаем, как получить средневзвешанный сл, но показатель выше вебима на 15-20%

Можешь посмотреть запрос и сказать, что в нем может быть не так?

Сам запрос:
select 
    JSON_EXTRACT(t.json,'$.startPage.departmentKey') AS "dep",  
    #COUNT(1) AS "all", 
    #count(CASE 
       # when (JSON_EXTRACT(t.json,'$.startPage.departmentKey') LIKE '"roznichnyi_biznes%' and TIMESTAMPDIFF(second, c2.dtm, COALESCE(c1.dtm, NOW()))<=60)  
      #  OR (JSON_EXTRACT(t.json,'$.startPage.departmentKey') not LIKE '"roznichnyi_biznes%' and TIMESTAMPDIFF(second, c2.dtm, COALESCE(c1.dtm, NOW()))<=20) 
     #   then 1 
    #END) AS "SL",
    count(CASE 
        when (JSON_EXTRACT(t.json,'$.startPage.departmentKey') LIKE '"roznichnyi_biznes%' and TIMESTAMPDIFF(second, c2.dtm, COALESCE(c1.dtm, NOW()))<=60)  
        OR (JSON_EXTRACT(t.json,'$.startPage.departmentKey') not LIKE '"roznichnyi_biznes%' and TIMESTAMPDIFF(second, c2.dtm, COALESCE(c1.dtm, NOW()))<=20) 
        then 1 
    END) / COUNT(1) AS "SL_to_all_ratio"
from chatthread t 
left JOIN chatthreadhistory c1 ON c1.threadhistoryid = (SELECT MIN(c.threadhistoryid) from chatthreadhistory c WHERE c.threadid = t.threadid AND c.state="chatting" AND c.operatorid NOT IN (SELECT r.operatorid  
FROM robot r)) 
left JOIN chatthreadhistory c2 ON c2.threadhistoryid = (SELECT MIN(c.threadhistoryid) from chatthreadhistory c WHERE c.threadid = t.threadid AND c.state="queue" AND c.operatorid NOT IN (SELECT r.operatorid  
FROM robot r)) 
WHERE t.created >= CURDATE() AND t.created < DATE_ADD(CURDATE(), INTERVAL 1 DAY) 
AND JSON_EXTRACT(t.json,'$.startPage.departmentKey') IS NOT NULL 
GROUP BY JSON_EXTRACT(t.json,'$.startPage.departmentKey')

