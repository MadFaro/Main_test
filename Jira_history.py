WITH chat_counts AS (
    SELECT 
        TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') AS minute_slot,
        COUNT(chat_id) AS chat_count
    FROM 
        your_table
    GROUP BY 
        TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI')
)
SELECT 
    minute_slot, 
    chat_count
FROM 
    chat_counts
WHERE 
    chat_count = (SELECT MAX(chat_count) FROM chat_counts);
