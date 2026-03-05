# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# https://chadireoroonu.tistory.com/350

from collections import deque

def solution(begin, target, words):
    visited = set([begin]) # 방문 단어 집합
    queue = deque([(begin, 0)])
    
    while queue:
        now, cnt = queue.popleft()
        
        for word in words:
            # 방문하지 않은 단어만 비교
            if word not in visited:
                miss = 0 # 다른 알파벳 수
                for i in range(len(word)):
                    if now[i] != word[i]:
                        miss += 1
                if miss == 1: # 한글자만 다른 경우
                    if word == target: # 타겟 단어일 경우
                        return cnt + 1
                    visited.add(word)
                    queue.append((word, cnt + 1))
                
    return 0