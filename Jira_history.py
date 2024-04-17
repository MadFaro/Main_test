WITH chat_intervals AS (
    SELECT
        chat_id,
        operator_id,
        visitor_id,
        chat_date,
        LAG(chat_date) OVER (PARTITION BY operator_id ORDER BY chat_date) AS prev_chat_date
    FROM
        your_table_name
)
SELECT
    operator_id,
    CASE
        WHEN time_interval_minutes <= 5 THEN '0-5 min'
        WHEN time_interval_minutes <= 10 THEN '6-10 min'
        WHEN time_interval_minutes <= 15 THEN '11-15 min'
        WHEN time_interval_minutes <= 20 THEN '16-20 min'
        WHEN time_interval_minutes <= 30 THEN '21-30 min'
        WHEN time_interval_minutes <= 40 THEN '31-40 min'
        WHEN time_interval_minutes <= 50 THEN '41-50 min'
        ELSE '51+ min'
    END AS time_interval,
    COUNT(*) AS chat_count,
    COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY operator_id) AS ratio
FROM (
    SELECT
        operator_id,
        visitor_id,
        chat_date - LAG(chat_date) OVER (PARTITION BY operator_id, visitor_id ORDER BY chat_date) * 24 * 60 AS time_interval_minutes
    FROM
        chat_intervals
) intervals
GROUP BY
    operator_id,
    CASE
        WHEN time_interval_minutes <= 5 THEN '0-5 min'
        WHEN time_interval_minutes <= 10 THEN '6-10 min'
        WHEN time_interval_minutes <= 15 THEN '11-15 min'
        WHEN time_interval_minutes <= 20 THEN '16-20 min'
        WHEN time_interval_minutes <= 30 THEN '21-30 min'
        WHEN time_interval_minutes <= 40 THEN '31-40 min'
        WHEN time_interval_minutes <= 50 THEN '41-50 min'
        ELSE '51+ min'
    END
ORDER BY
    operator_id,
    time_interval;
