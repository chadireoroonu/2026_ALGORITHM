# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# https://chadireoroonu.tistory.com/337

from collections import deque

def solution(priorities, location):
    answer = 0 # 현재까지 실행된 프로세스 수
    queue = deque()
    
    for i in enumerate(priorities):
        queue.append(i)
    
    # 우선순위 내림차순 정렬
    priorities.sort(reverse=True)
    
    while queue:
        x, y = queue.popleft()
        # 남은 프로세스 중 현재 프로세스가 가장 우선순위가 높지 않은 경우
        if y < priorities[answer]:
            queue.append((x, y))
        else: # 현재 프로세스 우선순위가 가장 높은 경우
            answer += 1
            # 현재 프로세스가 순서가 궁금한 프로세스일 경우
            if x == location:
                break
    
    return answer
