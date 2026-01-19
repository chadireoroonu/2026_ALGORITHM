# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# https://chadireoroonu.tistory.com/343

def solution(n):
    binary = '0' + bin(n)[2:] # 0b 자르기
    
    target = binary.rfind('01') # '01' 문자열 인덱스 찾기
    answer = binary[:target] + '10' + "".join(sorted(binary[target + 2:]))

    return int(answer, 2)