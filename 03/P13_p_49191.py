# 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# https://chadireoroonu.tistory.com/352

from collections import deque

def solution(n, results):
    answer = 0
    winners = [set()  for _ in range(n + 1)] # 나를 이긴 사람들 
    losers = [set() for _ in range(n + 1)] # 나한테 진 사람들
    
    for w, l in results:
        winners[l].add(w)
        losers[w].add(l)
    
    # BFS 탐색
    def battle(p, arr): # 직접 경기하지 않은 사람들과의 관계 확인
        queue = deque([p])
        people = set() # 추가할 사람들
        visited = [False] * (n + 1)
        visited[p] = True
        
        while queue:
            x = queue.popleft()
            for nx in arr[x]:
                if not visited[nx]:
                    people.add(nx)
                    visited[nx] = True
                    queue.append(nx)
                
        return people
    
    
    for p in range(1, n + 1):
        winners[p] = battle(p, winners) # 나를 이긴 사람들을 이긴 사람들 추가
        losers[p] = battle(p, losers) # 나한테 진 사람들한테 진 사람들 추가

        # 모든 사람들의 순위를 아는 경우
        if len(winners[p]) + len(losers[p]) == n - 1:
            answer += 1

    return answer