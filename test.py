create table rap_reten_call_closed as
select /*+parallel(4)*/
distinct rap.*,
max(case when b.CLIENT_DID is not null and b.product_category_name <> 'Договор на текущий счет для кредитной карты' 
then 1 else 0 end) over (partition by call_id,dt) as card_close_debet,
max(case when b.CLIENT_DID is not null and b.call_flag=1 
and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end)
over (partition by call_id,dt) card_close_CC_debet,
max(case when b.CLIENT_DID is not null and b.call_flag=0 
and b.product_category_name <> 'Договор на текущий счет для кредитной карты' then 1 else 0 end)
over (partition by call_id,dt) as card_close_OFICE_debet,
max(case when b.CLIENT_DID is not null and b.product_category_name = 'Договор на текущий счет для кредитной карты' 
then 1 else 0 end) over (partition by call_id,dt) as card_close_credit,
max(case when b.CLIENT_DID is not null and b.call_flag=1 
and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end)
over (partition by call_id,dt) as card_close_CC_credit,
max(case when b.CLIENT_DID is not null and b.call_flag=0 
and b.product_category_name = 'Договор на текущий счет для кредитной карты' then 1 else 0 end)
over (partition by call_id,dt) as card_close_OFICE_credit,
max(case when d.CLIENT_DID is not null then 1 else 0 end)over (partition by call_id,dt) as have_termination
from rap_reten_motiv_com rap
left join rap_reten_card_closed b on rap.CLIENT_DID=b.CLIENT_DID and trunc(b.TIME_CLOSE)>=trunc(rap.DT)--закрыто после звонка
left join rap_reten_card_closed d on rap.CLIENT_DID=d.CLIENT_DID and trunc(d.TIME_CLOSE)<trunc(rap.DT)
