WITH last_records AS (
    SELECT t.*,
           ROW_NUMBER() OVER (PARTITION BY id ORDER BY date_column DESC) AS rn
    FROM your_table t
)
SELECT *
FROM last_records
WHERE rn = 1  -- выбираем только последнюю запись для каждого ID
  AND column_not_contains_cd NOT LIKE '%CD%';  -- проверяем, что в последней записи нет 'CD'

