# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# https://chadireoroonu.tistory.com/332

def solution(s):
    answer = [0, 0]
    
    # 0 제거
    def zerokill(w):
        answer[0] += 1
        count = w.count('1')
        answer[1] += len(w) - count
        
        return binary(count)
    
    
    # 2진 변환
    def binary(n):
        result = ''
        while n > 0:
            result += str(n % 2)
            n //= 2
            
        return result[::-1]
    
    
    while s != '1':
        s = zerokill(s)
    
    return answer
    