WITH green_zone AS (
    -- 1. Отбираем сотрудников в зеленой зоне
    SELECT 
        FIO,
        TRUNC(MONTH, 'MM') AS month_start,  -- Берём первый день месяца
        RANK_SUM
    FROM your_table
    WHERE RANK_SUM = 1
),
seq_groups AS (
    -- 2. Находим группы последовательных месяцев, используя разницу дат и row_number
    SELECT 
        FIO,
        month_start,
        ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY month_start) AS rn,
        ADD_MONTHS(month_start, -ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY month_start)) AS grp
    FROM green_zone
),
grouped_sequences AS (
    -- 3. Группируем последовательности и находим их длину
    SELECT 
        FIO,
        MIN(month_start) AS start_month,
        MAX(month_start) AS end_month,
        COUNT(*) AS seq_length
    FROM seq_groups
    GROUP BY FIO, grp
),
final_counts AS (
    -- 4. Считаем, сколько сотрудников закончили последовательность в каждом месяце и её длина
    SELECT 
        TO_CHAR(end_month, 'Month', 'NLS_DATE_LANGUAGE=RUSSIAN') AS month_name,
        CASE 
            WHEN seq_length >= 3 THEN 'Месяцев подряд 3+'
            WHEN seq_length = 2 THEN 'Месяцев подряд 2'
            ELSE 'Месяцев подряд 1'
        END AS seq_category,
        COUNT(DISTINCT FIO) AS employee_count
    FROM grouped_sequences
    GROUP BY 
        TO_CHAR(end_month, 'Month', 'NLS_DATE_LANGUAGE=RUSSIAN'), 
        CASE 
            WHEN seq_length >= 3 THEN 'Месяцев подряд 3+'
            WHEN seq_length = 2 THEN 'Месяцев подряд 2'
            ELSE 'Месяцев подряд 1'
        END
)
-- 5. Преобразуем данные в итоговую таблицу (PIVOT)
SELECT *
FROM final_counts
PIVOT (
    SUM(employee_count)
    FOR month_name IN ('Июль' AS июль, 'Август' AS август, 'Сентябрь' AS сентябрь, 'Октябрь' AS октябрь, 'Ноябрь' AS ноябрь, 'Декабрь' AS декабрь)
)
ORDER BY 
    CASE seq_category 
        WHEN 'Месяцев подряд 3+' THEN 1
        WHEN 'Месяцев подряд 2' THEN 2
        ELSE 3 
    END;
