SELECT start_time, end_time, MAX(parallel_chats) AS max_parallel_chats
FROM (
    SELECT start_time, end_time, SUM(case when chat_count > 3 then 3 else chat_count end) OVER (ORDER BY start_time) AS parallel_chats
    FROM (
        SELECT start_time, end_time, COUNT(*) OVER (ORDER BY start_time, end_time) AS chat_count
        FROM your_table
        WHERE start_time >= :start_date
        AND end_time <= :end_date
    )
)
GROUP BY start_time, end_time;
