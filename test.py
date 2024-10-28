SELECT *
FROM users
WHERE strftime('%m-%d', birthday) = strftime('%m-%d', date('now', '-1 day'));
