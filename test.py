create table analytics.tolog_shop_users_bd as
select distinct UPPER(a."Email") as EMAIL, b.BIRTH_DATE  from USB_FNS_LOADER.KO_AD_BK_NIGHT a
left join REF.KO_AD_STORY b on a."NetName" = b.NETNAME
where a."DEP_ID_L3"='40050455' AND a."StateNP"=1 AND a."StateAD"=1 and UPPER(a."Email") not in (
select * from ANALYTICS.TOLOG_SHOP_USERS
)


Error starting at line : 1 in command -
create table analytics.tolog_shop_users_bd as
select distinct UPPER(a."Email") as EMAIL, b.BIRTH_DATE  from USB_FNS_LOADER.KO_AD_BK_NIGHT a
left join REF.KO_AD_STORY b on cast(a."NetName" as VARCHAR2(200)) = cast(b.NETNAME as VARCHAR2(200))
where a."DEP_ID_L3"='40050455' AND a."StateNP"=1 AND a."StateAD"=1 and UPPER(a."Email") not in (
select * from ANALYTICS.TOLOG_SHOP_USERS
)
Error report -
ORA-00997: неверное использование типа данных LONG
00997. 00000 -  "illegal use of LONG datatype"
*Cause:    
*Action:

