SELECT a.OWNER as owner,
       a.object_name AS procedure_name,
       SUBSTR(b.text, INSTR(b.text, '@', 1) + 1, LENGTH(b.text) - INSTR(b.text, '@', 1)) AS table_name_right,
       SUBSTR(b.text, 1, INSTR(b.text, '@', 1) - 1) AS table_name_left,
       SUBSTR(b.text, 1, INSTR(b.text, '@', 1) - 1) || SUBSTR(b.text, INSTR(b.text, '@', 1) + 1, LENGTH(b.text) - INSTR(b.text, '@', 1)) AS table_name_full
FROM all_objects a
JOIN all_source b ON a.object_name = b.name
WHERE a.object_type = 'PROCEDURE'
  AND (LOWER(a.object_name) LIKE '%np%' OR LOWER(a.object_name) LIKE '%rap%')
  AND b.text LIKE '%@%';
