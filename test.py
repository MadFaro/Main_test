select mm, nvl(preapproved_credit, 0) as preapproved_credit, nvl(fullapproved_credit, 0) as fullapproved_credit
from (select mm, campaign_category, case when sum(cnt_closed) >= sum(cnt_loads_deact) then sum(cnt_closed) else sum(cnt_loads_deact) end / 1000 as total_offer_no_deact
from analytics.rap_tech_voronka_svod_prez a
where product = 'пк' and company_type = 'xsell' and (is_control_cell = 0 or is_control_cell is null) and channel = 'вкц' and a.mm < sysdate - 31
group by mm, campaign_category)
pivot (max(total_offer_no_deact) for campaign_category in ('preapproved_credit' as preapproved_credit, 'fullapproved_credit' as fullapproved_credit))
order by mm;
