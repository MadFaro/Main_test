SELECT 
    timezone_offset,
    CASE
        WHEN timezone_offset LIKE 'GTM+%' THEN 
            '+' || LPAD(SUBSTR(timezone_offset, 5), 2, '0') || ':00'
        WHEN timezone_offset LIKE 'GTM-%' THEN 
            '-' || LPAD(SUBSTR(timezone_offset, 5), 2, '0') || ':00'
        ELSE
            NULL
    END AS formatted_timezone
FROM 
    your_table_name;

