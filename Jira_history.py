SELECT
    v1.date_time AS date_time_v1,
    v1.phone_number AS phone_number_v1,
    v2.date_time AS date_time_v2,
    v2.phone_number AS phone_number_v2
FROM
    (SELECT
        v1.date_time,
        v1.phone_number,
        v2.date_time AS date_time_v2,
        v2.phone_number AS phone_number_v2,
        ROW_NUMBER() OVER (PARTITION BY v1.date_time, v1.phone_number ORDER BY ABS(v1.date_time - v2.date_time)) AS rn
    FROM
        v1
    LEFT JOIN v2 ON v1.phone_number = v2.phone_number) sub
WHERE
    sub.rn = 1;

