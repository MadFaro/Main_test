WITH ranked_data AS (
    SELECT event_time, 
           type_ecent,
           call_id,
           LEAD(event_time) OVER (PARTITION BY call_id ORDER BY event_time) AS next_event_time,
           RANK() OVER (PARTITION BY call_id ORDER BY event_time) AS event_rank
    FROM your_existing_table_name -- замените your_existing_table_name на имя вашей таблицы
)
SELECT type_ecent,
       SUM((next_event_time - event_time) * 86400) AS total_time_seconds,
       COUNT(DISTINCT call_id) AS total_clients
FROM ranked_data
WHERE event_rank = 1
GROUP BY type_ecent;
