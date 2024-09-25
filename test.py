SELECT sql_text, last_load_time
FROM v$sql
ORDER BY last_load_time DESC;

