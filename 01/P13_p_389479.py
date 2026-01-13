# 서버 증설 횟수
# https://school.programmers.co.kr/learn/courses/30/lessons/389479
# https://chadireoroonu.tistory.com/341

def solution(players, m, k):
    answer = 0
    server_count = 0
    server_open = [0] * 24
    
    for i in range(24):
        # 서버 줄이기
        if i >= k:
            server_count -= server_open[i - k]
            
        # 서버 늘리기
        plus = 0
        if players[i] >= m * server_count:
            plus = (players[i] - (m * server_count)) // m  
        
        server_open[i] = plus
        server_count += plus
        answer += plus
    
    return answer
