WITH tab_1 AS (
  SELECT CLIENT_DID AS client_id,
         CAST(INT_CREATE_DATE AS DATE) AS date_added
  FROM analytics.rap_tech_voronka_polotn 
  WHERE INT_CREATE_DATE >= DATE '2024-06-01' 
    AND TEMPLATE_CODE IN ('pk_difrate_35', 'pk_topup_35', 'tm_cc_35')
),
client_adds AS (
  SELECT
    client_id,
    date_added,
    LAG(date_added) OVER (PARTITION BY client_id ORDER BY date_added) AS prev_date
  FROM tab_1
),
date_differences AS (
  SELECT
    client_id,
    date_added,
    prev_date,
    CASE
      WHEN prev_date IS NOT NULL THEN (date_added - prev_date)
      ELSE NULL
    END AS day_diff
  FROM client_adds
),
categorized_diffs AS (
  SELECT
    client_id,
    date_added,
    prev_date,
    day_diff,
    CASE
      WHEN day_diff BETWEEN 1 AND 14 THEN '1-14 days'
      WHEN day_diff BETWEEN 15 AND 20 THEN '15-20 days'
      WHEN day_diff BETWEEN 21 AND 25 THEN '21-25 days'
      WHEN day_diff BETWEEN 26 AND 30 THEN '26-30 days'
      ELSE 'More than 30 days or First entry'
    END AS interval_category
  FROM date_differences
)
SELECT
  TO_CHAR(TRUNC(date_added, 'MM'), 'YYYY-MM') AS month,
  interval_category,
  COUNT(*) AS count_of_repeats
FROM categorized_diffs
WHERE interval_category != 'More than 30 days or First entry'
GROUP BY TO_CHAR(TRUNC(date_added, 'MM'), 'YYYY-MM'), interval_category
ORDER BY month, interval_category;
