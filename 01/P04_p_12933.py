# 정수 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# https://chadireoroonu.tistory.com/333

def solution(n):
    array = list(str(n).strip())
    array.sort(reverse=True)
    
    return int("".join(map(str, array)))
