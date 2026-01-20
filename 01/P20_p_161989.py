# 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# https://chadireoroonu.tistory.com/344

def solution(n, m, section):
    answer = 0
    last = 0
    
    for s in section:
        if s > last:
            answer += 1
            last = s + m - 1
    
    return answer
