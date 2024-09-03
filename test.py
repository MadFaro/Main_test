    CASE
        WHEN timezone_offset LIKE 'GTM+%' THEN 
            TO_CHAR(TO_NUMBER(SUBSTR(timezone_offset, 5)) - 3)
        WHEN timezone_offset LIKE 'GTM-%' THEN 
            TO_CHAR(3 - TO_NUMBER(SUBSTR(timezone_offset, 5)))
        ELSE
            NULL
    END AS offset_hours
