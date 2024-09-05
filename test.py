select * from (
select MM, CAMPAIGN_CATEGORY, case when sum(CNT_CLOSED)>= sum (CNT_LOADS_DEACT) then sum(CNT_CLOSED) else sum (CNT_LOADS_DEACT) end/1000 as total_offer_NO_DEACT
from ANALYTICS.RAP_TECH_VORONKA_SVOD_PREZ a
where PRODUCT='ПК'
and COMPANY_TYPE='XSELL' and (IS_CONTROL_CELL=0 or IS_CONTROL_CELL is null)
and CHANNEL='ВКЦ'
and a.MM<sysdate-31
group by MM, CAMPAIGN_CATEGORY
order by MM, CAMPAIGN_CATEGORY)
where CAMPAIGN_CATEGORY is not null

MM	CAMPAIGN_CATEGORY	TOTAL_OFFER_NO_DEACT
01.03.2024 0:00	PreApproved_Credit	4,22
01.03.2024 0:00	FullApproved_Credit	97,988
01.04.2024 0:00	PreApproved_Credit	30,203
01.04.2024 0:00	FullApproved_Credit	63,819
01.05.2024 0:00	PreApproved_Credit	45,562
01.05.2024 0:00	FullApproved_Credit	44,258
01.06.2024 0:00	PreApproved_Credit	13,676
01.06.2024 0:00	FullApproved_Credit	34,845
01.07.2024 0:00	PreApproved_Credit	1,733
01.07.2024 0:00	FullApproved_Credit	58,95
01.08.2024 0:00	PreApproved_Credit	1,739
01.08.2024 0:00	FullApproved_Credit	78,478

