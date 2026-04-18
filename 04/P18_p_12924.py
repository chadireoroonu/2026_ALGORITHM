# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    nums = [1] * n
    
    if n == 1: # 예외처리
        return 1
    
    for i in range(1, n): # 누적합
        nums[i] += i + nums[i - 1]
        
    first = 1
    second = 0
    
    while first < n and second < n - 1:
        if nums[first] == n:
            answer += 1
            first += 1
            continue
            
        temp = nums[first] - nums[second]
        
        if temp == n:
            answer += 1
        elif temp < n:
            first += 1
            continue
            
        second += 1
            
    return answer
