SELECT *
FROM users
WHERE strftime('%m-%d', birthday) = strftime('%m-%d', 'now');
