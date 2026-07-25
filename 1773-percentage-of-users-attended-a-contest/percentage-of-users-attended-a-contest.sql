SELECT R.contest_id, ROUND(COUNT(U.user_id) / (SELECT COUNT(user_id) FROM Users) * 100, 2) as percentage
FROM Users U RIGHT JOIN Register R
ON U.user_id = R.user_id
GROUP BY R.contest_id
ORDER BY -percentage, R.contest_id
