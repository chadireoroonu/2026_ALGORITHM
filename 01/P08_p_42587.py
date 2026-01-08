# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# https://chadireoroonu.tistory.com/337

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in enumerate(priorities):
        queue.append(i)
    
    while queue:
        maxi = max(queue, key=lambda x:x[1])[1]
        x, y = queue.popleft()
        if y < maxi:
            queue.append((x, y))
        else:
            answer += 1
            if x == location:
                break
    
    return answer
