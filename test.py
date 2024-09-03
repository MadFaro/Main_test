case when extract (hour from CLIENT_TIME)>=9 and extract (hour from CLIENT_TIME)<22 then 'YES' else 'NO' end as CLIENT_WROK_TIME
