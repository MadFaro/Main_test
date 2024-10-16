WITH data_with_prev_operid AS (
    SELECT
        chatid,
        msg,
        created,
        operid,
        -- Используем оконную функцию для заполнения пропущенных значений operid
        LAST_VALUE(operid IGNORE NULLS) OVER (PARTITION BY chatid ORDER BY created ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS prev_operid
    FROM
        your_table_name
)
SELECT 
    chatid,
    prev_operid AS operid,  -- Используем предыдущее значение operid
    msg
FROM 
    data_with_prev_operid
WHERE 
    msg LIKE 'Оператор поставил тематику%'  -- Фильтруем только по тематике
ORDER BY 
    created;

