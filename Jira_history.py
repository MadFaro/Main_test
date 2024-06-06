WITH ActiveTime AS (
    SELECT
        operatorid,
        threadid,
        MIN(created) AS start_time,
        MAX(created) AS end_time,
        (MAX(created) - MIN(created)) * 24 * 60 * 60 AS active_seconds
    FROM
        chat_logs
    WHERE
        kind = 2
    GROUP BY
        operatorid,
        threadid
),
WorkloadTime AS (
    SELECT
        operatorid,
        threadid,
        SUM(EXTRACT(SECOND FROM (LEAD(created, 1) OVER (PARTITION BY threadid, operatorid ORDER BY created) - created))) AS workload_seconds
    FROM
        chat_logs
    WHERE
        kind = 2
    GROUP BY
        operatorid,
        threadid
)
SELECT
    a.operatorid,
    (SUM(w.workload_seconds) / SUM(a.active_seconds)) * 100 AS net_agent_occupancy
FROM
    ActiveTime a
JOIN
    WorkloadTime w ON a.operatorid = w.operatorid AND a.threadid = w.threadid
GROUP BY
    a.operatorid;

