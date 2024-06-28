case when extract(Hour from a.DATE_BEGIN_CRIF) >=7 and extract(Hour from a.DATE_BEGIN_CRIF)<20 then 'Worktime (7:00 -20:00 МСК)' else 'Night (20:00-7:00 МСК)' end as work_time,
ORA-30076: неверное поле выборки для источника выборки
30076. 00000 -  "invalid extract field for extract source"
*Cause:    The extract source does not contain the specified extract field.
*Action:
Error at Line: 2 Column: 29
