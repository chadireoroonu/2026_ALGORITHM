# 서버 증설 횟수
# https://school.programmers.co.kr/learn/courses/30/lessons/389479
# https://chadireoroonu.tistory.com/341

def solution(players, m, k):
    answer = [0] * 24
    server = 0
    
    for i in range(24):
        # 서버 줄이기
        if i >= k:
            server -= answer[i - k]
        
        # 서버 늘리기
        need = players[i] // m
        if need > server:
            answer[i] = need - server
            server += need - server
    
    return sum(answer)
