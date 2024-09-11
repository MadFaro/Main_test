PL/SQL: SQL Statement ignored
PL/SQL: ORA-00947: не хватает значений для данных

execute immediate 'truncate table analytics.tolog_agn_dpupp_kc_kg_proverka_res_sms_model_cc_kc_2';
insert into analytics.tolog_agn_dpupp_kc_kg_proverka_res_sms_model_cc_kc_2
select REPORT_DATE,max(rn) as rn
from analytics.tolog_agn_dpupp_kc_kg_proverka_res_sms_model_cc_kc
group by REPORT_DATE;
