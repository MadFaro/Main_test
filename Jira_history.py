select 
    a.APPLICATION_SRC_ID as APPLICATIONID,
    min_b.ACTIVITYSTART as dt_begin_crif,  -- минимальное значение b.STARTDATE
    max_b.ACTIVITYEND as dt_end_crif,      -- максимальное значение b.STARTDATE + ACTIVITYDURATION
    a.PRODUCT_CRIF_CODE as product_name_crif,
    'Ипотека' as product_name,
    b.STARTDATE as ACTIVITYSTART,
    b.STARTDATE + b.ACTIVITYDURATION as ACTIVITYEND,
    b.PHASECACHEID as PHASECACHEID,
    b.RESOURCENAME_PHASE as PHASENAME,
    b.USERID,
    d.TABNUM,
    d.fio,
    d.date_begin_ipot,
    d.date_end_ipot,
    m.CLIENT_KIH_ID as client_id,
    m.CHANNEL_TYPE_NAME,
    c.finalstatus
from 
    DM_MRK.DM_MRK_APPLICATION@cdw.prod a
left join 
    DM.APPLICATION_HISTORY b 
    on a.APPLICATION_SRC_ID = b.APPLICATIONID
left join 
    (select 
        APPLICATIONID,
        min(STARTDATE) as ACTIVITYSTART,
        max(STARTDATE + ACTIVITYDURATION) as ACTIVITYEND
     from 
        DM.APPLICATION_HISTORY
     group by 
        APPLICATIONID) min_b
    on a.APPLICATION_SRC_ID = min_b.APPLICATIONID
left join 
    analytics.NP_application_MTG_2 m 
    on a.APPLICATION_SRC_ID = m.APPLICATION_ID
left join 
    analytics.kuz_approval_rate c 
    on a.APPLICATION_SRC_ID = c.APPLICATION_ID
left join 
    analytics.kdi_ipoteka_operators d 
    on b.USERID = d.USERID 
where 
    a.CRIF_OPEN_DT >= date '2024-02-02' 
    and a.STREAM_TYPE = 'MTG_CAMO';
