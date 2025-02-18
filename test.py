create or replace procedure   tolog_retentions_crm as 
begin
execute immediate 'truncate table analytics.tolog_tk_ret2';
execute immediate 'insert into analytics.tolog_tk_ret2
select /*+ PARALLEL(16) */ * from campaign.v_contact_and_dtlcontact
where CAMPAIGN_NAME = ''RETENTION_DID''';

execute immediate 'truncate table analytics.tolog_tk_card';
execute immediate 'insert into analytics.tolog_tk_card
SELECT * FROM dm.cards';
...

execute immediate 'update analytics.tolog_tk_retation_oct6
set card_type_new=''CC''
where card_type_new=''DC'' and REZ like ''%_120%''';
...

commit;
end;
