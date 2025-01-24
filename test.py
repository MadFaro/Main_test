WITH source_data AS (
    WITH CTSGI AS (
        -- Основной запрос, объединяющий данные из нескольких таблиц
        SELECT
            t.SkillGroupSkillTargetID,
            t.DateTime,
            SUM(COALESCE(t.CallsAnswered, 0)) AS sumanswered,
            SUM(COALESCE(t.AnswerWaitTime, 0)) AS sumanstime,
            SUM(COALESCE(t.RouterCallsAbandQ, 0)) AS sumabandoned,
            SUM(COALESCE(t.CallDelayAbandTime, 0)) AS sumabandtime,
            SUM(COALESCE(t.CallsOfferedRouted, 0)) AS vhodyaschiye
        FROM (
            SELECT
                Call_Type_SG_Interval.*,
                SG.EnterpriseName AS SGEnterpriseName,
                SG.SkillTargetID AS SGSkillTargetID,
                Media_Routing_Domain.EnterpriseName AS Media
            FROM
                ODS.ODS_DLC_CALL_TYPE_SG_INTERVAL@cdw.prod Call_Type_SG_Interval
                JOIN ODS.ODS_CSC_T_MEDIA_ROUTING_DOMAIN@cdw.prod Media_Routing_Domain
                    ON SG.MRDomainID = Media_Routing_Domain.MRDomainID
                JOIN ODS.ODS_CSC_SKILL_GROUP@cdw.prod SG
                    ON SG.SkillTargetID = Call_Type_SG_Interval.SkillGroupSkillTargetID
            WHERE
                SG.SkillTargetID NOT IN (
                    SELECT BaseSkillTargetID
                    FROM ODS.ODS_CSC_SKILL_GROUP@cdw.prod
                    WHERE Priority > 0 AND Deleted <> 'Y'
                )
            UNION ALL
            SELECT
                Call_Type_SG_Interval.*,
                Precision_Queue.EnterpriseName AS SGEnterpriseName,
                SG.SkillTargetID AS SGSkillTargetID,
                Media_Routing_Domain.EnterpriseName AS Media
            FROM
                ODS.ODS_DLC_CALL_TYPE_SG_INTERVAL@cdw.prod Call_Type_SG_Interval
                JOIN ODS.ODS_CSC_T_MEDIA_ROUTING_DOMAIN@cdw.prod Media_Routing_Domain
                    ON SG.MRDomainID = Media_Routing_Domain.MRDomainID
                JOIN ODS.ODS_CSC_PRECISION_QUEUE@cdw.prod Precision_Queue
                    ON SG.PrecisionQueueID = Precision_Queue.PrecisionQueueID
                JOIN (
                    SELECT DISTINCT
                        CASE
                            WHEN Skill_Group.PrecisionQueueID IS NULL THEN Skill_Group.EnterpriseName
                            ELSE SGPQ.EnterpriseName
                        END AS EnterpriseName,
                        CASE
                            WHEN Skill_Group.PrecisionQueueID IS NULL THEN Skill_Group.SkillTargetID
                            ELSE SGPQ.SkillTargetID
                        END AS SkillTargetID,
                        CASE
                            WHEN Skill_Group.PrecisionQueueID IS NULL THEN NULL
                            ELSE SGPQ.PrecisionQueueID
                        END AS PrecisionQueueID,
                        MRDomainID
                    FROM
                        ODS.ODS_CSC_SKILL_GROUP@cdw.prod Skill_Group
                        LEFT JOIN (
                            SELECT
                                MIN(EnterpriseName) AS EnterpriseName,
                                MIN(SkillTargetID) AS SkillTargetID,
                                PrecisionQueueID
                            FROM
                                ODS.ODS_CSC_SKILL_GROUP@cdw.prod
                            WHERE
                                PrecisionQueueID IS NOT NULL
                            GROUP BY
                                PrecisionQueueID
                        ) SGPQ
                        ON Skill_Group.PrecisionQueueID = SGPQ.PrecisionQueueID
                ) SG
                ON SG.PrecisionQueueID = Call_Type_SG_Interval.PrecisionQueueID
        ) t
        GROUP BY
            t.SkillGroupSkillTargetID,
            t.DateTime
    )
    SELECT
        SGI.DateTime AS Interval,
        TRUNC(SGI.DateTime) AS DATE_,
        Skill_Group.EnterpriseName AS FullName,
        Skill_Group.SkillTargetID AS SkillGroupSkillID,
        Bucket_Intervals.IntervalUpperBound1 AS int1,
        Bucket_Intervals.IntervalUpperBound2 AS int2,
        Bucket_Intervals.IntervalUpperBound3 AS int3,
        Bucket_Intervals.IntervalUpperBound4 AS int4,
        Bucket_Intervals.IntervalUpperBound5 AS int5,
        Bucket_Intervals.IntervalUpperBound6 AS int6,
        Bucket_Intervals.IntervalUpperBound7 AS int7,
        Bucket_Intervals.IntervalUpperBound8 AS int8,
        Bucket_Intervals.IntervalUpperBound9 AS int9,
        SGI.TimeZone AS TimeZone,
        SGI.DbDateTime AS DbDateTime,
        Media_Routing_Domain.EnterpriseName AS Media,
        Media_Routing_Domain.MRDomainID AS MRDomainID,
        MAX(COALESCE(CTSGI.sumanswered, 0)) AS Sumanswered,
        MAX(COALESCE(CTSGI.sumanstime, 0)) AS Sumanstime,
        MAX(COALESCE(CTSGI.sumabandoned, 0)) AS Sumabandoned,
        MAX(COALESCE(CTSGI.sumabandtime, 0)) AS Sumabandtime
    FROM
        ODS.ODS_CSC_SKILL_GROUP@cdw.prod Skill_Group
        JOIN ODS.ODS_DLC_T_SKILL_GROUP_INTERVAL@cdw.prod SGI
            ON Skill_Group.SkillTargetID = SGI.SkillTargetID
        LEFT JOIN CTSGI
            ON CTSGI.SkillGroupSkillTargetID = SGI.SkillTargetID
            AND CTSGI.DateTime = SGI.DateTime
        JOIN ODS.ODS_CSC_T_MEDIA_ROUTING_DOMAIN@cdw.prod Media_Routing_Domain
            ON Skill_Group.MRDomainID = Media_Routing_Domain.MRDomainID
        JOIN ODS.ODS_CSC_T_Bucket_Intervals@cdw.prod Bucket_Intervals
            ON Bucket_Intervals.BucketIntervalID = SGI.BucketIntervalID
    WHERE
        SGI.DateTime >= TRUNC(ADD_MONTHS(SYSDATE, -6), 'MM')
        AND Skill_Group.EnterpriseName IN (
            'CCM_PG_1.SG_DDO_ActiveCredit',
            'CCM_PG_1.SG_DDO_CityBank',
            'CCM_PG_1.SG_Operator',
            'CCM_PG_1.SG_Operator_VIP',
            'CCM_PG_1.SG_DDO_Ipoteka',
            'CCM_PG_1.SG_DDO_Broker',
            'CCM_PG_1.SG_Operator_1'
        )
    GROUP BY
        Skill_Group.EnterpriseName,
        Skill_Group.SkillTargetID,
        Media_Routing_Domain.EnterpriseName,
        Media_Routing_Domain.MRDomainID,
        SGI.BucketIntervalID,
        Bucket_Intervals.IntervalUpperBound1,
        Bucket_Intervals.IntervalUpperBound2,
        Bucket_Intervals.IntervalUpperBound3,
        Bucket_Intervals.IntervalUpperBound4,
        Bucket_Intervals.IntervalUpperBound5,
        Bucket_Intervals.IntervalUpperBound6,
        Bucket_Intervals.IntervalUpperBound7,
        Bucket_Intervals.IntervalUpperBound8,
        Bucket_Intervals.IntervalUpperBound9,
        SGI.DateTime,
        TRUNC(SGI.DateTime),
        SGI.TimeZone,
        SGI.DbDateTime
),
grouped_data AS (
    SELECT
        DATE_,
        FullName,
        SUM(Sumanswered) AS answer,
        SUM(Sumanstime) AS ans_time,
        SUM(Sumabandoned) AS aban,
        SUM(Sumabandtime) AS aba_time
    FROM
        source_data
    GROUP BY
        DATE_,
        FullName
)
SELECT
    DATE_,
    FullName,
    answer,
    ans_time,
    aban,
    aba_time,
    TO_CHAR(DATE_, 'YY.MMM') AS "Месяц",
    TO_CHAR(TRUNC(DATE_, 'IW'), 'DD') || '-' || TO_CHAR(TRUNC(DATE_ + 6, 'IW'), 'DD.MM') AS "Неделя",
    CASE
        WHEN FullName IN (
            'CCM_PG_1.SG_DDO_ActiveCredit',
            'CCM_PG_1.SG_DDO_CityBank',
            'CCM_PG_1.SG_Operator',
            'CCM_PG_1.SG_Operator_1',
            'CCM_PG_1.SG_Operator_2',
            'CCM_PG_1.SG_Operator_3',
            'CCM_PG_1.SG_Operator_4',
            'CCM_PG_1.SG_Operator_5'
        ) THEN 'All'
        ELSE FullName
    END AS "Группа"
FROM
    grouped_data
ORDER BY
    DATE_,
    FullName;
