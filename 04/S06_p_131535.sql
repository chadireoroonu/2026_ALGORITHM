-- 조건에 맞는 회원수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131535

SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE JOINED LIKE '2021%' AND 20 <= AGE AND AGE < 30