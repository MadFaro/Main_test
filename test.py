SELECT 
    timezone_offset,
    CASE
        WHEN timezone_offset LIKE 'GTM+%' THEN 
            CASE
                WHEN TO_NUMBER(SUBSTR(timezone_offset, 5)) > 3 THEN
                    '+' || LPAD(TO_NUMBER(SUBSTR(timezone_offset, 5)) - 3, 2, '0') || ':00'
                WHEN TO_NUMBER(SUBSTR(timezone_offset, 5)) = 3 THEN
                    '0:00'
                ELSE
                    '-' || LPAD(3 - TO_NUMBER(SUBSTR(timezone_offset, 5)), 2, '0') || ':00'
            END
        WHEN timezone_offset LIKE 'GTM-%' THEN 
            '-' || LPAD(3 + TO_NUMBER(SUBSTR(timezone_offset, 5)), 2, '0') || ':00'
        ELSE
            NULL
    END AS formatted_timezone
FROM 
    your_table_name;
