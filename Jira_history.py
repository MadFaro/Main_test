SELECT a.OWNER as owner, a.object_name AS procedure_name
FROM all_objects a
JOIN all_source b ON a.object_name = b.name
WHERE a.object_type = 'PROCEDURE' and (lower(a.object_name) like '%np%' or lower(a.object_name) like '%rap%')
and b.text like '%@%'
