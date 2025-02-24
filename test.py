WITH green_zone AS (
    -- 1. Сотрудники в зеленой зоне
    SELECT 
        FIO,
        MONTH
    FROM your_table
    WHERE RANK_SUM = 1
),
seq_with_counts AS (
    -- 2. Определяем последовательности для каждого месяца
    SELECT 
        FIO,
        MONTH,
        ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY MONTH) AS rn,
        ADD_MONTHS(MONTH, -ROW_NUMBER() OVER (PARTITION BY FIO ORDER BY MONTH)) AS grp
    FROM green_zone
),
sequence_lengths AS (
    -- 3. Считаем длину последовательности до каждого месяца (а не только в конце)
    SELECT 
        FIO,
        MONTH,
        COUNT(*) OVER (PARTITION BY FIO, grp ORDER BY MONTH ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS seq_length
    FROM seq_with_counts
),
categorized_sequences AS (
    -- 4. Присваиваем категорию последовательности
    SELECT 
        MONTH,
        CASE 
            WHEN seq_length >= 3 THEN 'Месяцев подряд 3+'
            WHEN seq_length = 2 THEN 'Месяцев подряд 2'
            ELSE 'Месяцев подряд 1'
        END AS seq_category,
        COUNT(DISTINCT FIO) AS employee_count
    FROM sequence_lengths
    GROUP BY MONTH, 
             CASE 
                 WHEN seq_length >= 3 THEN 'Месяцев подряд 3+'
                 WHEN seq_length = 2 THEN 'Месяцев подряд 2'
                 ELSE 'Месяцев подряд 1'
             END
),
all_categories AS (
    -- 5. Убедимся, что каждая категория есть в каждом месяце
    SELECT DISTINCT 
        c.seq_category,
        m.MONTH
    FROM categorized_sequences c
    CROSS JOIN (SELECT DISTINCT MONTH FROM green_zone) m
),
final_result AS (
    -- 6. Объединяем, чтобы вывести нули для отсутствующих категорий
    SELECT 
        a.MONTH,
        a.seq_category,
        NVL(c.employee_count, 0) AS employee_count
    FROM all_categories a
    LEFT JOIN categorized_sequences c 
        ON a.MONTH = c.MONTH AND a.seq_category = c.seq_category
)
-- 7. Выводим результат по порядку
SELECT 
    seq_category,
    MONTH,
    employee_count
FROM final_result
ORDER BY 
    CASE seq_category
        WHEN 'Месяцев подряд 3+' THEN 1
        WHEN 'Месяцев подряд 2' THEN 2
        ELSE 3
    END,
    MONTH;

