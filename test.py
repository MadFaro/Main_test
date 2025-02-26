SELECT 
  REPLACE(REPLACE(REGEXP_SUBSTR(, '[A-Za-z]+\_[A-Za-z]+\.[A-Za-z]+'), '_', ''), '.', '') AS result
FROM dual;

