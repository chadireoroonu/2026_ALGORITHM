-- 연도 별 평균 미세먼지 농도 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/284530

SELECT
  YEAR(YM) AS YEAR,
  ROUND(AVG(PM_VAL1), 2) AS PM10, 
  ROUND(AVG(PM_VAL2), 2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR(YM)
ORDER BY YEAR

-- DATE_FORMAT을 썼더니 틀렸다고 나와서 수정했다. YEAR() 함수로 숫자 형식으로 만들어줬다.
-- 컬럼명 2.5 인식을 위해 ''로 감싸줬다.
-- GROUP BY 절에는 AS 사용하지 않고 값 넣어주자
-- 통과되는 것들도 ROUND 같은 조건들 잘 확인해서 반영하자