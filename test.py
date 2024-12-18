WITH grouped_periods AS (
    SELECT
        FI_,
        Type_,
        Group_,
        Start_,
        End_,
        Direction_,
        Day_,
        EXTRACT(YEAR FROM Day_) AS year_,
        EXTRACT(MONTH FROM Day_) AS month_,
        SUM(CASE 
                WHEN TRUNC(Day_) - LAG(TRUNC(Day_)) OVER (PARTITION BY FI_, Type_, Group_, EXTRACT(YEAR FROM Day_), EXTRACT(MONTH FROM Day_) ORDER BY Day_) > 1 THEN 1 
                ELSE 0 
            END) OVER (PARTITION BY FI_, Type_, Group_, EXTRACT(YEAR FROM Day_), EXTRACT(MONTH FROM Day_) ORDER BY Day_) AS group_id
    FROM 
        your_table
)
SELECT 
    FI_,
    Type_,
    Group_,
    year_,
    month_,
    COUNT(DISTINCT group_id) AS status_count
FROM 
    grouped_periods
GROUP BY 
    FI_,
    Type_,
    Group_,
    year_,
    month_
ORDER BY 
    FI_, year_, month_;

