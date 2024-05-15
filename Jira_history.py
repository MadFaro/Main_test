SELECT
    s.username,
    s.sid,
    s.serial#,
    SUM(ss.value) AS cpu_usage
FROM
    v$session s
    JOIN v$sesstat ss ON s.sid = ss.sid
    JOIN v$statname st ON ss.statistic# = st.statistic#
WHERE
    st.name = 'CPU used by this session'
GROUP BY
    s.username, s.sid, s.serial#
ORDER BY
    cpu_usage DESC;

