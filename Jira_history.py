SELECT 
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') AS minute_slot,
    COUNT(chat_id) AS chat_count
FROM 
    your_table
GROUP BY 
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI')
ORDER BY 
    chat_count DESC
FETCH FIRST 1 ROWS ONLY;

