WITH ranked_data AS (
    SELECT event_time, 
           event_type_id,
           call_id,
           LEAD(event_time) OVER (PARTITION BY call_id ORDER BY event_time) AS next_event_time,
           RANK() OVER (PARTITION BY call_id ORDER BY event_time) AS event_rank
    FROM your_existing_table_name -- замените your_existing_table_name на имя вашей таблицы
)
SELECT event_type_id,
       SUM(EXTRACT(DAY FROM (next_event_time - event_time)) * 86400 + 
           EXTRACT(HOUR FROM (next_event_time - event_time)) * 3600 +
           EXTRACT(MINUTE FROM (next_event_time - event_time)) * 60 +
           EXTRACT(SECOND FROM (next_event_time - event_time))) AS total_time,
       COUNT(DISTINCT call_id) AS total_clients
FROM ranked_data
WHERE event_rank = 1
GROUP BY event_type_id;

