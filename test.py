WITH green_zone AS (
    -- 1. Отбираем сотрудников в зеленой зоне
    SELECT 
        FIO,
        MONTH
    FROM your_table
    WHERE RANK_SUM = 1
),
seq_groups AS (
    -- 2. Определяем группы последовательных месяцев
    SELECT 
        FIO,
        MONTH,
        ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY MONTH) AS rn,
        ADD_MONTHS(MONTH, -ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY MONTH)) AS grp
    FROM green_zone
),
grouped_sequences AS (
    -- 3. Считаем длину каждой последовательности для каждого сотрудника
    SELECT 
        FIO,
        MAX(MONTH) AS end_month,     -- месяц окончания последовательности
        COUNT(*) AS seq_length
    FROM seq_groups
    GROUP BY FIO, grp
),
final_counts AS (
    -- 4. Определяем категорию и считаем сотрудников
    SELECT 
        end_month,
        CASE 
            WHEN seq_length >= 3 THEN 'Месяцев подряд 3+'
            WHEN seq_length = 2 THEN 'Месяцев подряд 2'
            ELSE 'Месяцев подряд 1'
        END AS seq_category,
        COUNT(DISTINCT FIO) AS employee_count
    FROM grouped_sequences
    GROUP BY end_month, 
             CASE 
                 WHEN seq_length >= 3 THEN 'Месяцев подряд 3+'
                 WHEN seq_length = 2 THEN 'Месяцев подряд 2'
                 ELSE 'Месяцев подряд 1'
             END
),
months_list AS (
    -- 5. Извлекаем уникальные месяцы и сортируем
    SELECT DISTINCT MONTH AS end_month
    FROM your_table
    ORDER BY end_month
)
-- 6. Формируем итоговую таблицу с динамическим списком месяцев
SELECT 
    fc.seq_category,
    ml.end_month,
    NVL(fc.employee_count, 0) AS employee_count
FROM months_list ml
CROSS JOIN (
    SELECT DISTINCT seq_category FROM final_counts
) fc_base
LEFT JOIN final_counts fc 
    ON fc.end_month = ml.end_month AND fc.seq_category = fc_base.seq_category
ORDER BY 
    CASE fc.seq_category
        WHEN 'Месяцев подряд 3+' THEN 1
        WHEN 'Месяцев подряд 2' THEN 2
        ELSE 3
    END,
    ml.end_month;
