# 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# https://chadireoroonu.tistory.com/334

def solution(numbers):
    answer = [-1] * len(numbers) # 뒤에 있는 큰 수가 없으면 -1 설정
    stack = [numbers[-1]] # 맨 뒤 숫자를 넣고 시작
    
    for i in range(len(numbers)-2, -1, -1): # numbers 거꾸로 순회
        while stack:
            # 뒤에 있는 큰 수를 찾으면 기록 및 중단
            if stack[-1] > numbers[i]:
                answer[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(numbers[i])
    return answer
