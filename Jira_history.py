create table analytics.NP_v_contact_and_dtlcontact_2 PARALLEL (8) as Select * from campaign.v_contact_and_dtlcontact where RUN_DATE_TIME>='01.04.24'
Error report -
ORA-12818: неверная опция во фразе PARALLEL
12818. 00000 -  "invalid option in PARALLEL clause"
*Cause:    an unrecognized option was used within a PARALLEL clause.
*Action:   specify any combination of DEGREE { <n> | DEFAULT } and
           INSTANCES { <n> | DEFAULT } within the PARALLEL clause.
