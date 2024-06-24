
Error starting at line : 1 in command -
create table ANALYTICS.TOLOG_TEMP_DBO_MSG as
SELECT /*+ PARALLEL(16) */ 
a.THREADID, 
a.DEPARTMENTID, 
a.DTM, 
a.OPERATORFULLNAME,
a.OPERATORID, 
a.CREATED, 
a.STATE, 
a.CATEGORY, 
a.SUBCATEGORY, 
a.PROVIDEDID, 
a.NAME_, 
a.SEG,
d.CREATED as DATE_MSG,
d.SENDERNAME as SENDERNAME_MSG,
d.MESSAGE as MSG,
d.KIND as KIND
FROM ANALYTICS.TOLOG_TEMP_DBO a
LEFT JOIN ODS.ODS_WIS_CHATMESSAGE@cdw.prod d on a.THREADID = d.THREADID
Error report -
ORA-12899: значение для столбца ??? слишком велико (фактическое: 4046, максимальное: 4000)
12899. 00000 -  "value too large for column %s (actual: %s, maximum: %s)"
*Cause:    An attempt was made to insert or update a column with a value
           which is too wide for the width of the destination column.
           The name of the column is given, along with the actual width
           of the value, and the maximum allowed width of the column.
           Note that widths are reported in characters if character length
           semantics are in effect for the column, otherwise widths are
           reported in bytes.
*Action:   Examine the SQL statement for correctness.  Check source
           and destination column data types.
           Either make the destination column wider, or use a subset
           of the source column (i.e. use substring).
