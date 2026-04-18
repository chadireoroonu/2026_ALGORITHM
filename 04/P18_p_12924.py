# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    nums = [1] * n
    
    for i in range(1, n):
        nums[i] += i + nums[i - 1]
        
    first = second = 0
    
    while first < n and second < n:
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
