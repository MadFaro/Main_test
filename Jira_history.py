WITH chats_with_gaps AS (
    SELECT
        chat_id,
        visitor_id,
        chat_date,
        LAG(chat_date) OVER (PARTITION BY visitor_id, TRUNC(chat_date) ORDER BY chat_date) AS prev_chat_date
    FROM
        your_table_name
)
SELECT
    TRUNC(chat_date) AS chat_date,
    COUNT(CASE WHEN prev_chat_date IS NULL OR (chat_date - prev_chat_date) * 24 >= 2 THEN 1 END) AS chat_count
FROM
    chats_with_gaps
GROUP BY
    TRUNC(chat_date)
ORDER BY
    TRUNC(chat_date);
