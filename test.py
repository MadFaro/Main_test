select trunc(DT, 'mm') as DT, TABEL, DIRECTION, PODRAZDELENIE, OPERATOR,  SUBJ1, PRODUCT1, REZ1, count(distinct CALL_ID) as cnt from ANALYTICS.KDI_SIEBEL_PAST
where DT >=date'2024-01-01' and TYPE = 'Вызов - входящий'
group by trunc(DT, 'mm'), TABEL, DIRECTION, PODRAZDELENIE, OPERATOR,  SUBJ1, PRODUCT1, REZ1,
