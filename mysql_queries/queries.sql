TEST 1:

SELECT users.email,users.username,users.created_at,
user_profiles.first_name, user_profiles.last_name, user_profiles.gender, user_profiles.birth_date
FROM users
INNER JOIN user_profiles
ON users.id = user_profiles.user_id;


TEST 2:
SELECT user_profile_id, ROUND(SUM(amount),2) total_amount, type, COUNT(type)
FROM transactions
WHERE type = 'deposit' AND user_profile_id = '2'
GROUP BY user_profile_id, type


TEST 3:

SELECT type, COUNT(type), ROUND(SUM(amount),2)
FROM transactions
GROUP BY type;