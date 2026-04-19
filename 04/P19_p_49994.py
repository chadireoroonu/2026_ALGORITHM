# 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    i, j = 0, 0
    visited = set() # 길 방문여부
    directions = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)} # 이동 방향
    
    for d in dirs: # 이동 명령어 처리
        di, dj = directions[d]
        ni, nj = i + di, j + dj
        if -5 <= ni <= 5 and -5 <= nj <= 5: # 배열 벗어나는지 확인
            # 방문 여부 확인, 처리
            if (i, j, ni, nj) not in visited and (ni, nj, i, j) not in visited:
                answer += 1
                visited.add((i, j, ni, nj))
            i, j = ni, nj # 이동
                
    return answer
