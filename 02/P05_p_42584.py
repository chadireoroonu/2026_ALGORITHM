# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# https://chadireoroonu.tistory.com/347

def solution(prices):
    answer = [len(prices) - 1 - i for i in range(len(prices))]
    stack = [[prices[0], 0]]
    
    for i in range(1, len(prices)):
        while stack and prices[i] < stack[-1][0]:
            answer[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append([prices[i], i])
    
    return answer