SELECT a.OWNER as owner,
       a.object_name AS procedure_name,
       c.table_name
FROM all_objects a
JOIN all_source b ON a.object_name = b.name
JOIN all_tab_columns c ON b.text LIKE '%' || c.table_name || '%@%'
WHERE a.object_type = 'PROCEDURE'
  AND (LOWER(a.object_name) LIKE '%np%' OR LOWER(a.object_name) LIKE '%rap%')
  AND b.text LIKE '%@%';
